## Example 1

**Intent:**
a forum for people who restore old motorcycles

**Spec:**
```
Type:       Web application (forum)
Auth:       Email + password registration, session cookies
Data model: User(id, username, email, password_hash, avatar_url)
            Board(id, name, description)
            Thread(id, board_id -> Board, author_id -> User, title, created_at)
            Post(id, thread_id -> Thread, author_id -> User, body, created_at)
Features:   - Create threads in boards like Engines, Bodywork and Electrics
            - Reply to threads with text and photos
            - Search threads by keyword and bike model
            - Mark a reply as the solution
            - Let moderators lock or move threads
API:        REST
            GET  /boards
            GET  /boards/{id}/threads
            POST /threads
            GET  /threads/{id}
            POST /threads/{id}/posts
            PATCH /threads/{id}
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, HTMX
```

---

## Example 2

**Intent:**
Can you make a website where local musicians can find bandmates? Like you post what instrument you play and what you're looking for.

**Spec:**
```
Type:       Web application (community matching)
Auth:       Email + password registration, JWT
Data model: Musician(id, name, email, password_hash, city, instruments, genres, bio)
            Listing(id, musician_id -> Musician, looking_for_instrument, genre, city, created_at)
            Message(id, sender_id -> Musician, receiver_id -> Musician, body, sent_at)
Features:   - Create a profile with instruments, genres and audio sample links
            - Post a "looking for" listing
            - Filter listings by city, instrument and genre
            - Send private messages to other musicians
            - Close a listing when the spot is filled
API:        REST
            POST /auth/register
            GET  /listings?city=&instrument=
            POST /listings
            DELETE /listings/{id}
            POST /messages
            GET  /messages
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 3

**Intent:**
online course platform where I can sell my watercolor painting lessons

**Spec:**
```
Type:       Web application (online course platform)
Auth:       Email + password login for students and the instructor, Stripe Checkout for purchases
Data model: Course(id, title, description, price_cents, cover_url)
            Lesson(id, course_id -> Course, title, video_url, position)
            Student(id, email, password_hash)
            Enrollment(id, student_id -> Student, course_id -> Course, purchased_at)
            LessonProgress(student_id -> Student, lesson_id -> Lesson, completed_at)
Features:   - Upload video lessons and order them inside a course
            - Sell courses with one-time payment via Stripe
            - Stream lessons only to enrolled students
            - Track which lessons each student has finished
            - Show the instructor sales and enrollment numbers
API:        REST
            GET  /courses
            GET  /courses/{id}
            POST /checkout/{course_id}
            POST /webhooks/stripe
            GET  /courses/{id}/lessons
            POST /lessons/{id}/complete
Storage:    PostgreSQL, Mux (video hosting)
Tech stack: Next.js, Prisma, Stripe, Mux
```

---

## Example 4

**Intent:**
blog

**Spec:**
```
Type:       Web application (blog)
Auth:       Single admin login (email + password)
Data model: Post(id, title, slug, body_markdown, published_at, status)
            Tag(id, name)
            PostTag(post_id -> Post, tag_id -> Tag)
Features:   - Write posts in Markdown with a live preview
            - Save drafts and publish later
            - Tag posts and list posts by tag
            - Generate an RSS feed
            - Show a paginated list of recent posts
API:        REST
            GET  /posts
            GET  /posts/{slug}
            POST /admin/posts
            PUT  /admin/posts/{id}
            GET  /feed.xml
Storage:    SQLite
Tech stack: Python, Flask, Jinja2
```

---

## Example 5

**Intent:**
i run a small dog walking group and want a site where members can sign up for walks

**Spec:**
```
Type:       Web application (event sign-up)
Auth:       Email magic-link login
Data model: Member(id, name, email, dog_name)
            Walk(id, title, meeting_point, starts_at, max_dogs)
            Signup(id, walk_id -> Walk, member_id -> Member, created_at)
Features:   - Post upcoming walks with meeting point and time
            - Let members sign up and cancel
            - Stop sign-ups when the walk is full
            - Email members a reminder the day before
            - Show organisers a list of who is coming
API:        REST
            GET  /walks
            POST /walks
            POST /walks/{id}/signup
            DELETE /walks/{id}/signup
            GET  /walks/{id}/attendees
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Action Mailer
```

---

## Example 6

**Intent:**
job board for remote rust developers

**Spec:**
```
Type:       Web application (job board)
Auth:       Employer accounts (email + password), job seekers browse without login
Data model: Employer(id, company_name, email, password_hash, logo_url)
            Job(id, employer_id -> Employer, title, description, salary_min, salary_max, timezone_range, apply_url, expires_at)
            Payment(id, job_id -> Job, amount_cents, paid_at)
Features:   - Post a job listing after paying a listing fee
            - Filter jobs by salary range and timezone
            - Expire listings automatically after 30 days
            - Send a weekly email digest of new jobs to subscribers
            - Show a featured badge for paid upgrades
API:        REST
            GET  /jobs
            GET  /jobs/{id}
            POST /jobs
            POST /jobs/{id}/feature
            POST /subscribers
Storage:    PostgreSQL
Tech stack: Rust, Axum, SQLx, Askama templates
```

---

## Example 7

**Intent:**
wiki for our company internal docs, something like confluence but way simpler

**Spec:**
```
Type:       Web application (wiki)
Auth:       Google Workspace SSO (OAuth 2.0), restricted to the company domain
Data model: User(id, name, email)
            Space(id, name, slug)
            Page(id, space_id -> Space, parent_id -> Page, title, body, updated_by -> User, updated_at)
            PageVersion(id, page_id -> Page, body, edited_by -> User, created_at)
Features:   - Create pages in a tree of spaces and sub-pages
            - Edit pages with a rich-text editor
            - Keep a full version history and restore old versions
            - Search all pages by full text
            - Link pages to each other with [[Page Title]] syntax
API:        REST
            GET  /spaces
            GET  /spaces/{slug}/pages
            GET  /pages/{id}
            PUT  /pages/{id}
            GET  /pages/{id}/versions
            GET  /search?q=
Storage:    PostgreSQL (full-text search)
Tech stack: TypeScript, NestJS, React, TipTap editor
```

---

## Example 8

**Intent:**
hey so i make pottery and want a portfolio site to show my work and let people email me about commissions

**Spec:**
```
Type:       Web application (portfolio)
Auth:       Single owner login for the admin panel
Data model: Piece(id, title, description, image_urls, year, is_available)
            Collection(id, name)
            Inquiry(id, name, email, message, piece_id -> Piece, created_at)
Features:   - Show pieces in a responsive image gallery
            - Group pieces into collections
            - Mark pieces as available or sold
            - Send commission inquiries through a contact form to the owner's email
            - Let the owner add and edit pieces from an admin page
API:        REST
            GET  /pieces
            GET  /collections/{id}
            POST /inquiries
            POST /admin/pieces
Storage:    SQLite, Cloudinary (images)
Tech stack: Astro, Node.js, Nodemailer
```

---

## Example 9

**Intent:**
newsletter platform like substack but only for my town's news

**Spec:**
```
Type:       Web application (newsletter platform)
Auth:       Email + password for writers, email-only subscriptions for readers
Data model: Writer(id, name, email, password_hash)
            Issue(id, writer_id -> Writer, subject, body_html, sent_at, status)
            Subscriber(id, email, confirmed, unsubscribe_token, created_at)
Features:   - Write and schedule newsletter issues
            - Collect subscribers with double opt-in
            - Send issues to all confirmed subscribers
            - Publish each issue as a public web page archive
            - Track opens and clicks per issue
API:        REST
            POST /subscribe
            GET  /confirm/{token}
            GET  /unsubscribe/{token}
            GET  /issues
            POST /issues
            POST /issues/{id}/send
Storage:    PostgreSQL
Tech stack: Python, Django, Celery, Amazon SES
```

---

## Example 10

**Intent:**
A site where people review local coffee shops.

**Spec:**
```
Type:       Web application (review site)
Auth:       Email + password registration
Data model: User(id, username, email, password_hash)
            Shop(id, name, address, lat, lng)
            Review(id, shop_id -> Shop, user_id -> User, rating, body, photo_url, created_at)
Features:   - Add a coffee shop with its address and location
            - Write a review with a 1-5 star rating and a photo
            - Show average rating per shop
            - Show shops on a map
            - Sort shops by rating or distance
API:        REST
            GET  /shops?near=lat,lng
            POST /shops
            GET  /shops/{id}/reviews
            POST /shops/{id}/reviews
Storage:    PostgreSQL with PostGIS
Tech stack: Node.js, Express, Vue.js, Leaflet
```

---

## Example 11

**Intent:**
crowdfunding site for school projects

**Spec:**
```
Type:       Web application (crowdfunding)
Auth:       Email + password registration for teachers, optional accounts for donors
Data model: Teacher(id, name, school, email, password_hash, verified)
            Project(id, teacher_id -> Teacher, title, description, goal_cents, raised_cents, deadline, status)
            Donation(id, project_id -> Project, donor_email, amount_cents, created_at)
Features:   - Create a project with a funding goal and deadline
            - Accept donations by card via Stripe
            - Show a progress bar of money raised
            - Verify teachers before projects go live
            - Post updates to donors when a project is funded
API:        REST
            GET  /projects
            POST /projects
            GET  /projects/{id}
            POST /projects/{id}/donations
            POST /projects/{id}/updates
Storage:    PostgreSQL
Tech stack: Laravel, MySQL, Stripe
```

---

## Example 12

**Intent:**
need a way to organise volunteers for our food bank shifts

**Spec:**
```
Type:       Web application (volunteer coordination)
Auth:       Email + password for volunteers, admin role for coordinators
Data model: Volunteer(id, name, email, phone, password_hash)
            Shift(id, role, starts_at, ends_at, slots)
            Assignment(id, shift_id -> Shift, volunteer_id -> Volunteer, status)
Features:   - Publish shifts with roles and number of slots
            - Let volunteers claim and drop shifts
            - Send SMS reminders before a shift
            - Track volunteer hours per person
            - Export hours to CSV for reports
API:        REST
            GET  /shifts
            POST /shifts
            POST /shifts/{id}/claim
            DELETE /shifts/{id}/claim
            GET  /volunteers/{id}/hours
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React, Twilio
```

---

## Example 13

**Intent:**
project management tool for my 5 person agency, kanban boards and time tracking

**Spec:**
```
Type:       Web application (project management)
Auth:       Email + password, workspace invites by email
Data model: User(id, name, email, password_hash)
            Project(id, name, client_name)
            Task(id, project_id -> Project, title, status, assignee_id -> User, due_date)
            TimeEntry(id, task_id -> Task, user_id -> User, minutes, date)
Features:   - Show tasks on a kanban board with drag and drop
            - Assign tasks and set due dates
            - Log time against tasks
            - Show hours per project and per person each week
            - Invite team members to the workspace
API:        REST
            GET  /projects
            GET  /projects/{id}/tasks
            POST /tasks
            PATCH /tasks/{id}
            POST /tasks/{id}/time
            GET  /reports/weekly
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, tRPC, Prisma
```

---

## Example 14

**Intent:**
AI tool that summarises long articles when you paste a link

**Spec:**
```
Type:       Web application (AI summariser)
Auth:       Email + password, free tier with daily limit
Data model: User(id, email, password_hash, plan)
            Summary(id, user_id -> User, url, title, summary_text, created_at)
Features:   - Fetch an article from a URL and extract the main text
            - Summarise it into key points with an LLM
            - Let users choose short, medium or detailed length
            - Save past summaries to the user's history
            - Limit free users to 5 summaries a day
API:        REST
            POST /summaries
            GET  /summaries
            GET  /summaries/{id}
            DELETE /summaries/{id}
Storage:    PostgreSQL, Redis (rate limits)
Tech stack: Python, FastAPI, trafilatura, OpenAI API, React
```

---

## Example 15

**Intent:**
marketplace for second hand textbooks between students at my uni

**Spec:**
```
Type:       Web application (marketplace)
Auth:       Registration restricted to university email addresses, email verification
Data model: Student(id, name, uni_email, password_hash)
            Listing(id, seller_id -> Student, isbn, title, course_code, condition, price, status)
            Message(id, listing_id -> Listing, sender_id -> Student, body, sent_at)
Features:   - List a textbook by ISBN with auto-filled title and cover
            - Search listings by course code or ISBN
            - Message the seller about a listing
            - Mark a listing as sold
            - Get an email alert when a wanted book is listed
API:        REST
            GET  /listings?course=&isbn=
            POST /listings
            PATCH /listings/{id}
            POST /listings/{id}/messages
            POST /alerts
Storage:    PostgreSQL
Tech stack: Python, Django, Open Library API
```

---

## Example 16

**Intent:**
i want my own social network for my family only, share photos and comment

**Spec:**
```
Type:       Web application (private social network)
Auth:       Invite-only registration, email + password
Data model: Member(id, name, email, password_hash, avatar_url)
            Post(id, author_id -> Member, caption, created_at)
            Photo(id, post_id -> Post, url)
            Comment(id, post_id -> Post, author_id -> Member, body, created_at)
            Invite(id, email, token, used)
Features:   - Invite family members by email link
            - Post photos with captions to a shared feed
            - Comment on and like posts
            - Show a calendar of family birthdays
            - Notify members by email about new posts
API:        REST
            POST /invites
            POST /register/{token}
            GET  /feed
            POST /posts
            POST /posts/{id}/comments
            POST /posts/{id}/like
Storage:    PostgreSQL, S3 (photos)
Tech stack: Node.js, Express, React, Multer
```

---

## Example 17

**Intent:**
Hello, I am teacher in Brazil and I want make website where my students can do quiz and I see the results of each one.

**Spec:**
```
Type:       Web application (online quiz platform)
Auth:       Teacher account with email + password, students log in with a class code and name
Data model: Teacher(id, name, email, password_hash)
            Class(id, teacher_id -> Teacher, name, join_code)
            Quiz(id, class_id -> Class, title, due_at)
            Question(id, quiz_id -> Quiz, text, options, correct_option)
            Attempt(id, quiz_id -> Quiz, student_name, score, submitted_at)
Features:   - Create quizzes with multiple-choice questions
            - Let students join a class with a code
            - Grade attempts automatically
            - Show the teacher each student's score per quiz
            - Export results to a spreadsheet
API:        REST
            POST /classes
            POST /classes/join
            POST /quizzes
            GET  /quizzes/{id}
            POST /quizzes/{id}/attempts
            GET  /quizzes/{id}/results
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Blade templates
```

---

## Example 18

**Intent:**
knowledge base for our customer support team using supabase

**Spec:**
```
Type:       Web application (knowledge base)
Auth:       Supabase Auth (email + password) for agents, public read access for customers
Data model: Category(id, name, slug)
            Article(id, category_id -> Category, title, body, is_published, updated_at)
            ArticleFeedback(id, article_id -> Article, helpful, comment, created_at)
Features:   - Write help articles grouped by category
            - Publish articles to a public help centre
            - Search articles with full-text search
            - Collect "was this helpful?" votes
            - Show agents the least helpful articles to improve
API:        REST (Supabase auto-generated)
            GET  /rest/v1/articles
            POST /rest/v1/articles
            PATCH /rest/v1/articles?id=eq.{id}
            POST /rest/v1/article_feedback
Storage:    Supabase (PostgreSQL)
Tech stack: Supabase, Next.js, Tailwind CSS
```

---

## Example 19

**Intent:**
site for sharing sewing patterns

**Spec:**
```
Type:       Web application (community content sharing)
Auth:       Email + password registration
Data model: User(id, username, email, password_hash)
            Pattern(id, author_id -> User, title, difficulty, garment_type, pdf_url, preview_url)
            Favourite(user_id -> User, pattern_id -> Pattern)
            Comment(id, pattern_id -> Pattern, user_id -> User, body)
Features:   - Upload patterns as PDF with a preview image
            - Filter patterns by garment type and difficulty
            - Save patterns to favourites
            - Comment on patterns and share finished makes
API:        REST
            GET  /patterns
            POST /patterns
            GET  /patterns/{id}
            POST /patterns/{id}/favourite
            POST /patterns/{id}/comments
Storage:    PostgreSQL, S3 (PDFs and images)
Tech stack: Python, Django, Bootstrap
```

---

## Example 20

**Intent:**
multi tenant saas for gyms to manage memberships, each gym gets its own subdomain

**Spec:**
```
Type:       Web application (multi-tenant SaaS)
Auth:       Email + password per tenant, roles: owner, staff, member
Data model: Tenant(id, name, subdomain, plan)
            User(id, tenant_id -> Tenant, email, password_hash, role)
            Membership(id, tenant_id -> Tenant, user_id -> User, plan_name, starts_at, ends_at, status)
            CheckIn(id, tenant_id -> Tenant, user_id -> User, checked_in_at)
Features:   - Resolve the tenant from the request subdomain
            - Isolate every query by tenant_id
            - Manage membership plans and renewals
            - Record member check-ins at the front desk
            - Bill each gym monthly through Stripe subscriptions
API:        REST
            POST /tenants
            GET  /members
            POST /members
            GET  /memberships
            POST /checkins
            POST /webhooks/stripe
Storage:    PostgreSQL with row-level security
Tech stack: Ruby on Rails, acts_as_tenant gem, Stripe
```

---

## Example 21

**Intent:**
writing assistant that fixes grammar and makes my emails sound more professional

**Spec:**
```
Type:       Web application (AI writing assistant)
Auth:       Google sign-in (OAuth 2.0)
Data model: User(id, email, name)
            Rewrite(id, user_id -> User, original_text, rewritten_text, tone, created_at)
Features:   - Paste text and get grammar and spelling fixes
            - Rewrite text in a chosen tone (professional, friendly, short)
            - Show the changes highlighted side by side
            - Copy the result with one click
            - Keep a history of recent rewrites
API:        REST
            POST /rewrite
            GET  /history
            DELETE /history/{id}
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Anthropic Claude API
```

---

## Example 22

**Intent:**
ok so me and my friends play a lot of board games and we always argue about who wins the most. i want a site where our group logs every game we play, who won, scores etc and then shows a leaderboard and maybe stats like who is best at catan

**Spec:**
```
Type:       Web application (game tracking community)
Auth:       Group invite link, email + password login
Data model: Player(id, name, email, password_hash)
            Group(id, name, invite_code)
            Game(id, name, bgg_id)
            Play(id, group_id -> Group, game_id -> Game, played_at)
            PlayResult(id, play_id -> Play, player_id -> Player, score, is_winner)
Features:   - Log a play with the game, players, scores and winner
            - Show a group leaderboard of total wins
            - Show win rate per player for each game
            - Look up games from BoardGameGeek
            - Show a history of all plays
API:        REST
            POST /groups
            POST /groups/join/{code}
            POST /plays
            GET  /groups/{id}/leaderboard
            GET  /games/{id}/stats
Storage:    PostgreSQL
Tech stack: SvelteKit, Drizzle ORM, BoardGameGeek XML API
```

---

## Example 23

**Intent:**
freelance marketplace for translators

**Spec:**
```
Type:       Web application (freelance marketplace)
Auth:       Email + password, roles: client and translator
Data model: User(id, email, password_hash, role, name)
            TranslatorProfile(user_id -> User, language_pairs, rate_per_word, rating)
            Job(id, client_id -> User, source_lang, target_lang, word_count, deadline, status)
            Bid(id, job_id -> Job, translator_id -> User, price, message)
            Review(id, job_id -> Job, rating, comment)
Features:   - Post translation jobs with language pair and deadline
            - Let translators bid on jobs
            - Accept a bid and hold payment in escrow
            - Upload the finished file and release payment
            - Rate the translator after delivery
API:        REST
            GET  /jobs
            POST /jobs
            POST /jobs/{id}/bids
            POST /bids/{id}/accept
            POST /jobs/{id}/deliver
            POST /jobs/{id}/review
Storage:    PostgreSQL, S3 (files)
Tech stack: Python, Django REST Framework, React, Stripe Connect
```

---

## Example 24

**Intent:**
recipe blog with comments

**Spec:**
```
Type:       Web application (blog)
Auth:       Admin login for the author, commenters log in with Google
Data model: Recipe(id, title, slug, intro, ingredients, steps, prep_minutes, image_url, published_at)
            Comment(id, recipe_id -> Recipe, user_name, user_email, body, approved, created_at)
Features:   - Publish recipes with ingredients, steps and photos
            - Add a "jump to recipe" button and printable view
            - Let readers post comments
            - Approve comments before they show
            - Add Recipe structured data for Google search
API:        REST
            GET  /recipes
            GET  /recipes/{slug}
            POST /recipes/{id}/comments
            PATCH /admin/comments/{id}
Storage:    SQLite
Tech stack: Go, Gin, html/template
```

---

## Example 25

**Intent:**
platform where neighbours can lend each other tools

**Spec:**
```
Type:       Web application (sharing marketplace)
Auth:       Email + password with address verification
Data model: Neighbour(id, name, email, password_hash, postcode)
            Tool(id, owner_id -> Neighbour, name, category, photo_url, available)
            Loan(id, tool_id -> Tool, borrower_id -> Neighbour, start_date, end_date, status)
Features:   - List tools available to borrow
            - Search tools near your postcode
            - Request to borrow for set dates
            - Approve or decline borrow requests
            - Remind borrowers when a tool is due back
API:        REST
            GET  /tools?postcode=
            POST /tools
            POST /tools/{id}/loans
            PATCH /loans/{id}
            GET  /loans
Storage:    PostgreSQL
Tech stack: Node.js, Fastify, React
```

---

## Example 26

**Intent:**
Q&A site like stack overflow but for gardening questions

**Spec:**
```
Type:       Web application (Q&A community)
Auth:       Email + password registration
Data model: User(id, username, email, password_hash, reputation)
            Question(id, author_id -> User, title, body, tags, accepted_answer_id -> Answer, created_at)
            Answer(id, question_id -> Question, author_id -> User, body, created_at)
            Vote(user_id -> User, target_type, target_id, value)
Features:   - Ask questions with tags like vegetables or pests
            - Answer questions and vote answers up or down
            - Accept the best answer
            - Award reputation points for upvotes and accepted answers
            - Search questions by keyword and tag
API:        REST
            GET  /questions
            POST /questions
            GET  /questions/{id}
            POST /questions/{id}/answers
            POST /votes
            POST /questions/{id}/accept
Storage:    PostgreSQL
Tech stack: Python, Django, PostgreSQL full-text search
```

---

## Example 27

**Intent:**
team retro board

**Spec:**
```
Type:       Web application (collaboration tool)
Auth:       Anonymous participants join with a board link, facilitator signs in with email
Data model: Board(id, title, facilitator_email, created_at)
            Column(id, board_id -> Board, name)
            Card(id, column_id -> Column, text, votes)
Features:   - Create a retro board with columns like Went well, To improve, Actions
            - Add cards in real time
            - Vote on cards
            - Hide cards until the facilitator reveals them
            - Export action items as Markdown
API:        REST and WebSocket
            POST /boards
            GET  /boards/{id}
            POST /boards/{id}/cards
            WS   /boards/{id}/live
Storage:    Redis (live boards), PostgreSQL
Tech stack: Node.js, Socket.IO, React
```

---

## Example 28

**Intent:**
website for my book club, we vote on the next book and discuss chapters

**Spec:**
```
Type:       Web application (community club)
Auth:       Email + password, members invited by the organiser
Data model: Member(id, name, email, password_hash)
            Book(id, title, author, cover_url)
            Poll(id, closes_at)
            PollOption(id, poll_id -> Poll, book_id -> Book)
            Vote(poll_id -> Poll, member_id -> Member, option_id -> PollOption)
            Discussion(id, book_id -> Book, chapter, member_id -> Member, body)
Features:   - Suggest books for the next pick
            - Run a vote and show the winner when it closes
            - Discuss each chapter in its own thread
            - Hide spoilers behind a click
            - Show the meeting date and place
API:        REST
            GET  /books
            POST /books
            POST /polls
            POST /polls/{id}/vote
            GET  /books/{id}/discussions
            POST /books/{id}/discussions
Storage:    SQLite
Tech stack: Python, Flask, Alpine.js
```

---

## Example 29

**Intent:**
subscription site for my yoga videos, people pay monthly to watch

**Spec:**
```
Type:       Web application (membership video site)
Auth:       Email + password, Stripe subscription status controls access
Data model: Member(id, email, password_hash, stripe_customer_id, subscription_status)
            Video(id, title, description, level, duration_minutes, video_url)
            WatchHistory(member_id -> Member, video_id -> Video, watched_at)
Features:   - Sell a monthly subscription with Stripe Billing
            - Lock videos to active subscribers
            - Filter videos by level and duration
            - Resume videos where the member stopped
            - Let members cancel from their account page
API:        REST
            POST /checkout
            POST /webhooks/stripe
            GET  /videos
            GET  /videos/{id}/stream
            GET  /account
Storage:    PostgreSQL, Vimeo (private video hosting)
Tech stack: Ruby on Rails, Stripe Billing, Vimeo API
```

---

## Example 30

**Intent:**
changelog page for my saas

**Spec:**
```
Type:       Web application (changelog)
Auth:       Admin login for the product team
Data model: Entry(id, title, body_markdown, category, published_at)
            Subscriber(id, email, created_at)
Features:   - Publish changelog entries tagged New, Improved or Fixed
            - Show entries newest first on a public page
            - Let users subscribe to email updates
            - Show an in-app "what's new" widget via a small script tag
API:        REST
            GET  /entries
            POST /admin/entries
            POST /subscribe
            GET  /widget.js
Storage:    PostgreSQL
Tech stack: Node.js, Hono, Preact
```

---

## Example 31

**Intent:**
i want to start a local marketplace for homemade food, cooks sell meals and people nearby order and pick up

**Spec:**
```
Type:       Web application (food marketplace)
Auth:       Email + password, roles: cook and customer, cooks must be approved
Data model: User(id, name, email, password_hash, role, postcode)
            Meal(id, cook_id -> User, name, description, price, portions_available, pickup_date)
            Order(id, meal_id -> Meal, customer_id -> User, quantity, status, paid_at)
Features:   - Let cooks list meals with portions and pickup time
            - Show meals available near the customer
            - Pay for orders online with Stripe
            - Reduce available portions on each order
            - Notify the cook of new orders by email
API:        REST
            GET  /meals?postcode=
            POST /meals
            POST /meals/{id}/orders
            PATCH /orders/{id}
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js, Stripe
```

---

## Example 32

**Intent:**
forum with reddit style upvotes for my university

**Spec:**
```
Type:       Web application (forum)
Auth:       University email verification, email + password
Data model: User(id, username, uni_email, password_hash, karma)
            Community(id, name, description)
            Post(id, community_id -> Community, author_id -> User, title, body, score, created_at)
            Comment(id, post_id -> Post, parent_id -> Comment, author_id -> User, body, score)
            Vote(user_id -> User, target_id, value)
Features:   - Create communities for courses and clubs
            - Post links and text posts
            - Upvote and downvote posts and comments
            - Sort by hot, new and top
            - Show nested comment threads
API:        REST
            GET  /c/{name}/posts?sort=
            POST /posts
            GET  /posts/{id}
            POST /posts/{id}/comments
            POST /votes
Storage:    PostgreSQL, Redis (ranking cache)
Tech stack: Go, Chi router, React
```

---

## Example 33

**Intent:**
help desk ticket system for small business saas, with email in

**Spec:**
```
Type:       Web application (help desk SaaS)
Auth:       Email + password for agents, customers identified by email
Data model: Workspace(id, name, inbound_address)
            Agent(id, workspace_id -> Workspace, email, password_hash)
            Ticket(id, workspace_id -> Workspace, customer_email, subject, status, assignee_id -> Agent)
            TicketMessage(id, ticket_id -> Ticket, from_email, body, created_at)
Features:   - Create tickets from emails sent to the support address
            - Reply to customers from the web app
            - Assign tickets and set status open, pending or solved
            - Use saved reply templates
            - Show response time stats
API:        REST
            POST /inbound/email
            GET  /tickets
            GET  /tickets/{id}
            POST /tickets/{id}/reply
            PATCH /tickets/{id}
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix LiveView, Postmark inbound webhooks
```

---

## Example 34

**Intent:**
dnd campaign wiki for my players

**Spec:**
```
Type:       Web application (wiki)
Auth:       Dungeon master account, players join with an invite link
Data model: Campaign(id, name, dm_id -> User)
            User(id, name, email, password_hash)
            Page(id, campaign_id -> Campaign, title, category, body, dm_only)
            SessionLog(id, campaign_id -> Campaign, session_number, summary, played_on)
Features:   - Write pages for NPCs, places and items
            - Hide DM-only pages from players
            - Auto-link page names mentioned in other pages
            - Post a recap after each session
            - Search the whole campaign
API:        REST
            GET  /campaigns/{id}/pages
            POST /pages
            PUT  /pages/{id}
            POST /campaigns/{id}/sessions
            GET  /campaigns/{id}/search?q=
Storage:    SQLite
Tech stack: Python, Flask, Markdown
```

---

## Example 35

**Intent:**
we are small NGO, need platform where donors can see how money is spent on each project, very transparent

**Spec:**
```
Type:       Web application (donation transparency)
Auth:       Admin login for staff, donors create optional accounts
Data model: Project(id, name, description, budget_cents)
            Donation(id, project_id -> Project, donor_id -> Donor, amount_cents, created_at)
            Donor(id, name, email)
            Expense(id, project_id -> Project, description, amount_cents, receipt_url, spent_on)
Features:   - Show each project with its budget, money received and money spent
            - Publish expenses with receipt photos
            - Accept donations to a specific project
            - Show donors where their own donations went
            - Publish a yearly report page
API:        REST
            GET  /projects
            GET  /projects/{id}/expenses
            POST /projects/{id}/donations
            POST /admin/expenses
            GET  /me/donations
Storage:    PostgreSQL, S3 (receipts)
Tech stack: PHP, Symfony, Twig, Stripe
```

---

## Example 36

**Intent:**
link in bio page builder

**Spec:**
```
Type:       Web application (link-in-bio SaaS)
Auth:       Email + password or Google sign-in
Data model: User(id, email, username, password_hash)
            Page(id, user_id -> User, theme, bio, avatar_url)
            Link(id, page_id -> Page, title, url, position, clicks)
Features:   - Build a public page at /username with a list of links
            - Reorder links by drag and drop
            - Pick a theme and colours
            - Count clicks on each link
            - Show a simple weekly click chart
API:        REST
            GET  /{username}
            GET  /api/links
            POST /api/links
            PATCH /api/links/{id}
            GET  /r/{link_id}
Storage:    PostgreSQL
Tech stack: Next.js, Prisma, Vercel
```

---

## Example 37

**Intent:**
An online course site for teaching kids to code, with little coding exercises that check the answer automatically.

**Spec:**
```
Type:       Web application (education platform)
Auth:       Parent account with email + password, child profiles under it
Data model: Parent(id, email, password_hash)
            Child(id, parent_id -> Parent, nickname, age)
            Lesson(id, title, instructions, starter_code, test_code, order)
            Submission(id, child_id -> Child, lesson_id -> Lesson, code, passed, submitted_at)
Features:   - Show lessons with an in-browser code editor
            - Run the child's code against hidden tests in a sandbox
            - Award badges for completed lessons
            - Show parents a progress report
            - Unlock the next lesson when the current one passes
API:        REST
            GET  /lessons
            GET  /lessons/{id}
            POST /lessons/{id}/submissions
            GET  /children/{id}/progress
Storage:    PostgreSQL
Tech stack: TypeScript, React, Monaco Editor, Node.js, Pyodide
```

---

## Example 38

**Intent:**
photographers sell prints marketplace

**Spec:**
```
Type:       Web application (marketplace)
Auth:       Email + password, roles: photographer and buyer
Data model: Photographer(id, name, email, password_hash, stripe_account_id)
            Photo(id, photographer_id -> Photographer, title, image_url, tags)
            PrintOption(id, photo_id -> Photo, size, paper, price)
            Order(id, buyer_email, print_option_id -> PrintOption, status, created_at)
Features:   - Upload photos with watermarked previews
            - Set print sizes and prices
            - Sell prints and split payment with the platform
            - Send orders to a print-on-demand partner
            - Show photographers their earnings
API:        REST
            GET  /photos
            POST /photos
            POST /photos/{id}/options
            POST /orders
            GET  /me/earnings
Storage:    PostgreSQL, S3 (originals)
Tech stack: Python, Django, Stripe Connect, Prodigi API
```

---

## Example 39

**Intent:**
shared grocery list website for my flatmates

**Spec:**
```
Type:       Web application (collaboration tool)
Auth:       Shared household with invite code, simple email login
Data model: Household(id, name, invite_code)
            Member(id, household_id -> Household, name, email)
            Item(id, household_id -> Household, name, quantity, added_by -> Member, bought)
Features:   - Add items to a shared list
            - Tick off items when bought
            - Sync the list live for everyone
            - Split the receipt total between flatmates
API:        REST
            POST /households
            POST /households/join
            GET  /items
            POST /items
            PATCH /items/{id}
Storage:    Firebase Firestore
Tech stack: React, Firebase
```

---

## Example 40

**Intent:**
event listing site for my city where anyone can submit events and admins approve them

**Spec:**
```
Type:       Web application (community events directory)
Auth:       Email + password for submitters, admin role for approvers
Data model: User(id, email, password_hash, role)
            Event(id, submitter_id -> User, title, description, venue, starts_at, category, status, image_url)
Features:   - Submit events with date, venue and category
            - Approve or reject events in an admin queue
            - Browse upcoming events by date and category
            - Export events to Google Calendar via iCal
            - Email submitters when their event is approved
API:        REST
            GET  /events?from=&category=
            POST /events
            PATCH /admin/events/{id}
            GET  /events/{id}.ics
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 41

**Intent:**
invoice saas for freelancers

**Spec:**
```
Type:       Web application (SaaS)
Auth:       Email + password, Stripe subscription for paid plan
Data model: User(id, email, password_hash, business_name, plan)
            Client(id, user_id -> User, name, email, address)
            Invoice(id, user_id -> User, client_id -> Client, number, issue_date, due_date, status, total_cents)
            InvoiceLine(id, invoice_id -> Invoice, description, quantity, unit_price_cents)
Features:   - Create invoices with line items and tax
            - Generate PDF invoices
            - Email invoices to clients with a pay link
            - Mark invoices paid and track overdue ones
            - Limit the free plan to 3 clients
API:        REST
            GET  /invoices
            POST /invoices
            GET  /invoices/{id}/pdf
            POST /invoices/{id}/send
            GET  /clients
            POST /clients
Storage:    PostgreSQL
Tech stack: Laravel, Vue.js, Stripe, dompdf
```

---

## Example 42

**Intent:**
Something where my students can write short stories and other students give them feedback, but anonymously so nobody is mean or shy

**Spec:**
```
Type:       Web application (peer review platform)
Auth:       Teacher creates class and gives students login codes
Data model: Teacher(id, email, password_hash)
            Student(id, class_id -> Class, display_code)
            Class(id, teacher_id -> Teacher, name)
            Story(id, student_id -> Student, title, body, submitted_at)
            Feedback(id, story_id -> Story, reviewer_id -> Student, strengths, suggestions, flagged)
Features:   - Submit stories to the class
            - Assign each story to 2 random classmates for review
            - Hide author and reviewer names from students
            - Let students flag unkind feedback
            - Show the teacher all names and feedback
API:        REST
            POST /stories
            GET  /reviews/assigned
            POST /stories/{id}/feedback
            POST /feedback/{id}/flag
            GET  /teacher/classes/{id}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Svelte
```

---

## Example 43

**Intent:**
pls make a site where ppl can rate their landlords

**Spec:**
```
Type:       Web application (review site)
Auth:       Email + password, reviews shown anonymously
Data model: User(id, email, password_hash)
            Landlord(id, name, company)
            Property(id, landlord_id -> Landlord, address, city)
            Review(id, property_id -> Property, user_id -> User, rating, repairs_rating, deposit_returned, body, created_at)
Features:   - Search by address or landlord name
            - Write reviews with ratings for repairs and communication
            - Show average scores per landlord
            - Report reviews for moderation
            - Hide reviewer identity from the public
API:        REST
            GET  /search?q=
            GET  /landlords/{id}
            POST /properties/{id}/reviews
            POST /reviews/{id}/report
Storage:    PostgreSQL
Tech stack: Node.js, Express, EJS
```

---

## Example 44

**Intent:**
newsletter signup page plus archive, using ghost

**Spec:**
```
Type:       Web application (newsletter site)
Auth:       Ghost member sign-in (magic link)
Data model: Member(id, email, name, status)
            Post(id, title, html, published_at, visibility)
Features:   - Collect newsletter sign-ups on a landing page
            - Send each post as an email newsletter
            - Show past issues in a public archive
            - Offer a paid tier with members-only posts
API:        REST (Ghost Content API)
            GET  /ghost/api/content/posts/
            GET  /ghost/api/content/posts/slug/{slug}/
Storage:    MySQL (Ghost database)
Tech stack: Ghost, Handlebars theme, Mailgun, Stripe
```

---

## Example 45

**Intent:**
website for coding bootcamp, students submit assignments and mentors review code

**Spec:**
```
Type:       Web application (education platform)
Auth:       Email + password, roles: student, mentor, admin
Data model: User(id, name, email, password_hash, role)
            Cohort(id, name, start_date)
            Assignment(id, cohort_id -> Cohort, title, brief, due_at)
            Submission(id, assignment_id -> Assignment, student_id -> User, repo_url, status)
            Review(id, submission_id -> Submission, mentor_id -> User, comments, grade)
Features:   - Publish weekly assignments to a cohort
            - Submit a GitHub repository link
            - Assign submissions to mentors
            - Leave review comments and a pass/fail grade
            - Show each student their progress over the course
API:        REST
            GET  /assignments
            POST /assignments/{id}/submissions
            GET  /mentor/queue
            POST /submissions/{id}/review
Storage:    PostgreSQL
Tech stack: Ruby on Rails, GitHub API
```

---

## Example 46

**Intent:**
crowdfunding for indie board games with reward tiers

**Spec:**
```
Type:       Web application (crowdfunding)
Auth:       Email + password registration
Data model: Creator(id, name, email, password_hash)
            Campaign(id, creator_id -> Creator, title, story, goal_cents, ends_at, status)
            RewardTier(id, campaign_id -> Campaign, title, price_cents, limit, shipping_regions)
            Pledge(id, tier_id -> RewardTier, backer_email, amount_cents, payment_intent_id, status)
Features:   - Create a campaign with reward tiers
            - Authorise card payments and only charge if the goal is reached
            - Show funding progress and backer count
            - Post updates to backers
            - Export backer addresses for shipping
API:        REST
            GET  /campaigns
            POST /campaigns
            POST /campaigns/{id}/tiers
            POST /tiers/{id}/pledges
            GET  /campaigns/{id}/backers.csv
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe (manual capture)
```

---

## Example 47

**Intent:**
collaborative whiteboard in the browser for remote teams

**Spec:**
```
Type:       Web application (collaboration tool)
Auth:       Email + password or Google sign-in, share boards by link
Data model: User(id, email, name)
            Board(id, owner_id -> User, title, share_token)
            BoardMember(board_id -> Board, user_id -> User, role)
Features:   - Draw shapes, sticky notes and arrows on an infinite canvas
            - Sync edits live between all users
            - Show other users' cursors
            - Share boards with view or edit rights
            - Export the board as PNG
API:        REST and WebSocket
            POST /boards
            GET  /boards/{id}
            POST /boards/{id}/share
            WS   /boards/{id}/sync
Storage:    PostgreSQL, Yjs document snapshots in S3
Tech stack: TypeScript, React, Yjs, y-websocket, Node.js
```

---

## Example 48

**Intent:**
site for people to swap plants and cuttings

**Spec:**
```
Type:       Web application (swap marketplace)
Auth:       Email + password
Data model: User(id, username, email, password_hash, city)
            Offer(id, user_id -> User, plant_name, type, photo_url, wants, status)
            SwapRequest(id, offer_id -> Offer, requester_id -> User, message, status)
Features:   - Post plants or cuttings to swap
            - Say what you want in return
            - Request a swap and chat about it
            - Filter offers by city
            - Mark swaps as completed
API:        REST
            GET  /offers?city=
            POST /offers
            POST /offers/{id}/requests
            PATCH /requests/{id}
Storage:    SQLite
Tech stack: Python, Flask, Bootstrap
```

---

## Example 49

**Intent:**
build me a hacker news clone in elixir

**Spec:**
```
Type:       Web application (link aggregator)
Auth:       Username + password registration
Data model: User(id, username, password_hash, karma)
            Story(id, user_id -> User, title, url, points, created_at)
            Comment(id, story_id -> Story, parent_id -> Comment, user_id -> User, text)
            Upvote(user_id -> User, item_id)
Features:   - Submit links and Ask posts
            - Upvote stories and comments
            - Rank the front page by points and age
            - Show threaded comments
            - Show user profiles with karma
API:        REST
            GET  /news
            GET  /newest
            POST /submit
            GET  /item/{id}
            POST /vote/{id}
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix, Ecto
```

---

## Example 50

**Intent:**
An AI chatbot on our docs site that answers questions using our documentation.

**Spec:**
```
Type:       Web application (AI documentation assistant)
Data model: DocChunk(id, source_url, heading, content, embedding)
            Conversation(id, created_at)
            ChatMessage(id, conversation_id -> Conversation, role, content, sources)
Features:   - Crawl the docs site and split pages into chunks
            - Store embeddings for each chunk
            - Answer questions using the most relevant chunks
            - Show links to the source pages under each answer
            - Let users rate answers with thumbs up or down
API:        REST
            POST /chat
            POST /chat/{id}/feedback
            POST /admin/reindex
Storage:    PostgreSQL with pgvector
Tech stack: Python, FastAPI, OpenAI embeddings, React widget
```

---

## Example 51

**Intent:**
portfolio site for a ux designer with case studies

**Spec:**
```
Type:       Web application (portfolio)
Data model: CaseStudy(id, title, slug, client, role, summary, body_mdx, cover_url, order)
Features:   - Show case studies as cards on the home page
            - Render long-form case studies with images
            - Add a password-protected case study for NDA work
            - Include an about page and downloadable CV
Storage:    Markdown/MDX files in the repo
Tech stack: Next.js, MDX, Tailwind CSS, Vercel
```

---

## Example 52

**Intent:**
membership site for our hiking club with trips, payments and a members only area

**Spec:**
```
Type:       Web application (club membership)
Auth:       Email + password, member status based on paid dues
Data model: Member(id, name, email, password_hash, dues_paid_until)
            Trip(id, title, date, difficulty, max_people, price)
            Booking(id, trip_id -> Trip, member_id -> Member, paid)
            Document(id, title, file_url)
Features:   - Pay yearly membership dues online
            - Book a place on upcoming trips
            - Restrict club documents to paid members
            - Email members when dues are about to expire
            - Show trip leaders a participant list
API:        REST
            POST /dues/checkout
            GET  /trips
            POST /trips/{id}/bookings
            GET  /documents
Storage:    PostgreSQL
Tech stack: WordPress, MemberPress, Stripe
```

---

## Example 53

**Intent:**
kanban for one person

**Spec:**
```
Type:       Web application (task board)
Data model: Column(id, name, position)
            Card(id, column_id -> Column, title, notes, due_date, position)
Features:   - Add columns and cards
            - Drag cards between columns
            - Add notes and due dates to cards
            - Highlight overdue cards
Storage:    Browser localStorage
Tech stack: HTML, CSS, JavaScript, SortableJS
```

---

## Example 54

**Intent:**
reviews site for online courses so people know which udemy courses are actually good

**Spec:**
```
Type:       Web application (review site)
Auth:       Email + password or GitHub sign-in
Data model: User(id, username, email)
            Course(id, title, provider, url, topic, price)
            Review(id, course_id -> Course, user_id -> User, rating, completed, pros, cons, created_at)
            HelpfulVote(review_id -> Review, user_id -> User)
Features:   - Add courses from Udemy, Coursera and others
            - Write reviews with pros and cons
            - Mark whether the reviewer finished the course
            - Vote reviews as helpful
            - Rank courses by topic and rating
API:        REST
            GET  /courses?topic=
            POST /courses
            GET  /courses/{id}/reviews
            POST /courses/{id}/reviews
            POST /reviews/{id}/helpful
Storage:    PostgreSQL
Tech stack: Python, Django, React
```

---

## Example 55

**Intent:**
fundraising page for my marathon run, people sponsor me per km

**Spec:**
```
Type:       Web application (fundraising)
Auth:       Owner login only
Data model: Sponsor(id, name, email, amount_per_km_cents, max_cents, message)
            RunResult(id, distance_km, recorded_at)
Features:   - Let people pledge an amount per kilometre with an optional cap
            - Show total pledged so far
            - Enter the final distance after the race
            - Calculate what each sponsor owes and email them a payment link
API:        REST
            GET  /pledges
            POST /pledges
            POST /admin/result
            POST /admin/send-invoices
Storage:    SQLite
Tech stack: Python, Flask, Stripe Payment Links
```

---

## Example 56

**Intent:**
community platform for parents in my area to ask questions and share tips, with groups for things like school, babysitting, playdates

**Spec:**
```
Type:       Web application (community platform)
Auth:       Email + password, address postcode check on signup
Data model: Parent(id, name, email, password_hash, postcode)
            Group(id, name, description)
            GroupMember(group_id -> Group, parent_id -> Parent)
            Post(id, group_id -> Group, author_id -> Parent, body, created_at)
            Reply(id, post_id -> Post, author_id -> Parent, body)
Features:   - Join topic groups like School, Babysitting and Playdates
            - Post questions and tips in groups
            - Reply to posts and get notified of replies
            - Report posts to moderators
            - Show a feed of posts from joined groups
API:        REST
            GET  /groups
            POST /groups/{id}/join
            GET  /feed
            POST /groups/{id}/posts
            POST /posts/{id}/replies
            POST /posts/{id}/report
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, Next.js
```

---

## Example 57

**Intent:**
forum for vegan recipes

**Spec:**
```
Type:       Web application (forum)
Auth:       Email + password registration
Data model: User(id, username, email, password_hash)
            Category(id, name)
            Topic(id, category_id -> Category, author_id -> User, title, created_at)
            Reply(id, topic_id -> Topic, author_id -> User, body, created_at)
Features:   - Start topics in categories like Baking, Meal Prep and Substitutes
            - Reply with text and recipe photos
            - Like replies
            - Follow topics and get email notifications
API:        REST
            GET  /categories
            GET  /categories/{id}/topics
            POST /topics
            POST /topics/{id}/replies
            POST /replies/{id}/like
Storage:    PostgreSQL
Tech stack: Discourse (self-hosted, Docker)
```

---

## Example 58

**Intent:**
marketplace for used camera gear

**Spec:**
```
Type:       Web application (marketplace)
Auth:       Email + password, phone number verification for sellers
Data model: User(id, name, email, password_hash, phone_verified, rating)
            Listing(id, seller_id -> User, brand, model, category, condition, price, shutter_count, status)
            Offer(id, listing_id -> Listing, buyer_id -> User, amount, status)
            Review(id, seller_id -> User, buyer_id -> User, rating, comment)
Features:   - List gear with brand, model, condition and shutter count
            - Make and accept price offers
            - Pay through the platform with buyer protection
            - Rate the seller after delivery
            - Filter listings by brand, mount and price
API:        REST
            GET  /listings
            POST /listings
            POST /listings/{id}/offers
            PATCH /offers/{id}
            POST /sellers/{id}/reviews
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, Stripe Connect
```

---

## Example 59

**Intent:**
wiki

**Spec:**
```
Type:       Web application (wiki)
Auth:       Email + password, anonymous read access
Data model: User(id, username, email, password_hash)
            Page(id, title, slug, body_markdown, updated_at)
            Revision(id, page_id -> Page, author_id -> User, body_markdown, summary, created_at)
Features:   - Create and edit pages in Markdown
            - Link pages with [[wiki links]]
            - Show the revision history and diff two revisions
            - Search pages by title and content
API:        REST
            GET  /wiki/{slug}
            PUT  /wiki/{slug}
            GET  /wiki/{slug}/history
            GET  /search?q=
Storage:    SQLite
Tech stack: Go, net/http, goldmark
```

---

## Example 60

**Intent:**
i teach guitar online and want a site where students book lessons, pay, and i send them sheet music after

**Spec:**
```
Type:       Web application (lesson booking and resources)
Auth:       Email + password for students, admin login for the teacher
Data model: Student(id, name, email, password_hash, level)
            Slot(id, starts_at, duration_minutes, is_booked)
            Booking(id, slot_id -> Slot, student_id -> Student, paid, zoom_link)
            Resource(id, title, file_url)
            SharedResource(resource_id -> Resource, student_id -> Student, shared_at)
Features:   - Show free lesson slots in the student's time zone
            - Book and pay for a lesson with Stripe
            - Create a Zoom link for each booking
            - Share PDFs of sheet music with a student after the lesson
            - Send reminder emails 24 hours before
API:        REST
            GET  /slots
            POST /slots/{id}/book
            POST /webhooks/stripe
            POST /resources
            POST /resources/{id}/share
Storage:    PostgreSQL, S3 (PDFs)
Tech stack: Node.js, Express, React, Stripe, Zoom API
```

---

## Example 61

**Intent:**
plz help i need website for my church, events, sermons videos and donations

**Spec:**
```
Type:       Web application (community site)
Auth:       Admin login for church staff
Data model: Event(id, title, starts_at, location, description)
            Sermon(id, title, speaker, preached_on, video_url, notes)
            Donation(id, donor_email, amount_cents, fund, recurring, created_at)
Features:   - Show upcoming events on a calendar
            - Publish sermon videos with notes
            - Accept one-time and monthly donations
            - Let donors choose a fund like Missions or Building
            - Email a yearly giving statement to donors
API:        REST
            GET  /events
            GET  /sermons
            POST /donations
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: WordPress, The Events Calendar plugin, Stripe, YouTube embeds
```

---

## Example 62

**Intent:**
tool that turns my meeting notes into a summary with action items, on the web

**Spec:**
```
Type:       Web application (AI summariser)
Auth:       Email + password
Data model: User(id, email, password_hash)
            Note(id, user_id -> User, title, raw_text, summary, created_at)
            ActionItem(id, note_id -> Note, text, owner_name, due_date, done)
Features:   - Paste or upload meeting notes
            - Generate a short summary with an LLM
            - Extract action items with owner and due date
            - Tick off action items
            - Copy the summary as Markdown for Slack
API:        REST
            POST /notes
            GET  /notes/{id}
            GET  /action-items
            PATCH /action-items/{id}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Anthropic Claude API, Vue.js
```

---

## Example 63

**Intent:**
I'd like a platform where retired people can offer to teach skills like knitting or woodworking to younger people in the neighbourhood, and they can arrange meetups. My grandma suggested it actually.

**Spec:**
```
Type:       Web application (skill sharing community)
Auth:       Email + password with simple large-text sign-up form
Data model: Member(id, name, email, password_hash, birth_year, neighbourhood)
            Skill(id, teacher_id -> Member, title, description, category)
            Meetup(id, skill_id -> Skill, location, starts_at, max_learners)
            Attendance(meetup_id -> Meetup, learner_id -> Member)
Features:   - Offer a skill with a description and category
            - Schedule meetups at a place and time
            - Let learners join meetups
            - Show skills in the member's neighbourhood
            - Use large fonts and simple navigation for older users
API:        REST
            GET  /skills?neighbourhood=
            POST /skills
            POST /skills/{id}/meetups
            POST /meetups/{id}/join
Storage:    PostgreSQL
Tech stack: Python, Django, server-rendered templates
```

---

## Example 64

**Intent:**
whats the best way to make a job board for nurses, hospitals post shifts and nurses apply

**Spec:**
```
Type:       Web application (job board)
Auth:       Email + password, roles: hospital and nurse, nurse licence check by admin
Data model: Hospital(id, name, email, password_hash, city)
            Nurse(id, name, email, password_hash, licence_number, verified, specialties)
            Shift(id, hospital_id -> Hospital, ward, specialty, starts_at, ends_at, hourly_rate, status)
            Application(id, shift_id -> Shift, nurse_id -> Nurse, status)
Features:   - Post shifts with ward, specialty and hourly rate
            - Let verified nurses apply to shifts
            - Accept one nurse per shift
            - Notify nurses of new shifts matching their specialty
            - Show nurses their upcoming confirmed shifts
API:        REST
            GET  /shifts
            POST /shifts
            POST /shifts/{id}/applications
            POST /applications/{id}/accept
            GET  /me/shifts
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Angular
```

---

## Example 65

**Intent:**
comment system i can embed on my static blog

**Spec:**
```
Type:       Web application (embeddable comments)
Auth:       Commenters sign in with GitHub or post as guest with name and email
Data model: Site(id, domain, owner_email)
            Thread(id, site_id -> Site, page_url)
            Comment(id, thread_id -> Thread, parent_id -> Comment, author_name, body, status, created_at)
Features:   - Embed comments on any page with a script tag
            - Reply to comments in threads
            - Hold first-time comments for moderation
            - Filter spam with Akismet
            - Notify the site owner of new comments
API:        REST
            GET  /threads?url=
            POST /comments
            PATCH /admin/comments/{id}
            GET  /embed.js
Storage:    SQLite
Tech stack: Go, Preact widget, Akismet API
```

---

## Example 66

**Intent:**
course platform with certificates

**Spec:**
```
Type:       Web application (online course platform)
Auth:       Email + password
Data model: Learner(id, name, email, password_hash)
            Course(id, title, description)
            Module(id, course_id -> Course, title, content, position)
            QuizResult(id, module_id -> Module, learner_id -> Learner, score)
            Certificate(id, learner_id -> Learner, course_id -> Course, code, issued_at)
Features:   - Show course modules in order
            - End each module with a short quiz
            - Issue a PDF certificate when all quizzes pass
            - Give each certificate a public verification link
            - Show learners their progress
API:        REST
            GET  /courses
            GET  /courses/{id}/modules
            POST /modules/{id}/quiz
            GET  /certificates/{code}
Storage:    PostgreSQL
Tech stack: Python, Django, WeasyPrint
```

---

## Example 67

**Intent:**
voluntario sistema para ong, voluntarios marcam disponibilidade e coordenador vê quem pode. english pls

**Spec:**
```
Type:       Web application (volunteer coordination)
Auth:       Email + password, roles: volunteer and coordinator
Data model: Volunteer(id, name, email, phone, password_hash, skills)
            Availability(id, volunteer_id -> Volunteer, weekday, start_time, end_time)
            Activity(id, title, date, needed_skills, needed_count)
            Invitation(id, activity_id -> Activity, volunteer_id -> Volunteer, status)
Features:   - Let volunteers set their weekly availability
            - Create activities with date and needed skills
            - Show coordinators who is available and has the right skills
            - Invite volunteers and track replies
            - Support Portuguese and English
API:        REST
            PUT  /me/availability
            POST /activities
            GET  /activities/{id}/available-volunteers
            POST /activities/{id}/invitations
            PATCH /invitations/{id}
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, i18next
```

---

## Example 68

**Intent:**
im building a saas and need the boring parts: teams, roles, billing, invites

**Spec:**
```
Type:       Web application (multi-tenant SaaS boilerplate)
Auth:       Email + password and Google OAuth, email verification
Data model: User(id, email, password_hash, name)
            Organization(id, name, slug, stripe_customer_id, plan)
            Membership(user_id -> User, organization_id -> Organization, role)
            Invite(id, organization_id -> Organization, email, role, token, expires_at)
Features:   - Create organizations and switch between them
            - Invite members by email with a role (owner, admin, member)
            - Enforce role permissions on every endpoint
            - Manage subscription plans with Stripe Billing and the customer portal
            - Write an audit log of membership changes
API:        REST
            POST /orgs
            GET  /orgs/{slug}/members
            POST /orgs/{slug}/invites
            POST /invites/{token}/accept
            POST /orgs/{slug}/billing/portal
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Auth.js, Prisma, Stripe
```

---

## Example 69

**Intent:**
site to share my poems

**Spec:**
```
Type:       Web application (personal blog)
Data model: Poem(id, title, body, written_on, tags)
Features:   - List poems newest first
            - Show each poem on its own page with clean typography
            - Filter by tag
            - Generate an RSS feed
Storage:    Markdown files in the repo
Tech stack: Hugo, Netlify
```

---

## Example 70

**Intent:**
Make a review website for video games with critic and user scores, written in typescript

**Spec:**
```
Type:       Web application (review site)
Auth:       Email + password, critic role assigned by admin
Data model: User(id, username, email, password_hash, role)
            Game(id, title, platforms, release_date, cover_url)
            Review(id, game_id -> Game, user_id -> User, score, body, is_critic, created_at)
Features:   - Show separate critic and user average scores per game
            - Write reviews with a 0-100 score
            - Filter games by platform and year
            - Prevent more than one review per user per game
            - Show top rated games this year
API:        REST
            GET  /games
            GET  /games/{id}
            POST /games/{id}/reviews
            GET  /games/top?year=
Storage:    PostgreSQL
Tech stack: TypeScript, Express, Prisma, React
```

---

## Example 71

**Intent:**
kickstarter for music albums

**Spec:**
```
Type:       Web application (crowdfunding)
Auth:       Email + password for artists, fans pay as guests or with an account
Data model: Artist(id, name, email, password_hash, bio)
            Album(id, artist_id -> Artist, title, goal_cents, deadline, status)
            Perk(id, album_id -> Album, title, price_cents, includes_download)
            Backing(id, perk_id -> Perk, fan_email, amount_cents, status)
Features:   - Launch an album campaign with a funding goal and perks
            - Play a preview track on the campaign page
            - Charge backers only if the goal is reached
            - Send backers a download link when the album is released
            - Show artists a list of backers
API:        REST
            GET  /albums
            POST /albums
            POST /perks/{id}/back
            POST /albums/{id}/release
            GET  /albums/{id}/backers
Storage:    PostgreSQL, S3 (audio)
Tech stack: Python, FastAPI, Svelte, Stripe
```

---

## Example 72

**Intent:**
doc collaboration like google docs but for screenplays

**Spec:**
```
Type:       Web application (collaborative editor)
Auth:       Email + password, share by invite
Data model: User(id, email, name, password_hash)
            Script(id, owner_id -> User, title, updated_at)
            Collaborator(script_id -> Script, user_id -> User, role)
            Comment(id, script_id -> Script, user_id -> User, anchor, body, resolved)
Features:   - Format text as scene headings, action, character and dialogue automatically
            - Edit the same script live with collaborators
            - Leave comments on lines
            - Export to PDF in standard screenplay format
            - Import and export Fountain files
API:        REST and WebSocket
            POST /scripts
            GET  /scripts/{id}
            POST /scripts/{id}/collaborators
            GET  /scripts/{id}/export.pdf
            WS   /scripts/{id}/collab
Storage:    PostgreSQL
Tech stack: TypeScript, React, ProseMirror, Yjs, Node.js
```

---

## Example 73

**Intent:**
mentorship platform matching junior devs with senior devs

**Spec:**
```
Type:       Web application (mentorship matching)
Auth:       GitHub OAuth sign-in
Data model: User(id, github_username, name, role, skills, timezone, bio)
            MentorshipRequest(id, mentee_id -> User, mentor_id -> User, goals, status)
            Session(id, request_id -> MentorshipRequest, scheduled_at, notes)
Features:   - Create mentor or mentee profiles with skills and time zone
            - Suggest mentors that match skills and time zone
            - Send a mentorship request with goals
            - Schedule sessions and keep session notes
            - Limit mentors to a chosen number of mentees
API:        REST
            GET  /mentors?skill=
            POST /requests
            PATCH /requests/{id}
            POST /requests/{id}/sessions
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX, GitHub OAuth
```

---

## Example 74

**Intent:**
Hi, I make digital planners and want to sell them as downloads on my own site instead of Etsy.

**Spec:**
```
Type:       Web application (digital products store)
Auth:       Customers check out as guests, admin login for the owner
Data model: Product(id, name, description, price_cents, file_key, preview_images)
            Order(id, customer_email, total_cents, stripe_session_id, created_at)
            OrderItem(id, order_id -> Order, product_id -> Product)
            DownloadLink(id, order_item_id -> OrderItem, token, expires_at, downloads)
Features:   - Show products with preview images
            - Take payment with Stripe Checkout
            - Email a time-limited download link after payment
            - Limit each link to 5 downloads
            - Add discount codes
API:        REST
            GET  /products
            POST /checkout
            POST /webhooks/stripe
            GET  /download/{token}
Storage:    PostgreSQL, S3 (product files, private)
Tech stack: Next.js, Stripe, Resend
```

---

## Example 75

**Intent:**
social network for dog owners

**Spec:**
```
Type:       Web application (social network)
Auth:       Email + password or Google sign-in
Data model: Owner(id, name, email, city)
            Dog(id, owner_id -> Owner, name, breed, birthday, photo_url)
            Post(id, dog_id -> Dog, image_url, caption, created_at)
            Follow(follower_id -> Owner, dog_id -> Dog)
            Like(owner_id -> Owner, post_id -> Post)
Features:   - Create profiles for each dog
            - Post photos to a feed
            - Follow other dogs and like posts
            - Find dog owners nearby for playdates
            - Show a feed of posts from followed dogs
API:        REST
            GET  /feed
            POST /dogs
            POST /posts
            POST /dogs/{id}/follow
            POST /posts/{id}/like
            GET  /owners/nearby
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: Node.js, NestJS, React
```

---

## Example 76

**Intent:**
we need an intranet where employees can see news, birthdays and the staff directory

**Spec:**
```
Type:       Web application (intranet portal)
Auth:       Microsoft Entra ID single sign-on
Data model: Employee(id, name, email, department, job_title, phone, birthday, photo_url)
            NewsPost(id, author_id -> Employee, title, body, published_at, pinned)
Features:   - Show company news with pinned posts at the top
            - Search the staff directory by name or department
            - Show this week's birthdays
            - Sync employee data from Microsoft Graph nightly
API:        REST
            GET  /news
            POST /news
            GET  /employees?q=
            GET  /birthdays/this-week
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Blazor, Microsoft Graph API
```

---

## Example 77

**Intent:**
tutoring marketplace

**Spec:**
```
Type:       Web application (tutoring marketplace)
Auth:       Email + password, roles: tutor and student
Data model: Tutor(id, user_id -> User, subjects, hourly_rate, bio, rating)
            User(id, name, email, password_hash, role)
            Booking(id, tutor_id -> Tutor, student_id -> User, starts_at, duration_minutes, status, price)
            Review(id, booking_id -> Booking, rating, comment)
Features:   - Search tutors by subject, price and rating
            - Book a lesson from the tutor's calendar
            - Pay upfront and pay out tutors after the lesson
            - Join lessons through a video link
            - Review tutors after a lesson
API:        REST
            GET  /tutors?subject=
            GET  /tutors/{id}/availability
            POST /bookings
            POST /bookings/{id}/review
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React, Stripe Connect, Daily.co video
```

---

## Example 78

**Intent:**
my sister runs a quilting guild and they keep using facebook groups for everything, she wants a proper website where they can post their quilts, sign up for workshops and see the newsletter, nothing too complicated cause most members are older

**Spec:**
```
Type:       Web application (club community site)
Auth:       Email + password, accounts approved by an admin
Data model: Member(id, name, email, password_hash, approved)
            Quilt(id, member_id -> Member, title, photo_url, description)
            Workshop(id, title, date, teacher, seats)
            WorkshopSignup(workshop_id -> Workshop, member_id -> Member)
            Newsletter(id, title, pdf_url, month)
Features:   - Show a gallery of members' quilts
            - Let members sign up for workshops with limited seats
            - Post monthly newsletters as PDFs
            - Approve new members before they can post
            - Keep the layout simple with large text and buttons
API:        REST
            GET  /quilts
            POST /quilts
            GET  /workshops
            POST /workshops/{id}/signup
            GET  /newsletters
Storage:    MySQL
Tech stack: PHP, Laravel, Blade
```

---

## Example 79

**Intent:**
a slack-like chat app for small teams

**Spec:**
```
Type:       Web application (team chat)
Auth:       Email + password, workspace invites
Data model: Workspace(id, name)
            User(id, email, name, password_hash)
            Channel(id, workspace_id -> Workspace, name, is_private)
            Message(id, channel_id -> Channel, user_id -> User, body, thread_parent_id -> Message, created_at)
            ChannelMember(channel_id -> Channel, user_id -> User, last_read_at)
Features:   - Create public and private channels
            - Send messages in real time
            - Reply in threads
            - Show unread counts per channel
            - Upload files and images in messages
API:        REST and WebSocket
            GET  /channels
            POST /channels
            GET  /channels/{id}/messages
            POST /channels/{id}/messages
            WS   /ws
Storage:    PostgreSQL, S3 (files)
Tech stack: Elixir, Phoenix Channels, React
```

---

## Example 80

**Intent:**
blog cms with multiple authors and editor approval

**Spec:**
```
Type:       Web application (CMS)
Auth:       Email + password, roles: author, editor, admin
Data model: User(id, name, email, password_hash, role)
            Article(id, author_id -> User, title, slug, body, status, published_at)
            ReviewNote(id, article_id -> Article, editor_id -> User, note, created_at)
Features:   - Let authors write and submit articles for review
            - Let editors approve, request changes or schedule publication
            - Keep a status workflow draft, in review, scheduled, published
            - Show each author's articles and status
            - Publish scheduled articles automatically
API:        REST
            GET  /articles
            POST /articles
            POST /articles/{id}/submit
            POST /articles/{id}/approve
            POST /articles/{id}/request-changes
Storage:    PostgreSQL
Tech stack: Python, Django, Celery Beat
```

---

## Example 81

**Intent:**
a site where people anonymously share salaries for tech jobs

**Spec:**
```
Type:       Web application (salary sharing)
Auth:       Optional account, submissions stored without user link
Data model: SalaryReport(id, company, job_title, level, location, base_salary, bonus, years_experience, currency, submitted_at)
            Company(id, name, slug)
Features:   - Submit a salary report without an account
            - Show median salary by company, title and location
            - Hide groups with fewer than 3 reports
            - Filter by years of experience
            - Convert currencies for comparison
API:        REST
            POST /reports
            GET  /companies/{slug}/salaries
            GET  /salaries?title=&location=
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Svelte
```

---

## Example 82

**Intent:**
ai tool for writing product descriptions for my shopify store

**Spec:**
```
Type:       Web application (AI writing assistant)
Auth:       Shopify OAuth app install
Data model: Shop(id, shop_domain, access_token, plan)
            Product(id, shop_id -> Shop, shopify_product_id, title, generated_description, status)
Features:   - Import products from the Shopify store
            - Generate descriptions from title, attributes and a chosen brand voice
            - Edit the generated text before saving
            - Push approved descriptions back to Shopify
            - Generate in bulk for many products
API:        REST
            GET  /auth/shopify/callback
            GET  /products
            POST /products/{id}/generate
            POST /products/{id}/publish
            POST /products/bulk-generate
Storage:    PostgreSQL
Tech stack: Node.js, Remix, Shopify Admin API, OpenAI API
```

---

## Example 83

**Intent:**
help me make site so artists in my country can sell paintings, need commission take 10% for the site

**Spec:**
```
Type:       Web application (art marketplace)
Auth:       Email + password, roles: artist and buyer
Data model: Artist(id, name, email, password_hash, payout_account_id)
            Artwork(id, artist_id -> Artist, title, medium, width_cm, height_cm, price, image_url, status)
            Order(id, artwork_id -> Artwork, buyer_id -> Buyer, total, commission, status)
            Buyer(id, name, email, password_hash, address)
Features:   - Let artists upload artworks with size, medium and price
            - Browse and filter artworks by medium and price
            - Take payment and keep a 10% platform commission
            - Pay the artist the rest after delivery
            - Mark an artwork sold so it cannot be bought twice
API:        REST
            GET  /artworks
            POST /artworks
            POST /artworks/{id}/orders
            PATCH /orders/{id}
Storage:    PostgreSQL, Cloudinary (images)
Tech stack: Python, Django, Stripe Connect
```

---

## Example 84

**Intent:**
personal knowledge base with backlinks

**Spec:**
```
Type:       Web application (personal knowledge base)
Auth:       Single-user login
Data model: Note(id, title, body_markdown, created_at, updated_at)
            Link(from_note_id -> Note, to_note_id -> Note)
Features:   - Write notes in Markdown
            - Link notes with [[double brackets]]
            - Show backlinks at the bottom of each note
            - Show a graph view of linked notes
            - Search notes instantly
API:        REST
            GET  /notes
            POST /notes
            PUT  /notes/{id}
            GET  /notes/{id}/backlinks
            GET  /graph
Storage:    SQLite
Tech stack: SvelteKit, better-sqlite3, D3.js
```

---

## Example 85

**Intent:**
platform where youth sports clubs manage teams, schedules and parent messages

**Spec:**
```
Type:       Web application (sports club management)
Auth:       Email + password, roles: club admin, coach, parent
Data model: Club(id, name)
            Team(id, club_id -> Club, name, age_group, coach_id -> User)
            Player(id, team_id -> Team, name, parent_id -> User)
            User(id, name, email, password_hash, role)
            Game(id, team_id -> Team, opponent, starts_at, location)
            Announcement(id, team_id -> Team, body, created_at)
Features:   - Manage teams and player rosters
            - Publish game and practice schedules
            - Send announcements to parents of a team
            - Let parents mark if their child can attend
            - Sync schedules to phone calendars via iCal
API:        REST
            GET  /teams/{id}/schedule
            POST /teams/{id}/games
            POST /teams/{id}/announcements
            POST /games/{id}/availability
            GET  /teams/{id}/calendar.ics
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire
```

---

## Example 86

**Intent:**
wiki for fans of a tv show

**Spec:**
```
Type:       Web application (fan wiki)
Auth:       Email + password, edits by registered users, admins can protect pages
Data model: User(id, username, email, password_hash, role)
            Article(id, title, slug, body, infobox_json, protected)
            Revision(id, article_id -> Article, user_id -> User, body, created_at)
            Category(id, name)
            ArticleCategory(article_id -> Article, category_id -> Category)
Features:   - Create articles for characters, episodes and places
            - Add infoboxes with structured facts
            - Track revisions and revert vandalism
            - Protect popular pages from editing
            - Browse by category
API:        REST
            GET  /wiki/{slug}
            PUT  /wiki/{slug}
            GET  /wiki/{slug}/revisions
            POST /wiki/{slug}/revert/{rev_id}
            GET  /categories/{id}
Storage:    MariaDB
Tech stack: MediaWiki
```

---

## Example 87

**Intent:**
newsletter with paid subscribers and free posts, built with django

**Spec:**
```
Type:       Web application (newsletter platform)
Auth:       Email + password or magic link for readers
Data model: Reader(id, email, password_hash, is_paid, stripe_customer_id)
            Post(id, title, body, is_paid_only, published_at)
            EmailSend(id, post_id -> Post, sent_count, opened_count, sent_at)
Features:   - Publish posts as both web pages and emails
            - Lock paid-only posts behind a subscription
            - Sell monthly and yearly subscriptions with Stripe
            - Send posts to the right audience (all or paid)
            - Show subscriber growth on a dashboard
API:        REST
            POST /subscribe
            POST /checkout
            GET  /posts/{slug}
            POST /admin/posts/{id}/send
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Python, Django, Celery, Stripe, Postmark
```

---

## Example 88

**Intent:**
buy sell trade video games locally

**Spec:**
```
Type:       Web application (local marketplace)
Auth:       Email + password
Data model: User(id, username, email, password_hash, city)
            Listing(id, user_id -> User, game_title, platform, condition, price, open_to_trade, status)
            Message(id, listing_id -> Listing, from_id -> User, to_id -> User, body, sent_at)
Features:   - List games for sale or trade
            - Search by title, platform and city
            - Message sellers inside the site
            - Mark listings as sold or traded
            - Save searches and get alerts
API:        REST
            GET  /listings
            POST /listings
            POST /listings/{id}/messages
            PATCH /listings/{id}
            POST /saved-searches
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js
```

---

## Example 89

**Intent:**
An app where my coworkers can propose ideas and vote on them, best ideas go to management each month.

**Spec:**
```
Type:       Web application (idea voting)
Auth:       Company SSO with Google Workspace
Data model: Employee(id, name, email, department)
            Idea(id, author_id -> Employee, title, description, status, created_at)
            Vote(idea_id -> Idea, employee_id -> Employee)
            Comment(id, idea_id -> Idea, author_id -> Employee, body)
Features:   - Submit ideas with a title and description
            - Upvote ideas once per person
            - Comment on ideas
            - Show a monthly top-10 list for management
            - Let managers mark ideas as planned, done or declined
API:        REST
            GET  /ideas?sort=votes
            POST /ideas
            POST /ideas/{id}/vote
            POST /ideas/{id}/comments
            PATCH /ideas/{id}
Storage:    PostgreSQL
Tech stack: Python, Flask, React
```

---

## Example 90

**Intent:**
forum but its for teenagers so needs strong moderation

**Spec:**
```
Type:       Web application (moderated forum)
Auth:       Email + password, parental consent email for under-16 users
Data model: User(id, username, email, password_hash, birth_year, consent_confirmed, status)
            Topic(id, author_id -> User, title, body, created_at, hidden)
            Reply(id, topic_id -> Topic, author_id -> User, body, hidden)
            Report(id, target_type, target_id, reporter_id -> User, reason, status)
Features:   - Filter profanity and personal info like phone numbers before posting
            - Run posts through an AI moderation check
            - Let users report posts and hide them after 3 reports
            - Give moderators a review queue
            - Block private messages between users
API:        REST
            GET  /topics
            POST /topics
            POST /topics/{id}/replies
            POST /reports
            GET  /mod/queue
            PATCH /mod/reports/{id}
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, OpenAI Moderation API, React
```

---

## Example 91

**Intent:**
saas for restaurants to collect customer feedback by qr code

**Spec:**
```
Type:       Web application (multi-tenant SaaS)
Auth:       Email + password for restaurant owners, customers give feedback without login
Data model: Restaurant(id, name, owner_email, password_hash, slug)
            Table(id, restaurant_id -> Restaurant, number, qr_token)
            Feedback(id, restaurant_id -> Restaurant, table_id -> Table, rating, comment, created_at)
Features:   - Generate a QR code for each table
            - Show a short feedback form when the QR code is scanned
            - Alert the owner by email about ratings of 2 or less
            - Show average rating per week on a dashboard
            - Separate data per restaurant
API:        REST
            POST /restaurants
            POST /restaurants/{id}/tables
            GET  /f/{qr_token}
            POST /f/{qr_token}
            GET  /dashboard/stats
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Jinja2, qrcode library
```

---

## Example 92

**Intent:**
Hello! I would like to create online school for my language, Georgian, with lessons, audio and small tests. Students pay monthly.

**Spec:**
```
Type:       Web application (language learning platform)
Auth:       Email + password, Stripe subscription
Data model: Student(id, email, password_hash, subscription_status)
            Unit(id, title, level, position)
            Lesson(id, unit_id -> Unit, title, text, audio_url)
            Exercise(id, lesson_id -> Lesson, type, prompt, answer)
            Progress(student_id -> Student, lesson_id -> Lesson, score, completed_at)
Features:   - Organise lessons into units by level
            - Play native speaker audio for each lesson
            - Check exercise answers automatically
            - Charge a monthly subscription
            - Show the Georgian alphabet with pronunciation
API:        REST
            GET  /units
            GET  /lessons/{id}
            POST /exercises/{id}/answer
            POST /checkout
            POST /webhooks/stripe
Storage:    PostgreSQL, S3 (audio)
Tech stack: Python, Django, Stripe
```

---

## Example 93

**Intent:**
link sharing site for designers, like dribbble meets pinboard

**Spec:**
```
Type:       Web application (bookmarking community)
Auth:       Email + password or Google sign-in
Data model: User(id, username, email)
            Bookmark(id, user_id -> User, url, title, preview_image, note, created_at)
            Collection(id, user_id -> User, name, is_public)
            CollectionItem(collection_id -> Collection, bookmark_id -> Bookmark)
            Save(user_id -> User, bookmark_id -> Bookmark)
Features:   - Save links with an auto-fetched preview image
            - Organise bookmarks into public or private collections
            - Browse popular links from other designers
            - Save other people's bookmarks to your collections
            - Tag bookmarks and filter by tag
API:        REST
            POST /bookmarks
            GET  /explore
            GET  /collections/{id}
            POST /collections/{id}/items
            POST /bookmarks/{id}/save
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stimulus, Open Graph scraping
```

---

## Example 94

**Intent:**
simple poll website

**Spec:**
```
Type:       Web application (polls)
Data model: Poll(id, question, created_at, closes_at, share_code)
            Option(id, poll_id -> Poll, text)
            Vote(id, option_id -> Option, voter_hash, created_at)
Features:   - Create a poll with several options
            - Share the poll by a short link
            - Allow one vote per browser
            - Show live results as a bar chart
API:        REST
            POST /polls
            GET  /polls/{code}
            POST /polls/{code}/vote
            GET  /polls/{code}/results
Storage:    SQLite
Tech stack: Python, Flask, Chart.js
```

---

## Example 95

**Intent:**
website for a makerspace where members book the laser cutter and 3d printers

**Spec:**
```
Type:       Web application (equipment booking)
Auth:       Email + password, equipment access only after training is recorded
Data model: Member(id, name, email, password_hash)
            Machine(id, name, type, hourly_cost)
            Training(member_id -> Member, machine_id -> Machine, completed_on)
            Booking(id, machine_id -> Machine, member_id -> Member, starts_at, ends_at)
Features:   - Show a calendar of bookings per machine
            - Book a machine only if trained on it
            - Prevent overlapping bookings
            - Record training sign-offs by staff
            - Bill members monthly for machine time
API:        REST
            GET  /machines/{id}/bookings
            POST /machines/{id}/bookings
            DELETE /bookings/{id}
            POST /trainings
            GET  /members/{id}/invoice
Storage:    PostgreSQL
Tech stack: Python, Django, FullCalendar
```

---

## Example 96

**Intent:**
elearning site with live classes not just videos

**Spec:**
```
Type:       Web application (live online classes)
Auth:       Email + password, roles: teacher and student
Data model: User(id, name, email, password_hash, role)
            Class(id, teacher_id -> User, title, starts_at, duration_minutes, capacity, price)
            Enrollment(class_id -> Class, student_id -> User, paid)
            Recording(id, class_id -> Class, video_url)
Features:   - Schedule live classes with capacity and price
            - Enroll and pay for a class
            - Join the live class in the browser with video and chat
            - Record classes and share recordings with enrolled students
            - Remind students 1 hour before class
API:        REST
            GET  /classes
            POST /classes
            POST /classes/{id}/enroll
            GET  /classes/{id}/join-token
            GET  /classes/{id}/recording
Storage:    PostgreSQL
Tech stack: Node.js, Next.js, LiveKit, Stripe
```

---

## Example 97

**Intent:**
website where volunteers can sign up to clean beaches and log how much trash they picked up

**Spec:**
```
Type:       Web application (volunteer events)
Auth:       Email + password or Google sign-in
Data model: Volunteer(id, name, email)
            Cleanup(id, beach_name, lat, lng, date, organiser_id -> Volunteer)
            Participation(cleanup_id -> Cleanup, volunteer_id -> Volunteer)
            TrashLog(id, cleanup_id -> Cleanup, volunteer_id -> Volunteer, kg, item_counts_json)
Features:   - Show upcoming cleanups on a map
            - Sign up for a cleanup
            - Log kilograms and item types collected
            - Show totals per beach and per volunteer
            - Show a public impact counter on the home page
API:        REST
            GET  /cleanups
            POST /cleanups
            POST /cleanups/{id}/join
            POST /cleanups/{id}/logs
            GET  /stats
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React, Leaflet
```

---

## Example 98

**Intent:**
help center + community forum combined for my app

**Spec:**
```
Type:       Web application (help center and community)
Auth:       Single sign-on from the main app via JWT
Data model: User(id, external_id, name, email)
            Article(id, title, body, category, updated_at)
            Question(id, user_id -> User, title, body, status)
            Answer(id, question_id -> Question, user_id -> User, body, is_official)
Features:   - Publish official help articles
            - Let users ask and answer questions in a community area
            - Mark staff answers as official
            - Suggest related articles while a user types a question
            - Turn good answers into help articles
API:        REST
            GET  /articles
            GET  /questions
            POST /questions
            POST /questions/{id}/answers
            GET  /suggest?q=
Storage:    PostgreSQL, Meilisearch
Tech stack: TypeScript, Remix, Meilisearch
```

---

## Example 99

**Intent:**
something like goodreads but for board games

**Spec:**
```
Type:       Web application (social cataloguing)
Auth:       Email + password
Data model: User(id, username, email, password_hash)
            Game(id, title, designer, min_players, max_players, play_minutes)
            ShelfEntry(user_id -> User, game_id -> Game, shelf, rating)
            Review(id, user_id -> User, game_id -> Game, body, created_at)
            Follow(follower_id -> User, followee_id -> User)
Features:   - Add games to shelves like Owned, Want to play and Played
            - Rate and review games
            - Follow friends and see their activity
            - Show game pages with average rating
            - Recommend games based on your ratings
API:        REST
            GET  /games/{id}
            PUT  /me/shelves/{game_id}
            POST /games/{id}/reviews
            POST /users/{id}/follow
            GET  /feed
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 100

**Intent:**
client portal for my design agency where clients see project files and approve stuff

**Spec:**
```
Type:       Web application (client portal)
Auth:       Email + password for staff, magic-link login for clients
Data model: Client(id, company, contact_email)
            Project(id, client_id -> Client, name, status)
            Deliverable(id, project_id -> Project, title, file_url, version, approval_status)
            Feedback(id, deliverable_id -> Deliverable, author, body, created_at)
Features:   - Upload deliverables with versions
            - Let clients approve or request changes
            - Comment on deliverables
            - Show project status and timeline
            - Notify staff when a client approves
API:        REST
            GET  /projects
            GET  /projects/{id}/deliverables
            POST /deliverables
            POST /deliverables/{id}/approve
            POST /deliverables/{id}/feedback
Storage:    PostgreSQL, S3 (files)
Tech stack: Laravel, Inertia.js, Vue.js
```

---

## Example 101

**Intent:**
lowkey want a twitter clone for my friend group lol

**Spec:**
```
Type:       Web application (microblogging)
Auth:       Invite code + email + password
Data model: User(id, handle, email, password_hash, avatar_url)
            Post(id, user_id -> User, body, reply_to_id -> Post, created_at)
            Follow(follower_id -> User, followee_id -> User)
            Like(user_id -> User, post_id -> Post)
Features:   - Post short messages up to 280 characters
            - Follow friends and see their posts in a timeline
            - Reply to and like posts
            - Mention people with @handle and notify them
            - Join only with an invite code
API:        REST
            GET  /timeline
            POST /posts
            POST /posts/{id}/like
            POST /users/{handle}/follow
            GET  /notifications
Storage:    PostgreSQL
Tech stack: Node.js, Fastify, React
```

---

## Example 102

**Intent:**
An AI tool that reads my students essays and suggests a grade with a rubric.

**Spec:**
```
Type:       Web application (AI grading assistant)
Auth:       Email + password for teachers
Data model: Teacher(id, email, password_hash)
            Rubric(id, teacher_id -> Teacher, name, criteria_json)
            Essay(id, rubric_id -> Rubric, student_name, text, suggested_scores_json, final_grade)
Features:   - Create rubrics with criteria and point levels
            - Upload essays as text or .docx
            - Suggest a score and short feedback for each criterion with an LLM
            - Let the teacher adjust scores before finalising
            - Export grades to CSV
API:        REST
            POST /rubrics
            POST /essays
            POST /essays/{id}/grade
            PATCH /essays/{id}
            GET  /rubrics/{id}/grades.csv
Storage:    PostgreSQL
Tech stack: Python, FastAPI, python-docx, Anthropic Claude API, React
```

---

## Example 103

**Intent:**
neighbourhood noticeboard website

**Spec:**
```
Type:       Web application (community noticeboard)
Auth:       Email + password with postcode on signup
Data model: Resident(id, name, email, password_hash, postcode)
            Notice(id, author_id -> Resident, category, title, body, expires_at, created_at)
Features:   - Post notices in categories like Lost & Found, For Sale and Events
            - Show notices for the resident's postcode area
            - Expire notices automatically
            - Report inappropriate notices
API:        REST
            GET  /notices?postcode=
            POST /notices
            DELETE /notices/{id}
            POST /notices/{id}/report
Storage:    PostgreSQL
Tech stack: PHP, Slim Framework, Alpine.js
```

---

## Example 104

**Intent:**
open source project showcase site where devs submit their projects and others star them

**Spec:**
```
Type:       Web application (project showcase)
Auth:       GitHub OAuth sign-in
Data model: User(id, github_username, avatar_url)
            Project(id, submitter_id -> User, repo_url, name, description, language, stars_cached)
            Upvote(user_id -> User, project_id -> Project)
Features:   - Submit a GitHub repository and fetch its details automatically
            - Upvote projects
            - Show trending projects this week
            - Filter by programming language
            - Refresh GitHub star counts daily
API:        REST
            GET  /projects?lang=&sort=
            POST /projects
            POST /projects/{id}/upvote
Storage:    PostgreSQL
Tech stack: Go, Echo, GitHub REST API, htmx
```

---

## Example 105

**Intent:**
alumni network for my old high school

**Spec:**
```
Type:       Web application (alumni network)
Auth:       Email + password, admin approval with graduation year check
Data model: Alumnus(id, name, email, password_hash, graduation_year, city, occupation, approved)
            Event(id, title, date, location)
            RSVP(event_id -> Event, alumnus_id -> Alumnus, status)
            Post(id, alumnus_id -> Alumnus, body, created_at)
Features:   - Search alumni by graduation year, city and job
            - Post news and updates
            - RSVP to reunions
            - Approve new members before they see the directory
            - Send a newsletter to all alumni
API:        REST
            GET  /alumni?year=&city=
            GET  /events
            POST /events/{id}/rsvp
            POST /posts
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 106

**Intent:**
wanna make a site were ppl post there cosplay pics and vote best one each month

**Spec:**
```
Type:       Web application (photo contest community)
Auth:       Email + password or Discord sign-in
Data model: User(id, username, email, avatar_url)
            Contest(id, month, theme, starts_at, ends_at)
            Entry(id, contest_id -> Contest, user_id -> User, character_name, series, image_url)
            Vote(entry_id -> Entry, user_id -> User)
Features:   - Upload cosplay photos to the current monthly contest
            - Vote once per entry, not on your own entry
            - Close voting at the end of the month and announce winners
            - Show a hall of fame of past winners
            - Tag entries by character and series
API:        REST
            GET  /contests/current
            POST /contests/{id}/entries
            POST /entries/{id}/vote
            GET  /hall-of-fame
Storage:    PostgreSQL, Cloudinary (images)
Tech stack: Node.js, Express, React, Passport (Discord OAuth)
```

---

## Example 107

**Intent:**
forum software in php

**Spec:**
```
Type:       Web application (forum)
Auth:       Username + email + password registration, email confirmation
Data model: User(id, username, email, password_hash, role, post_count)
            Forum(id, name, description, position)
            Thread(id, forum_id -> Forum, user_id -> User, title, sticky, locked)
            Post(id, thread_id -> Thread, user_id -> User, body_bbcode, created_at)
Features:   - Organise forums into sections
            - Post threads and replies with BBCode formatting
            - Pin and lock threads as a moderator
            - Show who is online
            - Paginate long threads
API:        REST
            GET  /forums
            GET  /forums/{id}
            POST /threads
            GET  /threads/{id}?page=
            POST /threads/{id}/posts
Storage:    MySQL
Tech stack: PHP 8, Laravel, Blade
```

---

## Example 108

**Intent:**
i want people pay me to put their job ads on my site for graphic designers in europe

**Spec:**
```
Type:       Web application (paid job board)
Auth:       Employer accounts (email + password), applicants apply on the employer site
Data model: Employer(id, company, email, password_hash, country)
            JobAd(id, employer_id -> Employer, title, description, location, remote, salary_range, paid_until, status)
            Payment(id, job_ad_id -> JobAd, amount_cents, vat_id, paid_at)
Features:   - Post a job ad and pay per listing with Stripe
            - Collect EU VAT numbers on invoices
            - Filter jobs by country and remote
            - Expire ads after the paid period
            - Offer a discount bundle of 5 ads
API:        REST
            GET  /jobs?country=&remote=
            POST /jobs
            POST /jobs/{id}/checkout
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe Tax
```

---

## Example 109

**Intent:**
Our dance school needs a website where parents see class schedule, pay term fees and get announcements.

**Spec:**
```
Type:       Web application (school portal)
Auth:       Email + password for parents, admin login for staff
Data model: Parent(id, name, email, password_hash)
            Child(id, parent_id -> Parent, name, birth_date)
            DanceClass(id, style, level, weekday, time, teacher)
            Enrollment(child_id -> Child, class_id -> DanceClass, term)
            Invoice(id, parent_id -> Parent, term, amount_cents, status)
Features:   - Show the weekly class timetable
            - Enroll children in classes for a term
            - Pay term fees online
            - Post announcements and email them to parents
            - Show unpaid invoices to staff
API:        REST
            GET  /classes
            POST /enrollments
            GET  /invoices
            POST /invoices/{id}/pay
            POST /announcements
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe, Action Mailer
```

---

## Example 110

**Intent:**
AI summarizer for youtube videos

**Spec:**
```
Type:       Web application (AI summariser)
Auth:       Google sign-in
Data model: User(id, email)
            VideoSummary(id, user_id -> User, youtube_id, title, transcript, summary, chapters_json, created_at)
Features:   - Paste a YouTube link and fetch its transcript
            - Summarise the video into key points with an LLM
            - Generate timestamped chapters that link to the video
            - Cache summaries so the same video is not processed twice
            - Let users ask follow-up questions about the video
API:        REST
            POST /summaries
            GET  /summaries/{id}
            POST /summaries/{id}/ask
Storage:    PostgreSQL
Tech stack: Python, FastAPI, youtube-transcript-api, OpenAI API, React
```

---

## Example 111

**Intent:**
i want build community website for expats in berlin, people ask question about visa, apartments, also sell furniture. sorry my english

**Spec:**
```
Type:       Web application (expat community)
Auth:       Email + password
Data model: User(id, username, email, password_hash, home_country)
            Question(id, user_id -> User, topic, title, body, created_at)
            Answer(id, question_id -> Question, user_id -> User, body, upvotes)
            Classified(id, user_id -> User, title, price, district, photo_url, status)
Features:   - Ask and answer questions in topics like Visa, Housing and Jobs
            - Upvote helpful answers
            - Post classified ads for furniture and other items
            - Filter classifieds by Berlin district
            - Translate posts with one click
API:        REST
            GET  /questions?topic=
            POST /questions
            POST /questions/{id}/answers
            GET  /classifieds
            POST /classifieds
Storage:    PostgreSQL
Tech stack: Python, Django, DeepL API
```

---

## Example 112

**Intent:**
course marketplace like udemy where anyone can upload courses

**Spec:**
```
Type:       Web application (course marketplace)
Auth:       Email + password, anyone can become an instructor
Data model: User(id, name, email, password_hash, is_instructor, payout_account_id)
            Course(id, instructor_id -> User, title, category, price_cents, status)
            Lecture(id, course_id -> Course, title, video_url, position)
            Purchase(id, course_id -> Course, user_id -> User, amount_cents, created_at)
            Rating(course_id -> Course, user_id -> User, stars, comment)
Features:   - Let instructors upload video courses and submit them for review
            - Sell courses and split revenue with instructors
            - Stream lectures only to buyers
            - Rate and review purchased courses
            - Search courses by category and rating
API:        REST
            GET  /courses?category=
            POST /courses
            POST /courses/{id}/lectures
            POST /courses/{id}/purchase
            POST /courses/{id}/ratings
Storage:    PostgreSQL, Cloudflare Stream (video)
Tech stack: TypeScript, NestJS, Next.js, Stripe Connect
```

---

## Example 113

**Intent:**
need a simple cms for my restaurant to update the menu myself

**Spec:**
```
Type:       Web application (CMS)
Auth:       Single owner login
Data model: MenuSection(id, name, position)
            MenuItem(id, section_id -> MenuSection, name, description, price, is_vegetarian, is_available)
Features:   - Edit menu sections and dishes from an admin page
            - Mark dishes as vegetarian or sold out
            - Show the menu on the public site
            - Generate a printable PDF menu
API:        REST
            GET  /menu
            POST /admin/items
            PUT  /admin/items/{id}
            GET  /menu.pdf
Storage:    SQLite
Tech stack: Python, Flask, WeasyPrint
```

---

## Example 114

**Intent:**
crowdfund for medical bills

**Spec:**
```
Type:       Web application (crowdfunding)
Auth:       Email + password with ID verification for fundraisers
Data model: Fundraiser(id, organiser_id -> User, beneficiary_name, story, goal_cents, raised_cents, status)
            User(id, name, email, password_hash, id_verified)
            Donation(id, fundraiser_id -> Fundraiser, donor_name, amount_cents, anonymous, message)
            Update(id, fundraiser_id -> Fundraiser, body, created_at)
Features:   - Create a fundraiser with a story and goal
            - Verify the organiser's identity before payouts
            - Accept donations with optional anonymity
            - Post updates to donors
            - Withdraw raised funds to a bank account
API:        REST
            POST /fundraisers
            GET  /fundraisers/{id}
            POST /fundraisers/{id}/donations
            POST /fundraisers/{id}/updates
            POST /fundraisers/{id}/withdraw
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Stripe Connect, Stripe Identity
```

---

## Example 115

**Intent:**
collaborative todo lists with my team, real time, using firebase

**Spec:**
```
Type:       Web application (collaboration tool)
Auth:       Firebase Authentication (Google sign-in)
Data model: Team(id, name, member_ids)
            List(id, team_id -> Team, title)
            Todo(id, list_id -> List, text, done, assignee_id, due_date, updated_at)
Features:   - Create shared lists for a team
            - Add, assign and complete todos
            - Sync changes live between all team members
            - Filter todos by assignee
            - Show who changed what recently
Storage:    Firebase Firestore
Tech stack: React, Firebase Authentication, Cloud Firestore
```

---

## Example 116

**Intent:**
i run a small saas, i need a public roadmap page where users suggest features and vote, like canny

**Spec:**
```
Type:       Web application (feedback and roadmap)
Auth:       Users sign in with email magic link, admin login for the team
Data model: User(id, email, name)
            FeatureRequest(id, author_id -> User, title, description, status, vote_count)
            Vote(user_id -> User, request_id -> FeatureRequest)
            Comment(id, request_id -> FeatureRequest, user_id -> User, body)
Features:   - Let users suggest features and vote on them
            - Show a roadmap board with Planned, In progress and Done columns
            - Merge duplicate requests
            - Email voters when a request ships
            - Comment on requests
API:        REST
            GET  /requests?sort=
            POST /requests
            POST /requests/{id}/vote
            PATCH /admin/requests/{id}
            POST /admin/requests/{id}/merge
Storage:    PostgreSQL
Tech stack: Node.js, Hono, React
```

---

## Example 117

**Intent:**
website for my photography to sell digital downloads and book shoots

**Spec:**
```
Type:       Web application (portfolio and booking)
Auth:       Admin login for the photographer, clients check out as guests
Data model: Photo(id, title, gallery, image_url, download_price_cents)
            ShootPackage(id, name, duration_hours, price_cents)
            Booking(id, package_id -> ShootPackage, client_name, client_email, date, deposit_paid)
            Order(id, photo_id -> Photo, buyer_email, paid_at)
Features:   - Show galleries of work
            - Sell full-resolution photo downloads
            - Book a shoot package and pay a deposit
            - Block dates that are already booked
            - Email download links after purchase
API:        REST
            GET  /galleries
            POST /orders
            GET  /packages
            POST /bookings
            GET  /availability
Storage:    PostgreSQL, Backblaze B2 (photos)
Tech stack: Next.js, Stripe, Resend
```

---

## Example 118

**Intent:**
student clubs portal for my college

**Spec:**
```
Type:       Web application (campus community)
Auth:       College SSO via SAML
Data model: Student(id, name, email, year)
            Club(id, name, description, category)
            ClubMembership(club_id -> Club, student_id -> Student, role)
            ClubEvent(id, club_id -> Club, title, starts_at, location)
Features:   - Browse clubs by category
            - Join clubs and leave them
            - Let club officers post events
            - Show a combined campus events calendar
            - Message all members of a club
API:        REST
            GET  /clubs
            POST /clubs/{id}/join
            POST /clubs/{id}/events
            GET  /events
            POST /clubs/{id}/messages
Storage:    PostgreSQL
Tech stack: Python, Django, python3-saml
```

---

## Example 119

**Intent:**
Can you spec out a site where language learners find conversation partners? Like I speak Spanish and want English, so I match with someone who's the other way round.

**Spec:**
```
Type:       Web application (language exchange matching)
Auth:       Email + password or Google sign-in
Data model: User(id, name, email, native_language, learning_language, level, timezone, bio)
            Match(id, user_a_id -> User, user_b_id -> User, status, created_at)
            Message(id, match_id -> Match, sender_id -> User, body, sent_at)
Features:   - Set your native and target languages
            - Suggest partners whose languages are the reverse of yours
            - Send and accept partner requests
            - Chat in the browser
            - Filter partners by time zone and level
API:        REST and WebSocket
            GET  /partners/suggested
            POST /matches
            PATCH /matches/{id}
            GET  /matches/{id}/messages
            WS   /chat
Storage:    PostgreSQL
Tech stack: Node.js, Socket.IO, Vue.js
```

---

## Example 120

**Intent:**
blog with django

**Spec:**
```
Type:       Web application (blog)
Auth:       Django admin login for authors
Data model: Author(id, user_id, bio)
            Post(id, author_id -> Author, title, slug, body, published, created_at)
            Category(id, name, slug)
            Comment(id, post_id -> Post, name, email, body, approved)
Features:   - Write posts in the Django admin
            - List posts by category
            - Show comments after approval
            - Add pagination and an RSS feed
API:        REST
            GET  /blog/
            GET  /blog/{slug}/
            GET  /blog/category/{slug}/
            POST /blog/{slug}/comment/
Storage:    PostgreSQL
Tech stack: Python, Django, Django templates
```

---

## Example 121

**Intent:**
rent out parking spaces app website thing

**Spec:**
```
Type:       Web application (parking space marketplace)
Auth:       Email + password, roles: owner and driver
Data model: User(id, name, email, password_hash)
            Space(id, owner_id -> User, address, lat, lng, price_per_hour, size)
            Availability(id, space_id -> Space, weekday, start_time, end_time)
            Booking(id, space_id -> Space, driver_id -> User, starts_at, ends_at, total, status)
Features:   - List a parking space with price and available hours
            - Search spaces near an address on a map
            - Book and pay for a time slot
            - Prevent double bookings
            - Pay owners monthly
API:        REST
            GET  /spaces?lat=&lng=
            POST /spaces
            POST /spaces/{id}/bookings
            GET  /me/bookings
Storage:    PostgreSQL with PostGIS
Tech stack: Python, FastAPI, React, Mapbox, Stripe Connect
```

---

## Example 122

**Intent:**
discord style community but on the web for my podcast listeners

**Spec:**
```
Type:       Web application (community chat)
Auth:       Email + password, Patreon sign-in unlocks supporter channels
Data model: Member(id, username, email, patreon_tier)
            Channel(id, name, required_tier)
            Message(id, channel_id -> Channel, member_id -> Member, body, created_at)
            Reaction(message_id -> Message, member_id -> Member, emoji)
Features:   - Chat in topic channels in real time
            - Lock some channels to Patreon supporters
            - React to messages with emoji
            - Pin episode discussion threads
            - Let moderators mute members
API:        REST and WebSocket
            GET  /channels
            GET  /channels/{id}/messages
            POST /channels/{id}/messages
            GET  /auth/patreon/callback
            WS   /live
Storage:    PostgreSQL, Redis (pub/sub)
Tech stack: Go, Gorilla WebSocket, Svelte, Patreon API
```

---

## Example 123

**Intent:**
hey i do woodworking youtube and want a members site where people get my plans pdfs and can ask me questions

**Spec:**
```
Type:       Web application (membership site)
Auth:       Email + password, paid membership
Data model: Member(id, email, password_hash, membership_status)
            Plan(id, title, description, pdf_url, difficulty, preview_image)
            Question(id, member_id -> Member, plan_id -> Plan, body, answer, answered_at)
Features:   - Sell a yearly membership
            - Let members download woodworking plans as PDFs
            - Ask questions about a plan
            - Answer questions publicly so all members can read them
            - Email members when new plans are added
API:        REST
            POST /checkout
            GET  /plans
            GET  /plans/{id}/download
            POST /plans/{id}/questions
            PATCH /questions/{id}
Storage:    PostgreSQL, S3 (PDFs)
Tech stack: Laravel, Laravel Cashier (Stripe)
```

---

## Example 124

**Intent:**
marketplace for freelance video editors with portfolios and fixed price packages

**Spec:**
```
Type:       Web application (freelance marketplace)
Auth:       Email + password, roles: buyer and editor
Data model: Editor(id, user_id -> User, showreel_url, skills)
            User(id, name, email, password_hash)
            Package(id, editor_id -> Editor, title, description, price, delivery_days, revisions)
            Order(id, package_id -> Package, buyer_id -> User, brief, status, due_at)
            Delivery(id, order_id -> Order, file_url, note)
Features:   - Show editor profiles with showreels
            - Sell fixed-price packages with delivery time and revisions
            - Upload raw footage and briefs with an order
            - Deliver files and request revisions
            - Release payment when the buyer accepts
API:        REST
            GET  /packages
            POST /packages
            POST /packages/{id}/orders
            POST /orders/{id}/deliveries
            POST /orders/{id}/accept
Storage:    PostgreSQL, S3 (footage)
Tech stack: Ruby on Rails, Stripe Connect, Uppy uploads
```

---

## Example 125

**Intent:**
blog platform for many users like medium

**Spec:**
```
Type:       Web application (blogging platform)
Auth:       Email + password or Google sign-in
Data model: User(id, username, email, bio)
            Story(id, author_id -> User, title, subtitle, body_json, published_at, read_minutes)
            Clap(story_id -> Story, user_id -> User, count)
            Follow(follower_id -> User, author_id -> User)
            Response(id, story_id -> Story, user_id -> User, body)
Features:   - Write stories in a rich-text editor
            - Publish stories under the author's profile
            - Clap for and respond to stories
            - Follow authors and see their stories in a feed
            - Estimate reading time
API:        REST
            GET  /feed
            POST /stories
            GET  /stories/{id}
            POST /stories/{id}/clap
            POST /stories/{id}/responses
            POST /users/{id}/follow
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Editor.js, Prisma
```

---

## Example 126

**Intent:**
i need site for my coworking space, members book desks and meeting rooms and i bill them

**Spec:**
```
Type:       Web application (coworking management)
Auth:       Email + password for members, admin role for staff
Data model: Member(id, name, email, password_hash, plan)
            Resource(id, name, type, capacity, hourly_rate)
            Booking(id, resource_id -> Resource, member_id -> Member, starts_at, ends_at)
            Invoice(id, member_id -> Member, month, total_cents, status)
Features:   - Book hot desks and meeting rooms by the hour
            - Show room availability on a calendar
            - Include monthly booking credits per plan
            - Generate monthly invoices
            - Let staff manage members and plans
API:        REST
            GET  /resources
            GET  /resources/{id}/availability
            POST /bookings
            DELETE /bookings/{id}
            GET  /invoices
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe Invoicing
```

---

## Example 127

**Intent:**
wiki for my open source project docs, versioned per release

**Spec:**
```
Type:       Web application (documentation site)
Data model: DocVersion(id, version, released_on)
            DocPage(id, version_id -> DocVersion, path, title, body_markdown)
Features:   - Build docs from Markdown files in the repository
            - Keep a separate copy of docs for each release
            - Add a version switcher
            - Search across docs with a search box
            - Deploy automatically on each release tag
Storage:    Static files generated from the Git repository
Tech stack: Docusaurus, Algolia DocSearch, GitHub Actions, GitHub Pages
```

---

## Example 128

**Intent:**
Theres so many scam reviews for contractors in my town. I want a review site where only verified customers who actually hired the plumber or electrician can leave a review, maybe by uploading the invoice?

**Spec:**
```
Type:       Web application (verified review site)
Auth:       Email + password with phone verification
Data model: User(id, name, email, phone, password_hash)
            Contractor(id, business_name, trade, phone, town)
            Review(id, contractor_id -> Contractor, user_id -> User, rating, body, invoice_url, verification_status, created_at)
Features:   - Search contractors by trade and town
            - Submit a review with an invoice photo
            - Hold reviews until an admin verifies the invoice
            - Show a Verified badge on approved reviews
            - Let contractors reply to reviews
API:        REST
            GET  /contractors?trade=&town=
            POST /contractors/{id}/reviews
            PATCH /admin/reviews/{id}
            POST /reviews/{id}/reply
Storage:    PostgreSQL, S3 (invoices, private)
Tech stack: Python, Django, Twilio Verify
```

---

## Example 129

**Intent:**
whiteboard app but for teachers and students in class

**Spec:**
```
Type:       Web application (classroom collaboration)
Auth:       Teacher account, students join with a room code and name
Data model: Teacher(id, email, password_hash)
            Room(id, teacher_id -> Teacher, code, locked)
            StudentBoard(id, room_id -> Room, student_name, snapshot_json)
Features:   - Give each student their own board inside a room
            - Let the teacher see all student boards as thumbnails
            - Push the teacher's board to everyone
            - Lock student boards when time is up
            - Save boards as PNG
API:        REST and WebSocket
            POST /rooms
            POST /rooms/{code}/join
            GET  /rooms/{id}/boards
            WS   /rooms/{id}
Storage:    Redis (live state), PostgreSQL
Tech stack: TypeScript, React, Fabric.js, Node.js, Socket.IO
```

---

## Example 130

**Intent:**
pet adoption website for shelters in my state

**Spec:**
```
Type:       Web application (adoption listings)
Auth:       Email + password for shelter staff, adopters apply without login
Data model: Shelter(id, name, city, email, password_hash)
            Pet(id, shelter_id -> Shelter, name, species, breed, age_months, photos, status)
            Application(id, pet_id -> Pet, applicant_name, email, phone, home_type, message, status)
Features:   - Let shelters list adoptable pets with photos
            - Filter pets by species, age and city
            - Submit an adoption application
            - Let shelters review and approve applications
            - Mark pets as adopted
API:        REST
            GET  /pets?species=&city=
            POST /pets
            POST /pets/{id}/applications
            PATCH /applications/{id}
Storage:    PostgreSQL, Cloudinary (photos)
Tech stack: Node.js, Express, Next.js
```

---

## Example 131

**Intent:**
ai that writes cover letters from my cv and the job ad

**Spec:**
```
Type:       Web application (AI writing assistant)
Auth:       Email + password, credits purchased with Stripe
Data model: User(id, email, password_hash, credits)
            Resume(id, user_id -> User, text, uploaded_at)
            CoverLetter(id, user_id -> User, job_ad_text, letter_text, created_at)
Features:   - Upload a CV as PDF and extract its text
            - Paste a job ad
            - Generate a tailored cover letter with an LLM
            - Edit and regenerate parts of the letter
            - Download the letter as .docx
API:        REST
            POST /resumes
            POST /cover-letters
            POST /cover-letters/{id}/regenerate
            GET  /cover-letters/{id}/download
Storage:    PostgreSQL
Tech stack: Python, FastAPI, pdfplumber, python-docx, Anthropic Claude API
```

---

## Example 132

**Intent:**
forum but with flutter web

**Spec:**
```
Type:       Web application (forum)
Auth:       Firebase Authentication (email + password)
Data model: User(id, displayName, email)
            Category(id, name)
            Thread(id, categoryId -> Category, authorId -> User, title, createdAt)
            Post(id, threadId -> Thread, authorId -> User, body, createdAt)
Features:   - Browse categories and threads
            - Create threads and reply
            - Show new replies live
            - Edit and delete your own posts
Storage:    Firebase Firestore
Tech stack: Flutter (web), Firebase Authentication, Cloud Firestore
```

---

## Example 133

**Intent:**
team okr tracking saas

**Spec:**
```
Type:       Web application (OKR SaaS)
Auth:       Email + password or Google Workspace SSO, organisation accounts
Data model: Organization(id, name)
            User(id, organization_id -> Organization, email, name, role)
            Objective(id, organization_id -> Organization, owner_id -> User, title, quarter)
            KeyResult(id, objective_id -> Objective, title, start_value, target_value, current_value)
            CheckIn(id, key_result_id -> KeyResult, value, note, created_at)
Features:   - Create quarterly objectives with measurable key results
            - Post weekly check-ins with progress
            - Show progress bars and confidence per objective
            - Align team objectives under company objectives
            - Remind owners by email to check in
API:        REST
            GET  /objectives?quarter=
            POST /objectives
            POST /objectives/{id}/key-results
            POST /key-results/{id}/check-ins
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, Angular
```

---

## Example 134

**Intent:**
newsletter for my cycling club

**Spec:**
```
Type:       Web application (newsletter)
Auth:       Admin login for the club secretary
Data model: Subscriber(id, email, name, confirmed, token)
            Campaign(id, subject, body_html, sent_at)
Features:   - Collect sign-ups with a form on the club site
            - Write and send newsletters to confirmed subscribers
            - Include an unsubscribe link in every email
            - Keep an archive of sent newsletters
API:        REST
            POST /subscribe
            GET  /unsubscribe/{token}
            POST /admin/campaigns
            POST /admin/campaigns/{id}/send
Storage:    SQLite
Tech stack: Listmonk (self-hosted), Amazon SES
```

---

## Example 135

**Intent:**
online exam system for my training company, timed tests and anti cheating

**Spec:**
```
Type:       Web application (online exam platform)
Auth:       Email + password for candidates, admin role for examiners
Data model: Candidate(id, name, email, password_hash)
            Exam(id, title, duration_minutes, pass_mark)
            Question(id, exam_id -> Exam, text, options, correct_answer, points)
            Attempt(id, exam_id -> Exam, candidate_id -> Candidate, started_at, submitted_at, score)
            Answer(attempt_id -> Attempt, question_id -> Question, response)
Features:   - Run timed exams with a countdown and auto-submit
            - Shuffle question and answer order per candidate
            - Log tab switches during the exam
            - Grade multiple-choice answers automatically
            - Issue certificates to candidates who pass
API:        REST
            GET  /exams
            POST /exams/{id}/attempts
            PUT  /attempts/{id}/answers
            POST /attempts/{id}/submit
            POST /attempts/{id}/events
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, React
```

---

## Example 136

**Intent:**
something like product hunt for indie games

**Spec:**
```
Type:       Web application (launch directory)
Auth:       Email + password or Twitch sign-in
Data model: User(id, username, email)
            Game(id, maker_id -> User, title, tagline, trailer_url, store_url, launch_date)
            Upvote(user_id -> User, game_id -> Game)
            Comment(id, game_id -> Game, user_id -> User, body)
Features:   - Submit a game launch with trailer and store link
            - Show today's launches ranked by upvotes
            - Comment on launches
            - Show daily and weekly winners
            - Email a weekly digest of top games
API:        REST
            GET  /launches?date=
            POST /games
            POST /games/{id}/upvote
            POST /games/{id}/comments
Storage:    PostgreSQL
Tech stack: Python, Django, Tailwind CSS
```

---

## Example 137

**Intent:**
knowledge base with ai search for our internal policies

**Spec:**
```
Type:       Web application (AI knowledge base)
Auth:       Microsoft Entra ID single sign-on
Data model: Document(id, title, department, file_url, uploaded_at)
            Chunk(id, document_id -> Document, text, embedding)
            Query(id, user_email, question, answer, created_at)
Features:   - Upload policy documents as PDF or Word files
            - Split documents into chunks and store embeddings
            - Answer staff questions with citations to the policy
            - Restrict documents by department
            - Log questions that had no good answer
API:        REST
            POST /documents
            GET  /documents
            POST /ask
            GET  /admin/unanswered
Storage:    PostgreSQL with pgvector, Azure Blob Storage
Tech stack: Python, FastAPI, Azure OpenAI, React
```

---

## Example 138

**Intent:**
Hi im a nurse and in my free time I want to build a place where new nurses can ask experienced ones about stuff anonymously without judgment, like a q and a but safe

**Spec:**
```
Type:       Web application (anonymous Q&A community)
Auth:       Email + password, posts shown under random pseudonyms, licence check for answerers
Data model: User(id, email, password_hash, is_verified_nurse, pseudonym)
            Question(id, user_id -> User, specialty, body, created_at)
            Answer(id, question_id -> Question, user_id -> User, body, helpful_count)
            Report(id, target_id, reason)
Features:   - Ask questions under a random pseudonym
            - Let verified experienced nurses answer
            - Tag questions by specialty
            - Mark answers as helpful
            - Report harmful content to moderators
API:        REST
            GET  /questions?specialty=
            POST /questions
            POST /questions/{id}/answers
            POST /answers/{id}/helpful
            POST /reports
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 139

**Intent:**
shared family recipe book website

**Spec:**
```
Type:       Web application (shared cookbook)
Auth:       Family invite link, email + password
Data model: Family(id, name, invite_code)
            Member(id, family_id -> Family, name, email)
            Recipe(id, family_id -> Family, added_by -> Member, title, ingredients, steps, story, photo_url)
Features:   - Add recipes with a photo and the story behind them
            - Search family recipes by ingredient
            - Scale ingredient amounts by servings
            - Print the whole collection as a PDF book
API:        REST
            GET  /recipes?q=
            POST /recipes
            GET  /recipes/{id}
            GET  /cookbook.pdf
Storage:    PostgreSQL
Tech stack: Python, Flask, WeasyPrint
```

---

## Example 140

**Intent:**
event ticketing website for small concerts

**Spec:**
```
Type:       Web application (event ticketing)
Auth:       Organiser login with email + password, buyers check out as guests
Data model: Organiser(id, name, email, password_hash)
            Event(id, organiser_id -> Organiser, title, venue, starts_at, capacity)
            TicketType(id, event_id -> Event, name, price_cents, quantity)
            Ticket(id, ticket_type_id -> TicketType, buyer_email, qr_code, checked_in)
Features:   - Create events with ticket types and limits
            - Sell tickets with Stripe Checkout
            - Email tickets with QR codes
            - Scan QR codes at the door to check in
            - Show sales per event
API:        REST
            POST /events
            GET  /events/{id}
            POST /events/{id}/checkout
            POST /tickets/{code}/check-in
            GET  /events/{id}/sales
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Stripe
```

---

## Example 141

**Intent:**
make a portfolio for me a web developer, with projects and a contact form, in react

**Spec:**
```
Type:       Web application (portfolio)
Data model: Project(id, title, description, tech_tags, repo_url, live_url, image_url)
Features:   - Show projects as cards with tech tags
            - Filter projects by technology
            - Send contact form messages by email
            - Add a dark mode toggle
            - Link to GitHub and LinkedIn
API:        REST
            POST /api/contact
Storage:    Projects stored in a JSON file
Tech stack: React, Vite, EmailJS, Netlify
```

---

## Example 142

**Intent:**
group buying site where neighbours buy in bulk together to get discounts

**Spec:**
```
Type:       Web application (group buying)
Auth:       Email + password
Data model: User(id, name, email, password_hash, address)
            Deal(id, organiser_id -> User, product, supplier, unit_price, min_quantity, deadline, status)
            Commitment(id, deal_id -> Deal, user_id -> User, quantity, paid)
Features:   - Create a group deal with a minimum quantity and deadline
            - Commit to a quantity and pre-authorise payment
            - Charge everyone only if the minimum is reached
            - Show progress toward the minimum
            - Organise a pickup point for delivery
API:        REST
            GET  /deals
            POST /deals
            POST /deals/{id}/commitments
            POST /deals/{id}/close
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js, Stripe
```

---

## Example 143

**Intent:**
blogging site for kids, safe, teachers approve posts

**Spec:**
```
Type:       Web application (moderated student blog)
Auth:       Teacher accounts with email + password, student accounts created by teachers
Data model: Teacher(id, email, password_hash)
            Classroom(id, teacher_id -> Teacher, name)
            Student(id, classroom_id -> Classroom, username, password_hash)
            BlogPost(id, student_id -> Student, title, body, image_url, status)
            Comment(id, post_id -> BlogPost, student_id -> Student, body, status)
Features:   - Let students write blog posts with images
            - Hold posts and comments until a teacher approves
            - Show only classmates' posts
            - Let parents view their child's blog by a private link
            - Block personal info like emails and addresses
API:        REST
            POST /posts
            GET  /classroom/posts
            PATCH /teacher/posts/{id}
            POST /posts/{id}/comments
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Livewire
```

---

## Example 144

**Intent:**
api-first headless cms

**Spec:**
```
Type:       Web application (headless CMS)
Auth:       Admin login for editors, API tokens for frontends
Data model: ContentType(id, name, fields_json)
            Entry(id, content_type_id -> ContentType, data_json, status, published_at)
            Asset(id, filename, url, mime_type)
            ApiToken(id, name, token_hash, scope)
Features:   - Define content types with custom fields
            - Create and publish entries in an admin UI
            - Upload images and files to a media library
            - Serve published content as JSON to any frontend
            - Trigger a webhook when content is published
API:        REST
            GET  /api/{type}
            GET  /api/{type}/{id}
            POST /admin/content-types
            POST /admin/entries
            POST /admin/assets
Storage:    PostgreSQL, S3 (assets)
Tech stack: Node.js, Strapi
```

---

## Example 145

**Intent:**
ok need a meme sharing site with tags and upvotes

**Spec:**
```
Type:       Web application (image sharing community)
Auth:       Email + password
Data model: User(id, username, email, password_hash)
            Meme(id, user_id -> User, image_url, title, tags, score, created_at)
            Vote(user_id -> User, meme_id -> Meme, value)
            Comment(id, meme_id -> Meme, user_id -> User, body)
Features:   - Upload memes with a title and tags
            - Upvote and downvote memes
            - Sort by hot, new and top
            - Browse by tag
            - Comment on memes
API:        REST
            GET  /memes?sort=&tag=
            POST /memes
            POST /memes/{id}/vote
            POST /memes/{id}/comments
Storage:    PostgreSQL, S3 (images)
Tech stack: Node.js, Express, React
```

---

## Example 146

**Intent:**
platform for nonprofits to post volunteer opportunities and people search by cause

**Spec:**
```
Type:       Web application (volunteer matching)
Auth:       Email + password, roles: organisation and volunteer
Data model: Organisation(id, name, cause, email, password_hash, verified)
            Opportunity(id, organisation_id -> Organisation, title, cause, location, remote, hours_per_week, skills)
            Volunteer(id, name, email, password_hash, interests, location)
            Application(id, opportunity_id -> Opportunity, volunteer_id -> Volunteer, message, status)
Features:   - Post volunteer opportunities with cause, skills and time needed
            - Search opportunities by cause, location and remote
            - Apply to an opportunity with a short message
            - Recommend opportunities based on interests
            - Verify organisations before they post
API:        REST
            GET  /opportunities?cause=&location=
            POST /opportunities
            POST /opportunities/{id}/applications
            PATCH /applications/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Elasticsearch
```

---

## Example 147

**Intent:**
bug tracker so my 4 devs stop losing issues in slack threads

**Spec:**
```
Type:       Web application (issue tracker)
Auth:       Email + password
Data model: User(id, name, email, password_hash)
            Project(id, name, key)
            Issue(id, project_id -> Project, number, title, description, status, priority, assignee_id -> User, reporter_id -> User)
            IssueComment(id, issue_id -> Issue, user_id -> User, body)
Features:   - Create issues with priority and assignee
            - Move issues through Open, In Progress and Closed
            - Comment on issues
            - Filter issues by status, priority and assignee
            - Link commits to issues from GitHub webhooks
API:        REST
            GET  /projects/{key}/issues
            POST /projects/{key}/issues
            PATCH /issues/{id}
            POST /issues/{id}/comments
            POST /webhooks/github
Storage:    PostgreSQL
Tech stack: Go, Gin, Vue.js
```

---

## Example 148

**Intent:**
car enthusiasts forum with build logs

**Spec:**
```
Type:       Web application (forum)
Auth:       Email + password registration
Data model: User(id, username, email, password_hash)
            Car(id, owner_id -> User, make, model, year)
            BuildLog(id, car_id -> Car, title, created_at)
            LogEntry(id, build_log_id -> BuildLog, body, photos, cost, created_at)
            Comment(id, log_entry_id -> LogEntry, user_id -> User, body)
Features:   - Create a build log for each car
            - Add dated entries with photos and parts cost
            - Show total spent on a build
            - Follow build logs and get notified of new entries
            - Comment on entries
API:        REST
            GET  /builds
            POST /cars
            POST /builds
            POST /builds/{id}/entries
            POST /entries/{id}/comments
            POST /builds/{id}/follow
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, HTMX
```

---

## Example 149

**Intent:**
tinder but for finding cofounders

**Spec:**
```
Type:       Web application (cofounder matching)
Auth:       LinkedIn OAuth sign-in
Data model: Founder(id, name, linkedin_url, skills, idea_stage, commitment, location, bio)
            Swipe(id, from_id -> Founder, to_id -> Founder, liked, created_at)
            Match(id, founder_a_id -> Founder, founder_b_id -> Founder, created_at)
            Message(id, match_id -> Match, sender_id -> Founder, body)
Features:   - Create a profile with skills, stage and time commitment
            - Show one profile at a time to like or pass
            - Create a match when both sides like each other
            - Chat with matches
            - Filter by technical or business skills
API:        REST
            GET  /candidates
            POST /swipes
            GET  /matches
            GET  /matches/{id}/messages
            POST /matches/{id}/messages
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 150

**Intent:**
plataforma para professores venderem aulas gravadas, need english spec

**Spec:**
```
Type:       Web application (course platform)
Auth:       Email + password, roles: teacher and student
Data model: Teacher(id, name, email, password_hash, payout_key)
            Course(id, teacher_id -> Teacher, title, price_cents, language)
            Video(id, course_id -> Course, title, url, position)
            Purchase(id, course_id -> Course, student_id -> Student, paid_at)
            Student(id, name, email, password_hash)
Features:   - Upload recorded lessons into courses
            - Sell courses with card or Pix payment
            - Stream videos only to buyers
            - Pay teachers their share monthly
            - Show courses in Portuguese and English
API:        REST
            GET  /courses
            POST /courses
            POST /courses/{id}/videos
            POST /courses/{id}/purchase
            POST /webhooks/payments
Storage:    PostgreSQL, Bunny Stream (video)
Tech stack: Node.js, NestJS, Next.js, Mercado Pago API
```

---

## Example 151

**Intent:**
hello my name is Ahmed, I want site for my city people to find blood donors fast in emergency

**Spec:**
```
Type:       Web application (blood donor directory)
Auth:       Phone number login with SMS one-time code
Data model: Donor(id, name, phone, blood_type, area, last_donated_on, available)
            Request(id, requester_phone, blood_type, hospital, area, needed_by, status)
            Response(id, request_id -> Request, donor_id -> Donor, created_at)
Features:   - Register as a donor with blood type and area
            - Post an urgent blood request
            - Send SMS alerts to matching available donors nearby
            - Hide donors who donated in the last 3 months
            - Let donors respond that they can help
API:        REST
            POST /auth/otp
            POST /donors
            POST /requests
            POST /requests/{id}/responses
            GET  /requests?area=
Storage:    PostgreSQL
Tech stack: Python, Django, Twilio SMS
```

---

## Example 152

**Intent:**
substack alternative self hosted

**Spec:**
```
Type:       Web application (newsletter platform)
Auth:       Email + password for the writer, magic link for readers
Data model: Writer(id, name, email, password_hash)
            Post(id, title, body, audience, published_at)
            Reader(id, email, tier, stripe_customer_id, confirmed)
            Comment(id, post_id -> Post, reader_id -> Reader, body)
Features:   - Publish posts to the web and by email
            - Offer free and paid tiers
            - Let paying readers comment
            - Import subscribers from a CSV
            - Run on one server with Docker Compose
API:        REST
            POST /subscribe
            GET  /p/{slug}
            POST /admin/posts
            POST /admin/import
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Go, HTMX, Stripe, Docker Compose
```

---

## Example 153

**Intent:**
marketplace for renting costumes

**Spec:**
```
Type:       Web application (rental marketplace)
Auth:       Email + password
Data model: User(id, name, email, password_hash, city)
            Costume(id, owner_id -> User, title, size, category, daily_price, deposit, photos)
            Rental(id, costume_id -> Costume, renter_id -> User, start_date, end_date, status, total)
Features:   - List costumes with size, category and photos
            - Check availability for chosen dates
            - Rent a costume and hold a refundable deposit
            - Return the deposit when the owner confirms return
            - Review owners and renters
API:        REST
            GET  /costumes?size=&category=
            POST /costumes
            GET  /costumes/{id}/availability
            POST /rentals
            POST /rentals/{id}/return
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React, Stripe
```

---

## Example 154

**Intent:**
Wiki for recipes my restaurant staff use, with photos of plating

**Spec:**
```
Type:       Web application (internal recipe wiki)
Auth:       Staff login with PIN per employee
Data model: Staff(id, name, pin_hash, role)
            Recipe(id, title, station, ingredients, method, yield, plating_photo_url, updated_at)
            RecipeVersion(id, recipe_id -> Recipe, changed_by -> Staff, body, created_at)
Features:   - Show recipes by kitchen station
            - Show plating photos next to the method
            - Scale recipes to a chosen yield
            - Keep a change history for each recipe
            - Work well on a kitchen tablet
API:        REST
            GET  /recipes?station=
            GET  /recipes/{id}
            PUT  /recipes/{id}
            GET  /recipes/{id}/history
Storage:    SQLite
Tech stack: Python, Flask, Bootstrap
```

---

## Example 155

**Intent:**
jobboard 4 bartenders and waiters in my city

**Spec:**
```
Type:       Web application (hospitality job board)
Auth:       Email + password for venues, workers apply with a phone number
Data model: Venue(id, name, address, email, password_hash)
            Job(id, venue_id -> Venue, role, shift_type, hourly_pay, start_date, status)
            Application(id, job_id -> Job, name, phone, experience, status)
Features:   - Post bar and waiting jobs with pay and shift type
            - Apply in under a minute without an account
            - Show jobs nearest to the worker
            - Text venues when someone applies
            - Close the job when filled
API:        REST
            GET  /jobs
            POST /jobs
            POST /jobs/{id}/apply
            PATCH /jobs/{id}
Storage:    PostgreSQL
Tech stack: Node.js, Express, EJS, Twilio
```

---

## Example 156

**Intent:**
a community-run directory of accessible places (wheelchair ramps, quiet rooms, etc.)

**Spec:**
```
Type:       Web application (accessibility directory)
Auth:       Email + password for contributors
Data model: Place(id, name, address, lat, lng, category)
            AccessibilityReport(id, place_id -> Place, user_id -> User, step_free, accessible_toilet, quiet_space, notes, photo_url, created_at)
            User(id, name, email, password_hash)
Features:   - Search places on a map by accessibility features
            - Add accessibility reports with photos
            - Show the latest report and how old it is
            - Confirm or dispute others' reports
            - Meet WCAG 2.1 AA accessibility guidelines in the site itself
API:        REST
            GET  /places?bbox=&features=
            POST /places
            POST /places/{id}/reports
            POST /reports/{id}/confirm
Storage:    PostgreSQL with PostGIS
Tech stack: Python, Django, Leaflet, OpenStreetMap
```

---

## Example 157

**Intent:**
video course site where i can drip content weekly

**Spec:**
```
Type:       Web application (drip course platform)
Auth:       Email + password
Data model: Student(id, email, password_hash, enrolled_at)
            Module(id, title, unlock_after_days, position)
            Lesson(id, module_id -> Module, title, video_url, worksheet_url)
Features:   - Unlock modules a set number of days after enrollment
            - Email students when a new module unlocks
            - Stream lesson videos
            - Attach downloadable worksheets
            - Show locked modules with their unlock date
API:        REST
            GET  /modules
            GET  /lessons/{id}
            POST /enroll
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Sidekiq, Vimeo
```

---

## Example 158

**Intent:**
ai writing assistant for fiction writers that remembers my characters and world

**Spec:**
```
Type:       Web application (AI writing assistant)
Auth:       Email + password
Data model: User(id, email, password_hash)
            Project(id, user_id -> User, title)
            Character(id, project_id -> Project, name, description)
            Location(id, project_id -> Project, name, description)
            Chapter(id, project_id -> Project, title, text, position)
Features:   - Keep a story bible of characters and locations
            - Write chapters in a distraction-free editor
            - Ask the AI to continue a scene using the story bible as context
            - Flag continuity errors against character details
            - Export the manuscript as .docx
API:        REST
            GET  /projects/{id}
            POST /projects/{id}/characters
            PUT  /chapters/{id}
            POST /chapters/{id}/continue
            POST /chapters/{id}/check
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Anthropic Claude API, TipTap
```

---

## Example 159

**Intent:**
help desk portal for my apartment building, residents report broken stuff

**Spec:**
```
Type:       Web application (maintenance requests)
Auth:       Residents log in with email + password, building manager account
Data model: Resident(id, name, email, password_hash, unit)
            MaintenanceRequest(id, resident_id -> Resident, category, description, photo_url, status, created_at)
            RequestUpdate(id, request_id -> MaintenanceRequest, note, created_at)
Features:   - Report a problem with a category and photo
            - Track request status from Open to Fixed
            - Let the manager post updates on a request
            - Email residents when status changes
            - Post building-wide announcements
API:        REST
            POST /requests
            GET  /me/requests
            PATCH /requests/{id}
            POST /requests/{id}/updates
            POST /announcements
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Blade
```

---

## Example 160

**Intent:**
spec for a reading platform where authors post web novels chapter by chapter and readers comment

**Spec:**
```
Type:       Web application (web fiction platform)
Auth:       Email + password
Data model: User(id, username, email, password_hash)
            Novel(id, author_id -> User, title, synopsis, genre, status)
            Chapter(id, novel_id -> Novel, number, title, body, published_at)
            Comment(id, chapter_id -> Chapter, user_id -> User, body)
            Bookmark(user_id -> User, novel_id -> Novel, last_chapter_id -> Chapter)
Features:   - Publish novels chapter by chapter
            - Schedule chapter releases
            - Comment on chapters
            - Bookmark novels and remember the last read chapter
            - Notify followers of new chapters
API:        REST
            GET  /novels?genre=
            POST /novels
            POST /novels/{id}/chapters
            GET  /chapters/{id}
            POST /chapters/{id}/comments
            PUT  /bookmarks/{novel_id}
Storage:    PostgreSQL
Tech stack: Python, Django, Celery
```

---

## Example 161

**Intent:**
i want site like eventbrite but for free community meetups only

**Spec:**
```
Type:       Web application (meetup platform)
Auth:       Email + password or Google sign-in
Data model: User(id, name, email)
            Group(id, organiser_id -> User, name, city, topic)
            Meetup(id, group_id -> Group, title, starts_at, venue, capacity)
            RSVP(meetup_id -> Meetup, user_id -> User, status)
Features:   - Create groups by topic and city
            - Schedule free meetups with a capacity
            - RSVP and join a waitlist when full
            - Email reminders to attendees
            - Show attendee list to organisers
API:        REST
            GET  /groups?city=
            POST /groups
            POST /groups/{id}/meetups
            POST /meetups/{id}/rsvp
            GET  /meetups/{id}/attendees
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 162

**Intent:**
portfolio for architect

**Spec:**
```
Type:       Web application (portfolio)
Auth:       Admin login for the architect
Data model: Project(id, title, location, year, type, description, images, featured)
Features:   - Show featured projects in a full-screen slideshow
            - Filter projects by type and year
            - Show each project with a photo gallery and plans
            - Edit projects from a simple admin panel
API:        REST
            GET  /projects
            GET  /projects/{id}
            POST /admin/projects
Storage:    Headless CMS (Sanity)
Tech stack: Next.js, Sanity, Vercel
```

---

## Example 163

**Intent:**
forum for players of my mobile game with official dev posts highlighted

**Spec:**
```
Type:       Web application (game community forum)
Auth:       Sign in with the game account via OAuth
Data model: Player(id, game_account_id, username, is_dev)
            Section(id, name)
            Thread(id, section_id -> Section, player_id -> Player, title, pinned)
            Post(id, thread_id -> Thread, player_id -> Player, body, created_at)
Features:   - Sign in with the same account as the game
            - Highlight posts from developers
            - Pin patch notes and announcements
            - Show a dev tracker page listing all developer posts
            - Report bugs in a dedicated section with device info
API:        REST
            GET  /sections
            GET  /threads/{id}
            POST /threads
            POST /threads/{id}/posts
            GET  /dev-tracker
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, Next.js
```

---

## Example 164

**Intent:**
crowdsourced translation site for subtitles

**Spec:**
```
Type:       Web application (crowdsourced translation)
Auth:       Email + password
Data model: User(id, username, email, password_hash, languages)
            Video(id, title, source_language)
            SubtitleLine(id, video_id -> Video, start_ms, end_ms, text)
            Translation(id, line_id -> SubtitleLine, user_id -> User, language, text, votes)
Features:   - Upload a video's subtitle file in SRT format
            - Translate subtitles line by line
            - Vote on the best translation for each line
            - Show translation progress per language
            - Export a finished SRT file
API:        REST
            POST /videos
            GET  /videos/{id}/lines?lang=
            POST /lines/{id}/translations
            POST /translations/{id}/vote
            GET  /videos/{id}/export.srt?lang=
Storage:    PostgreSQL
Tech stack: Python, Django, Vue.js
```

---

## Example 165

**Intent:**
My church choir wants to share sheet music and practice recordings, but only to members, and we need to know who is coming to which rehearsal. Nothing fancy, most of us are in our 60s.

**Spec:**
```
Type:       Web application (choir members area)
Auth:       Email + password, accounts created by the choir director
Data model: Member(id, name, email, password_hash, voice_part)
            Piece(id, title, composer, sheet_pdf_url)
            Recording(id, piece_id -> Piece, voice_part, audio_url)
            Rehearsal(id, date, location)
            Attendance(rehearsal_id -> Rehearsal, member_id -> Member, coming)
Features:   - Show sheet music PDFs for each piece
            - Play practice recordings for each voice part
            - Mark whether you are coming to a rehearsal
            - Show the director who is coming
            - Use big buttons and plain language
API:        REST
            GET  /pieces
            GET  /pieces/{id}/recordings
            GET  /rehearsals
            PUT  /rehearsals/{id}/attendance
Storage:    SQLite, S3 (files)
Tech stack: Python, Django
```

---

## Example 166

**Intent:**
a site for bootcamp grads to show projects and recruiters browse them

**Spec:**
```
Type:       Web application (talent showcase)
Auth:       GitHub sign-in for grads, email + password for recruiters
Data model: Graduate(id, name, github_username, bootcamp, cohort, location, open_to_work)
            Project(id, graduate_id -> Graduate, title, description, demo_url, repo_url, stack)
            Recruiter(id, name, company, email, password_hash)
            Shortlist(recruiter_id -> Recruiter, graduate_id -> Graduate)
Features:   - Let graduates build a profile with projects
            - Let recruiters filter by stack, location and bootcamp
            - Shortlist candidates
            - Contact a graduate through the site
            - Hide graduates who are not open to work
API:        REST
            GET  /graduates?stack=&location=
            POST /projects
            POST /shortlist
            POST /graduates/{id}/contact
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire, GitHub OAuth
```

---

## Example 167

**Intent:**
wiki that my students can edit together for a history project

**Spec:**
```
Type:       Web application (classroom wiki)
Auth:       Teacher account, student accounts created from a class list
Data model: Teacher(id, email, password_hash)
            Student(id, username, password_hash, class_id -> Class)
            Class(id, teacher_id -> Teacher, name)
            Page(id, class_id -> Class, title, body)
            Edit(id, page_id -> Page, student_id -> Student, diff, created_at)
Features:   - Let students create and edit pages together
            - Show which student wrote which part
            - Let the teacher lock pages before grading
            - Show a contribution count per student
            - Embed images and timelines
API:        REST
            GET  /classes/{id}/pages
            POST /pages
            PUT  /pages/{id}
            GET  /pages/{id}/edits
            POST /pages/{id}/lock
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js
```

---

## Example 168

**Intent:**
build a saas where agencies white label a client reporting dashboard

**Spec:**
```
Type:       Web application (white-label SaaS)
Auth:       Email + password for agency staff, client logins per agency
Data model: Agency(id, name, custom_domain, logo_url, brand_color)
            Client(id, agency_id -> Agency, name)
            User(id, agency_id -> Agency, client_id -> Client, email, password_hash, role)
            Report(id, client_id -> Client, title, period, data_json)
Features:   - Serve each agency on its own custom domain with its logo and colours
            - Connect Google Analytics and ad accounts per client
            - Build monthly reports from metric widgets
            - Let clients log in and see only their reports
            - Email reports as PDF on a schedule
API:        REST
            GET  /clients
            POST /clients
            GET  /clients/{id}/reports
            POST /reports
            GET  /reports/{id}/pdf
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma, Google Analytics Data API, Puppeteer
```

---

## Example 169

**Intent:**
hiking trail review site

**Spec:**
```
Type:       Web application (review site)
Auth:       Email + password or Google sign-in
Data model: User(id, username, email)
            Trail(id, name, region, length_km, elevation_gain_m, difficulty, gpx_url)
            Review(id, trail_id -> Trail, user_id -> User, rating, conditions, body, hiked_on, photos)
Features:   - Show trails with distance, elevation and a map from GPX
            - Write reviews with current trail conditions
            - Show the most recent conditions first
            - Filter trails by region, length and difficulty
            - Upload trail photos
API:        REST
            GET  /trails?region=&difficulty=
            GET  /trails/{id}
            POST /trails/{id}/reviews
Storage:    PostgreSQL, S3 (photos and GPX files)
Tech stack: Python, FastAPI, Svelte, Leaflet
```

---

## Example 170

**Intent:**
crowdfunding but people lend money to small farmers and get repaid

**Spec:**
```
Type:       Web application (peer-to-peer microlending)
Auth:       Email + password with identity verification for lenders
Data model: Lender(id, name, email, password_hash, verified, balance_cents)
            Farmer(id, name, region, crop, story)
            Loan(id, farmer_id -> Farmer, amount_cents, term_months, purpose, status)
            LoanShare(id, loan_id -> Loan, lender_id -> Lender, amount_cents)
            Repayment(id, loan_id -> Loan, amount_cents, paid_on)
Features:   - List farmer loans with story and purpose
            - Let lenders fund loans in $25 shares
            - Disburse loans when fully funded
            - Record repayments and credit lenders proportionally
            - Let lenders re-lend or withdraw their balance
API:        REST
            GET  /loans
            POST /loans/{id}/shares
            POST /admin/loans/{id}/repayments
            GET  /me/portfolio
            POST /me/withdraw
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 171

**Intent:**
tool where a team writes standup updates async instead of meetings

**Spec:**
```
Type:       Web application (async standups)
Auth:       Slack OAuth sign-in
Data model: Team(id, slack_team_id, name, standup_time)
            Member(id, team_id -> Team, slack_user_id, name)
            StandupEntry(id, member_id -> Member, date, yesterday, today, blockers)
Features:   - Ask each member their update at a set time in Slack
            - Collect answers in the web app
            - Post a team summary to a Slack channel
            - Highlight blockers
            - Show each person's past updates
API:        REST
            POST /slack/events
            GET  /teams/{id}/standups?date=
            POST /standups
            GET  /members/{id}/history
Storage:    PostgreSQL
Tech stack: Python, Flask, Slack Bolt SDK
```

---

## Example 172

**Intent:**
marketplace connecting home bakers with people ordering birthday cakes

**Spec:**
```
Type:       Web application (custom order marketplace)
Auth:       Email + password, roles: baker and customer
Data model: Baker(id, name, email, password_hash, area, gallery)
            CakeRequest(id, customer_id -> Customer, event_date, servings, flavours, design_notes, reference_image_url, area)
            Quote(id, request_id -> CakeRequest, baker_id -> Baker, price, message, status)
            Customer(id, name, email, password_hash)
Features:   - Post a cake request with date, servings and a reference photo
            - Let nearby bakers send quotes
            - Accept a quote and pay a deposit
            - Show baker galleries and reviews
            - Message about design details
API:        REST
            POST /requests
            GET  /requests?area=
            POST /requests/{id}/quotes
            POST /quotes/{id}/accept
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js, Stripe
```

---

## Example 173

**Intent:**
notion like workspace but simpler

**Spec:**
```
Type:       Web application (collaborative workspace)
Auth:       Email + password or Google sign-in
Data model: User(id, email, name)
            Workspace(id, name, owner_id -> User)
            Page(id, workspace_id -> Workspace, parent_id -> Page, title, icon)
            Block(id, page_id -> Page, type, content_json, position)
Features:   - Create nested pages in a sidebar tree
            - Edit pages made of blocks (text, heading, to-do, image)
            - Reorder blocks by drag and drop
            - Share a workspace with teammates
            - Search across all pages
API:        REST
            GET  /workspaces/{id}/pages
            POST /pages
            GET  /pages/{id}/blocks
            PUT  /pages/{id}/blocks
            GET  /search?q=
Storage:    PostgreSQL
Tech stack: TypeScript, React, BlockNote, Node.js, Express
```

---

## Example 174

**Intent:**
a site for my town's community garden: plot waiting list, shared tool sign-out and a watering rota

**Spec:**
```
Type:       Web application (community garden)
Auth:       Email + password, coordinator role
Data model: Gardener(id, name, email, password_hash, plot_id -> Plot)
            Plot(id, number, size)
            WaitlistEntry(id, name, email, joined_at)
            Tool(id, name, checked_out_by -> Gardener)
            WateringSlot(id, date, gardener_id -> Gardener)
Features:   - Join the plot waiting list and show your position
            - Assign free plots to the next person in line
            - Sign tools in and out
            - Sign up for watering rota days
            - Email a reminder the day before your watering slot
API:        REST
            POST /waitlist
            GET  /plots
            POST /tools/{id}/checkout
            POST /tools/{id}/return
            POST /watering/{id}/claim
Storage:    SQLite
Tech stack: Python, Flask, APScheduler
```

---

## Example 175

**Intent:**
AI summarizer for legal contracts, highlight risky clauses

**Spec:**
```
Type:       Web application (AI contract review)
Auth:       Email + password with two-factor authentication
Data model: User(id, email, password_hash, totp_secret)
            Contract(id, user_id -> User, filename, text, uploaded_at)
            Clause(id, contract_id -> Contract, text, category, risk_level, explanation)
Features:   - Upload contracts as PDF or .docx
            - Summarise the key terms in plain language
            - Detect and highlight risky clauses such as auto-renewal and liability
            - Explain each risk with a short note
            - Delete uploaded files after 30 days
API:        REST
            POST /contracts
            GET  /contracts/{id}
            GET  /contracts/{id}/clauses
            DELETE /contracts/{id}
Storage:    PostgreSQL, S3 (encrypted documents)
Tech stack: Python, FastAPI, pdfplumber, Anthropic Claude API, React
```

---

## Example 176

**Intent:**
i want facebook marketplace but only for my apartment complex

**Spec:**
```
Type:       Web application (private marketplace)
Auth:       Email + password with unit number, approved by the building admin
Data model: Resident(id, name, email, password_hash, unit, approved)
            Item(id, seller_id -> Resident, title, price, photo_url, status, created_at)
            Message(id, item_id -> Item, sender_id -> Resident, body)
Features:   - List items with a photo and price
            - Browse items from neighbours only
            - Message the seller
            - Mark items as free, pending or sold
            - Approve new residents before access
API:        REST
            GET  /items
            POST /items
            PATCH /items/{id}
            POST /items/{id}/messages
            PATCH /admin/residents/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 177

**Intent:**
Book review blog where I review sci-fi books, with star ratings, using wordpress

**Spec:**
```
Type:       Web application (review blog)
Auth:       WordPress admin login
Data model: Review(id, book_title, author, rating, cover_image, body, published_at)
            Genre(id, name)
Features:   - Publish reviews with star ratings and cover images
            - Browse reviews by sub-genre
            - Show top-rated books in a sidebar
            - Add affiliate links to buy each book
            - Allow reader comments
Storage:    MySQL
Tech stack: WordPress, Advanced Custom Fields, Review schema markup plugin
```

---

## Example 178

**Intent:**
interview practice platform where people practice coding interviews with each other

**Spec:**
```
Type:       Web application (peer interview practice)
Auth:       Email + password or GitHub sign-in
Data model: User(id, name, email, timezone, level)
            Slot(id, user_id -> User, starts_at, topic)
            Pairing(id, interviewer_id -> User, candidate_id -> User, starts_at, problem_id -> Problem)
            Problem(id, title, statement, difficulty)
            Feedback(id, pairing_id -> Pairing, from_id -> User, rating, notes)
Features:   - Offer practice slots by time and topic
            - Pair users and swap interviewer and candidate roles
            - Open a shared code editor with video
            - Give the interviewer a problem with hints
            - Leave feedback after each session
API:        REST and WebSocket
            GET  /slots
            POST /slots
            POST /slots/{id}/book
            GET  /pairings/{id}
            POST /pairings/{id}/feedback
            WS   /pairings/{id}/editor
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Monaco Editor, Yjs, WebRTC
```

---

## Example 179

**Intent:**
membership directory for local business association

**Spec:**
```
Type:       Web application (business directory)
Auth:       Email + password for member businesses
Data model: Business(id, name, category, address, phone, website, description, logo_url, membership_paid_until)
            Category(id, name)
            Deal(id, business_id -> Business, title, valid_until)
Features:   - List member businesses by category
            - Let businesses edit their own listing
            - Post member-only deals
            - Hide listings whose membership has lapsed
            - Collect annual dues online
API:        REST
            GET  /businesses?category=
            PUT  /businesses/{id}
            POST /businesses/{id}/deals
            POST /dues/checkout
Storage:    PostgreSQL
Tech stack: PHP, WordPress, Gravity Forms, Stripe
```

---

## Example 180

**Intent:**
game jam website

**Spec:**
```
Type:       Web application (game jam platform)
Auth:       Email + password or itch.io sign-in
Data model: User(id, username, email)
            Jam(id, title, theme, starts_at, ends_at, voting_ends_at)
            Team(id, jam_id -> Jam, name)
            TeamMember(team_id -> Team, user_id -> User)
            Submission(id, team_id -> Team, title, build_url, screenshots)
            Rating(submission_id -> Submission, user_id -> User, category, score)
Features:   - Announce the theme when the jam starts
            - Form teams and submit games before the deadline
            - Rate entries in categories like Fun and Art
            - Show results when voting ends
            - Require voters to rate at least 5 games
API:        REST
            GET  /jams/{id}
            POST /jams/{id}/teams
            POST /teams/{id}/submission
            POST /submissions/{id}/ratings
            GET  /jams/{id}/results
Storage:    PostgreSQL, S3 (builds)
Tech stack: Python, Django, Bootstrap
```

---

## Example 181

**Intent:**
create education platform for my martial arts school, students see belt curriculum videos for their level

**Spec:**
```
Type:       Web application (curriculum platform)
Auth:       Email + password, accounts created by instructors
Data model: Student(id, name, email, password_hash, belt_rank)
            Technique(id, name, belt_rank, video_url, notes)
            Progress(student_id -> Student, technique_id -> Technique, signed_off_by, signed_off_at)
Features:   - Show technique videos for the student's current belt and below
            - Track which techniques an instructor has signed off
            - Show what is left before the next grading
            - Promote students to the next belt
            - Hide higher-belt content
API:        REST
            GET  /techniques
            GET  /me/progress
            POST /students/{id}/signoffs
            POST /students/{id}/promote
Storage:    PostgreSQL, Vimeo
Tech stack: Ruby on Rails, Vimeo API
```

---

## Example 182

**Intent:**
content calendar tool for my social media team

**Spec:**
```
Type:       Web application (content planning tool)
Auth:       Email + password, team invites
Data model: Team(id, name)
            User(id, team_id -> Team, email, name)
            Post(id, team_id -> Team, channel, caption, media_urls, scheduled_for, status, assignee_id -> User)
            Comment(id, post_id -> Post, user_id -> User, body)
Features:   - Plan posts on a monthly calendar by channel
            - Move posts through Draft, Review and Approved
            - Assign posts and comment on drafts
            - Attach images and videos
            - Export the month as a CSV
API:        REST
            GET  /posts?month=
            POST /posts
            PATCH /posts/{id}
            POST /posts/{id}/comments
            GET  /posts/export.csv
Storage:    PostgreSQL, S3 (media)
Tech stack: Node.js, Express, React, FullCalendar
```

---

## Example 183

**Intent:**
gimme a quick spec: anonymous confession board for my school

**Spec:**
```
Type:       Web application (anonymous board)
Data model: Confession(id, body, created_at, status, report_count)
            Reaction(id, confession_id -> Confession, emoji, count)
Features:   - Post confessions without an account
            - Hold every post for moderator approval
            - Filter names of students and bad words
            - React with emoji
            - Remove posts that get many reports
API:        REST
            GET  /confessions
            POST /confessions
            POST /confessions/{id}/react
            POST /confessions/{id}/report
            PATCH /mod/confessions/{id}
Storage:    PostgreSQL
Tech stack: Node.js, Express, Svelte
```

---

## Example 184

**Intent:**
site where people sell handmade jewelry, each seller has own shop page

**Spec:**
```
Type:       Web application (multi-vendor marketplace)
Auth:       Email + password, roles: seller and buyer
Data model: Seller(id, shop_name, slug, email, password_hash, banner_url, stripe_account_id)
            Product(id, seller_id -> Seller, name, material, price, stock, images)
            Order(id, buyer_email, seller_id -> Seller, total, status, shipping_address)
            OrderItem(order_id -> Order, product_id -> Product, quantity)
Features:   - Give each seller a shop page at /shop/{slug}
            - Manage products and stock
            - Split payments between sellers with Stripe Connect
            - Let sellers mark orders as shipped with a tracking number
            - Search across all shops
API:        REST
            GET  /shop/{slug}
            GET  /products?q=
            POST /seller/products
            POST /checkout
            PATCH /seller/orders/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe Connect
```

---

## Example 185

**Intent:**
newsletter digest that collects the best posts from my rss feeds and emails me weekly

**Spec:**
```
Type:       Web application (RSS digest)
Auth:       Email magic-link login
Data model: User(id, email, send_day)
            Feed(id, user_id -> User, url, title)
            Item(id, feed_id -> Feed, title, link, published_at, summary)
            Digest(id, user_id -> User, sent_at)
Features:   - Add RSS and Atom feeds
            - Fetch new items every hour
            - Summarise each item in one sentence with an LLM
            - Email a weekly digest on the chosen day
            - Skip items already sent
API:        REST
            GET  /feeds
            POST /feeds
            DELETE /feeds/{id}
            GET  /digests/preview
Storage:    PostgreSQL
Tech stack: Python, Django, feedparser, Celery, OpenAI API
```

---

## Example 186

**Intent:**
website where my community can request and lend books from each others shelves

**Spec:**
```
Type:       Web application (book lending community)
Auth:       Email + password
Data model: Member(id, name, email, password_hash, area)
            Book(id, owner_id -> Member, isbn, title, author, available)
            LoanRequest(id, book_id -> Book, borrower_id -> Member, status, due_on)
Features:   - Add books by scanning or typing the ISBN
            - Search books owned by people in the community
            - Request to borrow a book
            - Track due dates and send reminders
            - Show each member's lending history
API:        REST
            GET  /books?q=
            POST /books
            POST /books/{id}/requests
            PATCH /requests/{id}
Storage:    PostgreSQL
Tech stack: Node.js, Fastify, React, Google Books API
```

---

## Example 187

**Intent:**
Can I get a spec for a wedding website? Guests RSVP, see schedule, and pick from a gift registry.

**Spec:**
```
Type:       Web application (wedding site)
Auth:       Guests enter a shared password, couple has an admin login
Data model: Guest(id, name, email, party_id -> Party, rsvp, meal_choice, dietary_notes)
            Party(id, name, invite_code)
            ScheduleItem(id, title, starts_at, location)
            Gift(id, name, price, url, claimed_by)
Features:   - RSVP for everyone in your party with meal choices
            - Show the schedule and venue map
            - Claim gifts from the registry so they are not bought twice
            - Show the couple a guest list with RSVP status
            - Export the guest list to CSV
API:        REST
            GET  /parties/{code}
            PUT  /guests/{id}/rsvp
            GET  /schedule
            POST /gifts/{id}/claim
            GET  /admin/guests.csv
Storage:    SQLite
Tech stack: Python, Flask, Bootstrap
```

---

## Example 188

**Intent:**
platform where researchers share datasets and others can cite them

**Spec:**
```
Type:       Web application (dataset repository)
Auth:       ORCID sign-in
Data model: Researcher(id, orcid, name, institution)
            Dataset(id, owner_id -> Researcher, title, description, license, doi, version, published_at)
            DatasetFile(id, dataset_id -> Dataset, filename, size_bytes, checksum, url)
            Download(id, dataset_id -> Dataset, created_at)
Features:   - Upload datasets with metadata and a licence
            - Mint a DOI for each published version
            - Show a ready-made citation in APA and BibTeX
            - Count downloads per dataset
            - Search datasets by keyword and field
API:        REST
            GET  /datasets?q=
            POST /datasets
            POST /datasets/{id}/files
            POST /datasets/{id}/publish
            GET  /datasets/{id}/cite?format=
Storage:    PostgreSQL, S3 (files)
Tech stack: Python, Django, DataCite API
```

---

## Example 189

**Intent:**
i want a reddit for my company, like internal discussions

**Spec:**
```
Type:       Web application (internal discussion board)
Auth:       Okta single sign-on
Data model: Employee(id, okta_id, name, email)
            Space(id, name, description)
            Post(id, space_id -> Space, author_id -> Employee, title, body, score, created_at)
            Comment(id, post_id -> Post, parent_id -> Comment, author_id -> Employee, body)
            Vote(employee_id -> Employee, post_id -> Post, value)
Features:   - Create discussion spaces by team or topic
            - Post and upvote discussions
            - Reply in nested comment threads
            - Allow anonymous posting in a feedback space
            - Send a weekly digest of top posts
API:        REST
            GET  /spaces
            GET  /spaces/{id}/posts
            POST /posts
            POST /posts/{id}/comments
            POST /posts/{id}/vote
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, React, Okta
```

---

## Example 190

**Intent:**
write a spec for a website that lets teachers share lesson plans and others rate them

**Spec:**
```
Type:       Web application (resource sharing community)
Auth:       Email + password
Data model: Teacher(id, name, email, password_hash, subject, grade_level)
            LessonPlan(id, author_id -> Teacher, title, subject, grade_level, duration_minutes, file_url, description)
            Rating(plan_id -> LessonPlan, teacher_id -> Teacher, stars, comment)
            Download(plan_id -> LessonPlan, teacher_id -> Teacher, created_at)
Features:   - Upload lesson plans with subject and grade level
            - Rate and comment on plans
            - Filter by subject, grade and rating
            - Save plans to a personal folder
            - Show download counts to authors
API:        REST
            GET  /plans?subject=&grade=
            POST /plans
            POST /plans/{id}/ratings
            GET  /plans/{id}/download
            POST /folders/{id}/plans
Storage:    PostgreSQL, S3 (files)
Tech stack: Python, Django, Bootstrap
```

---

## Example 191

**Intent:**
website to coordinate meal trains for families with a new baby or illness

**Spec:**
```
Type:       Web application (meal train coordination)
Auth:       Organiser email + password, helpers sign up with name and email only
Data model: MealTrain(id, organiser_email, recipient_name, address, dietary_notes, share_code)
            MealSlot(id, train_id -> MealTrain, date, helper_name, helper_email, dish)
Features:   - Create a meal train with dates and dietary notes
            - Share a link so friends can claim dates
            - Show which dishes are already planned to avoid repeats
            - Email helpers a reminder with the address
            - Hide the address until a slot is claimed
API:        REST
            POST /trains
            GET  /trains/{code}
            POST /trains/{code}/slots/{id}/claim
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Action Mailer
```

---

## Example 192

**Intent:**
stack overflow for lawyers

**Spec:**
```
Type:       Web application (professional Q&A)
Auth:       Email + password, bar number verification for answerers
Data model: User(id, name, email, password_hash, is_verified_lawyer, jurisdiction)
            Question(id, user_id -> User, jurisdiction, practice_area, title, body)
            Answer(id, question_id -> Question, user_id -> User, body, votes)
            Disclaimer(id, text, version)
Features:   - Ask legal questions tagged by jurisdiction and practice area
            - Let only verified lawyers answer
            - Vote answers up
            - Show a "not legal advice" disclaimer on every answer
            - Let lawyers link to their firm profile
API:        REST
            GET  /questions?jurisdiction=&area=
            POST /questions
            POST /questions/{id}/answers
            POST /answers/{id}/vote
Storage:    PostgreSQL
Tech stack: Python, Django, PostgreSQL full-text search
```

---

## Example 193

**Intent:**
freelancer job board, but jobs only from vetted startups

**Spec:**
```
Type:       Web application (curated job board)
Auth:       Email + password for startups, admin vetting
Data model: Startup(id, name, website, funding_stage, email, password_hash, vetted)
            Gig(id, startup_id -> Startup, title, skills, budget, duration_weeks, status)
            Freelancer(id, name, email, portfolio_url)
            Pitch(id, gig_id -> Gig, freelancer_id -> Freelancer, message, rate)
Features:   - Vet startups before they can post
            - Post freelance gigs with budget and skills
            - Let freelancers send short pitches
            - Shortlist and reply to pitches
            - Close gigs when hired
API:        REST
            GET  /gigs
            POST /gigs
            POST /gigs/{id}/pitches
            PATCH /pitches/{id}
            PATCH /admin/startups/{id}
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 194

**Intent:**
lol my d&d group needs a place to schedule sessions cause the group chat is chaos

**Spec:**
```
Type:       Web application (group scheduling)
Auth:       Discord sign-in
Data model: Group(id, name, discord_guild_id)
            Player(id, discord_id, name)
            ProposedDate(id, group_id -> Group, starts_at)
            Availability(proposed_date_id -> ProposedDate, player_id -> Player, answer)
Features:   - Propose several possible session dates
            - Let each player answer yes, maybe or no
            - Highlight the date that works for most players
            - Post the chosen date to the Discord channel
            - Remind everyone the day before
API:        REST
            POST /groups/{id}/dates
            PUT  /dates/{id}/availability
            POST /groups/{id}/confirm
Storage:    PostgreSQL
Tech stack: Node.js, Express, discord.js, React
```

---

## Example 195

**Intent:**
I'm a nutritionist and I'd like a platform where my clients log meals and I comment on them, kind of like a private feed between each client and me.

**Spec:**
```
Type:       Web application (client coaching portal)
Auth:       Email + password, coach invites clients
Data model: Coach(id, name, email, password_hash)
            Client(id, coach_id -> Coach, name, email, password_hash, goals)
            MealLog(id, client_id -> Client, photo_url, description, eaten_at)
            CoachComment(id, meal_log_id -> MealLog, body, created_at)
Features:   - Let clients log meals with a photo and note
            - Show the coach a feed of each client's meals
            - Comment on individual meals
            - Keep each client's feed private to them and the coach
            - Email clients when the coach comments
API:        REST
            POST /meals
            GET  /clients/{id}/meals
            POST /meals/{id}/comments
            POST /clients/invite
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 196

**Intent:**
buy and sell domain names marketplace

**Spec:**
```
Type:       Web application (domain marketplace)
Auth:       Email + password with two-factor authentication
Data model: User(id, email, password_hash, totp_secret)
            DomainListing(id, seller_id -> User, domain, asking_price, min_offer, verified)
            Offer(id, listing_id -> DomainListing, buyer_id -> User, amount, status)
            Transfer(id, listing_id -> DomainListing, buyer_id -> User, escrow_status)
Features:   - List a domain and verify ownership with a DNS TXT record
            - Make and accept offers
            - Hold payment in escrow until the transfer is done
            - Track transfer steps
            - Search domains by keyword and extension
API:        REST
            GET  /domains?q=
            POST /domains
            POST /domains/{id}/verify
            POST /domains/{id}/offers
            PATCH /offers/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Escrow.com API
```

---

## Example 197

**Intent:**
wiki for warhammer lore

**Spec:**
```
Type:       Web application (fan wiki)
Auth:       Email + password
Data model: User(id, username, email, password_hash)
            Entry(id, title, faction, era, body, sources)
            EntryRevision(id, entry_id -> Entry, user_id -> User, body, created_at)
Features:   - Create lore entries tagged by faction and era
            - Cite source books for each entry
            - Show the edit history
            - Browse a timeline of events by era
API:        REST
            GET  /entries?faction=&era=
            POST /entries
            PUT  /entries/{id}
            GET  /timeline
Storage:    PostgreSQL
Tech stack: Python, Flask, SQLAlchemy
```

---

## Example 198

**Intent:**
plz i need saas for hair salons booking with each salon own page and staff calendars

**Spec:**
```
Type:       Web application (multi-tenant booking SaaS)
Auth:       Email + password for salon owners and staff, customers book as guests with phone number
Data model: Salon(id, name, slug, timezone, plan)
            Stylist(id, salon_id -> Salon, name, working_hours_json)
            Service(id, salon_id -> Salon, name, duration_minutes, price)
            Appointment(id, salon_id -> Salon, stylist_id -> Stylist, service_id -> Service, customer_name, customer_phone, starts_at, status)
Features:   - Give each salon a public booking page
            - Show free slots per stylist based on working hours and service length
            - Send SMS confirmations and reminders
            - Let staff see their daily calendar
            - Charge salons a monthly subscription
API:        REST
            GET  /s/{slug}/services
            GET  /s/{slug}/slots?service=&date=
            POST /s/{slug}/appointments
            GET  /staff/calendar
            PATCH /appointments/{id}
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma, Twilio, Stripe Billing
```

---

## Example 199

**Intent:**
blog for my travel adventures with a map of everywhere ive been

**Spec:**
```
Type:       Web application (travel blog)
Auth:       Single author login
Data model: Post(id, title, slug, body, country, lat, lng, cover_url, published_at)
            Photo(id, post_id -> Post, url, caption)
Features:   - Write travel posts with photos
            - Pin each post to a location
            - Show an interactive world map of all posts
            - Colour visited countries
            - Filter posts by country
API:        REST
            GET  /posts
            GET  /posts/{slug}
            GET  /map/points
            POST /admin/posts
Storage:    PostgreSQL, Cloudinary (images)
Tech stack: Astro, Mapbox GL JS, Netlify CMS
```

---

## Example 200

**Intent:**
crowd sourced map of potholes for my city council to fix

**Spec:**
```
Type:       Web application (civic issue reporting)
Auth:       Optional email login for reporters, staff login for the council
Data model: Report(id, category, description, photo_url, lat, lng, status, reporter_email, upvotes, created_at)
            StatusChange(id, report_id -> Report, status, note, changed_at)
Features:   - Report a pothole with a photo and map pin
            - Detect duplicates within 20 metres
            - Upvote existing reports
            - Let council staff update status
            - Email reporters when the issue is fixed
API:        REST
            GET  /reports?bbox=
            POST /reports
            POST /reports/{id}/upvote
            PATCH /admin/reports/{id}
Storage:    PostgreSQL with PostGIS
Tech stack: Python, Django, GeoDjango, Leaflet
```

---

## Example 201

**Intent:**
online course with cohort, discussion and homework peer grading

**Spec:**
```
Type:       Web application (cohort-based course)
Auth:       Email + password
Data model: Cohort(id, name, starts_on)
            Learner(id, cohort_id -> Cohort, name, email, password_hash)
            Week(id, number, content, homework_brief)
            Homework(id, week_id -> Week, learner_id -> Learner, file_url)
            PeerGrade(id, homework_id -> Homework, grader_id -> Learner, score, comment)
            Discussion(id, week_id -> Week, learner_id -> Learner, body)
Features:   - Release weekly content to a cohort
            - Submit homework each week
            - Assign 3 peers to grade each homework
            - Discuss each week in a cohort forum
            - Show learners their average peer grade
API:        REST
            GET  /weeks
            POST /weeks/{id}/homework
            GET  /me/grading-tasks
            POST /homework/{id}/grades
            POST /weeks/{id}/discussion
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire
```

---

## Example 202

**Intent:**
ai chatbot website that helps students study by quizzing them on their notes

**Spec:**
```
Type:       Web application (AI study assistant)
Auth:       Email + password or Google sign-in
Data model: Student(id, email, name)
            NoteSet(id, student_id -> Student, title, text)
            QuizQuestion(id, note_set_id -> NoteSet, question, answer)
            Attempt(id, question_id -> QuizQuestion, student_answer, correct, created_at)
Features:   - Upload notes as text or PDF
            - Generate quiz questions from the notes with an LLM
            - Quiz the student in a chat interface and grade free-text answers
            - Repeat questions the student got wrong
            - Show which topics need more study
API:        REST
            POST /notes
            POST /notes/{id}/questions
            POST /questions/{id}/attempts
            GET  /notes/{id}/weak-topics
Storage:    PostgreSQL
Tech stack: Python, FastAPI, OpenAI API, React
```

---

## Example 203

**Intent:**
im starting a podcast network and need a site with all shows, episodes and a player

**Spec:**
```
Type:       Web application (podcast network site)
Auth:       Admin login for producers
Data model: Show(id, title, slug, description, artwork_url, rss_url)
            Episode(id, show_id -> Show, title, audio_url, duration_seconds, published_at, show_notes)
            Host(id, name, bio, photo_url)
            ShowHost(show_id -> Show, host_id -> Host)
Features:   - List all shows with artwork
            - Import episodes from each show's RSS feed
            - Play episodes in a persistent player that keeps playing between pages
            - Show host bios
            - Search episodes across all shows
API:        REST
            GET  /shows
            GET  /shows/{slug}/episodes
            GET  /search?q=
            POST /admin/shows/{id}/sync
Storage:    PostgreSQL
Tech stack: Next.js, Prisma, rss-parser
```

---

## Example 204

**Intent:**
twitter for scientists to share papers

**Spec:**
```
Type:       Web application (academic social network)
Auth:       ORCID sign-in
Data model: Researcher(id, orcid, name, field)
            Paper(id, doi, title, authors, abstract, published_on)
            Post(id, researcher_id -> Researcher, paper_id -> Paper, comment, created_at)
            Follow(follower_id -> Researcher, followee_id -> Researcher)
Features:   - Share a paper by DOI with metadata fetched automatically
            - Comment on shared papers
            - Follow researchers and see a feed
            - Show trending papers in each field
            - Show a researcher's publication list from ORCID
API:        REST
            GET  /feed
            POST /posts
            GET  /papers/{doi}
            POST /researchers/{id}/follow
            GET  /trending?field=
Storage:    PostgreSQL
Tech stack: Python, Django, Crossref API, ORCID API
```

---

## Example 205

**Intent:**
Hi. I am working in small hotel in Croatia, we want web page where guests can book excursions and boat trips from local partners.

**Spec:**
```
Type:       Web application (activity booking marketplace)
Auth:       Partner login with email + password, guests book as visitors
Data model: Partner(id, name, email, password_hash, commission_rate)
            Activity(id, partner_id -> Partner, title, description, price, duration_hours, max_people)
            Departure(id, activity_id -> Activity, starts_at, seats_left)
            Booking(id, departure_id -> Departure, guest_name, guest_email, people, total, paid)
Features:   - Show excursions and boat trips with photos and prices
            - Book seats on a departure date and pay online
            - Reduce seats left after each booking
            - Send partners the passenger list
            - Show the page in English, German and Croatian
API:        REST
            GET  /activities
            GET  /activities/{id}/departures
            POST /departures/{id}/bookings
            GET  /partner/departures/{id}/passengers
Storage:    PostgreSQL
Tech stack: PHP, Symfony, Stripe, Symfony Translation
```

---

## Example 206

**Intent:**
a commenting/annotation tool where my book club can highlight and comment on a pdf together

**Spec:**
```
Type:       Web application (collaborative annotation)
Auth:       Email + password, invite to a group
Data model: Group(id, name)
            Member(id, group_id -> Group, name, email)
            Document(id, group_id -> Group, title, pdf_url)
            Annotation(id, document_id -> Document, member_id -> Member, page, rects_json, quote, comment, created_at)
            Reply(id, annotation_id -> Annotation, member_id -> Member, body)
Features:   - Upload a PDF to a group
            - Highlight text and add a comment
            - See everyone's highlights in different colours
            - Reply to comments
            - Jump between annotations
API:        REST
            POST /documents
            GET  /documents/{id}/annotations
            POST /documents/{id}/annotations
            POST /annotations/{id}/replies
Storage:    PostgreSQL, S3 (PDFs)
Tech stack: TypeScript, React, PDF.js, Node.js
```

---

## Example 207

**Intent:**
a gofundme for animal shelters

**Spec:**
```
Type:       Web application (crowdfunding)
Auth:       Email + password for shelters with charity number verification
Data model: Shelter(id, name, charity_number, verified, email, password_hash)
            Appeal(id, shelter_id -> Shelter, title, animal_name, story, goal_cents, raised_cents, photo_url)
            Donation(id, appeal_id -> Appeal, donor_email, amount_cents, gift_aid, created_at)
Features:   - Create appeals for specific animals or needs
            - Accept donations with an optional Gift Aid declaration
            - Show progress toward the goal
            - Post updates and photos when an animal is helped
            - Verify charity numbers before payouts
API:        REST
            GET  /appeals
            POST /appeals
            POST /appeals/{id}/donations
            POST /appeals/{id}/updates
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 208

**Intent:**
knowledgebase in notion style for my small team but self hosted, docker please

**Spec:**
```
Type:       Web application (self-hosted knowledge base)
Auth:       Email + password, optional OIDC single sign-on
Data model: User(id, email, name)
            Collection(id, name)
            Document(id, collection_id -> Collection, parent_id -> Document, title, text, updated_at)
            Share(id, document_id -> Document, public_token)
Features:   - Organise documents into collections and nested pages
            - Edit documents in Markdown with slash commands
            - Share a document by public link
            - Search documents by full text
            - Run as Docker containers on our own server
API:        REST
            GET  /api/collections
            POST /api/documents
            GET  /api/documents/{id}
            POST /api/documents/{id}/share
Storage:    PostgreSQL, MinIO (attachments)
Tech stack: Outline (self-hosted), Docker Compose, Redis
```

---

## Example 209

**Intent:**
a site where indie authors swap beta reading

**Spec:**
```
Type:       Web application (beta reader exchange)
Auth:       Email + password
Data model: Author(id, pen_name, email, password_hash, genres, credits)
            Manuscript(id, author_id -> Author, title, genre, word_count, file_url, status)
            ReadSwap(id, manuscript_id -> Manuscript, reader_id -> Author, status, feedback, completed_at)
Features:   - Upload a manuscript with genre and word count
            - Earn credits by beta reading others' work
            - Spend credits to get readers for your manuscript
            - Match readers by genre
            - Submit structured feedback
API:        REST
            POST /manuscripts
            GET  /manuscripts/available?genre=
            POST /manuscripts/{id}/claim
            POST /swaps/{id}/feedback
Storage:    PostgreSQL, S3 (manuscripts)
Tech stack: Node.js, Express, Svelte
```

---

## Example 210

**Intent:**
jobs site for teachers in international schools

**Spec:**
```
Type:       Web application (job board)
Auth:       Email + password, roles: school and teacher
Data model: School(id, name, country, curriculum, email, password_hash)
            Vacancy(id, school_id -> School, subject, start_date, salary, housing_included, closes_on)
            TeacherProfile(id, name, email, password_hash, subjects, qualifications, cv_url)
            Application(vacancy_id -> Vacancy, teacher_id -> TeacherProfile, status)
Features:   - Post vacancies with curriculum, salary and benefits
            - Search jobs by country, subject and curriculum
            - Apply with a stored CV
            - Let schools search teacher profiles
            - Email teachers matching new vacancies
API:        REST
            GET  /vacancies?country=&subject=
            POST /vacancies
            POST /vacancies/{id}/applications
            GET  /teachers?subject=
Storage:    PostgreSQL
Tech stack: Python, Django, Elasticsearch
```

---

## Example 211

**Intent:**
team wiki + task tracker in one with vue

**Spec:**
```
Type:       Web application (wiki and task tracker)
Auth:       Email + password, workspace invites
Data model: Workspace(id, name)
            User(id, email, name)
            Page(id, workspace_id -> Workspace, title, body)
            Task(id, workspace_id -> Workspace, page_id -> Page, title, status, assignee_id -> User, due_date)
Features:   - Write wiki pages for team documentation
            - Create tasks inside pages or on their own
            - Show all tasks on a board by status
            - Link tasks back to the page they came from
            - Search pages and tasks together
API:        REST
            GET  /pages
            POST /pages
            GET  /tasks?status=
            POST /tasks
            PATCH /tasks/{id}
Storage:    PostgreSQL
Tech stack: Vue.js, Pinia, Node.js, Express
```

---

## Example 212

**Intent:**
Platform for musicians to sell beats with licenses

**Spec:**
```
Type:       Web application (beat marketplace)
Auth:       Email + password, roles: producer and artist
Data model: Producer(id, name, email, password_hash, stripe_account_id)
            Beat(id, producer_id -> Producer, title, bpm, key, genre, preview_url, file_url)
            License(id, beat_id -> Beat, type, price, includes_stems)
            Purchase(id, license_id -> License, buyer_email, paid_at, contract_pdf_url)
Features:   - Upload beats with BPM, key and a tagged preview
            - Offer licence types such as MP3 lease, WAV lease and exclusive
            - Generate a PDF licence contract on purchase
            - Remove a beat from sale after an exclusive purchase
            - Filter beats by genre, BPM and key
API:        REST
            GET  /beats?genre=&bpm=
            POST /beats
            POST /licenses/{id}/checkout
            GET  /purchases/{id}/download
Storage:    PostgreSQL, S3 (audio)
Tech stack: Python, Django, Stripe Connect, WeasyPrint
```

---

## Example 213

**Intent:**
i need site where people can upload recipes and other ppl can fork and modify them like github

**Spec:**
```
Type:       Web application (recipe version sharing)
Auth:       Email + password
Data model: User(id, username, email, password_hash)
            Recipe(id, owner_id -> User, forked_from_id -> Recipe, title, created_at)
            RecipeVersion(id, recipe_id -> Recipe, ingredients, steps, message, created_at)
            Star(user_id -> User, recipe_id -> Recipe)
Features:   - Publish recipes with versioned edits and change messages
            - Fork someone else's recipe into your account
            - Show the fork tree of a recipe
            - Compare two versions side by side
            - Star recipes
API:        REST
            GET  /recipes/{id}
            POST /recipes
            POST /recipes/{id}/versions
            POST /recipes/{id}/fork
            GET  /recipes/{id}/diff?a=&b=
Storage:    PostgreSQL
Tech stack: Go, Gin, React
```

---

## Example 214

**Intent:**
fantasy football league site for my mates

**Spec:**
```
Type:       Web application (fantasy sports league)
Auth:       Email + password, league invite code
Data model: League(id, name, invite_code, season)
            Manager(id, league_id -> League, user_id -> User, team_name)
            User(id, email, password_hash)
            Player(id, name, club, position, price)
            Pick(manager_id -> Manager, player_id -> Player, gameweek, is_captain)
            PlayerScore(player_id -> Player, gameweek, points)
Features:   - Pick a squad within a budget each gameweek
            - Choose a captain for double points
            - Import real match stats each gameweek
            - Calculate points and a league table
            - Show head-to-head results
API:        REST
            POST /leagues
            POST /leagues/join
            PUT  /gameweeks/{n}/picks
            GET  /leagues/{id}/table
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React, football-data.org API
```

---

## Example 215

**Intent:**
Simple portfolio + blog for a photographer, built with Gatsby.

**Spec:**
```
Type:       Web application (portfolio and blog)
Data model: Gallery(id, title, slug, images)
            Post(id, title, slug, date, body_markdown, cover)
Features:   - Show galleries in a masonry grid with lightbox
            - Generate optimised images at build time
            - Write blog posts in Markdown
            - Add a contact page with a form
Storage:    Markdown files and images in the repo
Tech stack: Gatsby, gatsby-plugin-image, Netlify Forms
```

---

## Example 216

**Intent:**
im a teacher and i want a forum for my students but i can see everything and approve new posts

**Spec:**
```
Type:       Web application (moderated class forum)
Auth:       Teacher account, students join with a class code
Data model: Teacher(id, email, password_hash)
            Class(id, teacher_id -> Teacher, name, code)
            Student(id, class_id -> Class, name, password_hash)
            Thread(id, class_id -> Class, student_id -> Student, title, body, approved)
            Reply(id, thread_id -> Thread, student_id -> Student, body, approved)
Features:   - Let students start threads and reply
            - Hold new posts until the teacher approves them
            - Let the teacher pin and lock threads
            - Show the teacher a participation count per student
            - Turn off posting outside school hours
API:        REST
            GET  /classes/{id}/threads
            POST /threads
            POST /threads/{id}/replies
            PATCH /teacher/posts/{id}
Storage:    PostgreSQL
Tech stack: Python, Flask, HTMX
```

---

## Example 217

**Intent:**
marketplace for tattoo artists flash designs, clients reserve a design

**Spec:**
```
Type:       Web application (flash design marketplace)
Auth:       Email + password, roles: artist and client
Data model: Artist(id, name, studio, city, email, password_hash)
            FlashDesign(id, artist_id -> Artist, image_url, size_cm, price, status)
            Reservation(id, design_id -> FlashDesign, client_id -> Client, deposit_paid, appointment_at)
            Client(id, name, email, password_hash)
Features:   - Post available flash designs with size and price
            - Reserve a design with a deposit
            - Remove reserved designs from the gallery
            - Book an appointment time with the artist
            - Filter designs by city and style
API:        REST
            GET  /designs?city=
            POST /designs
            POST /designs/{id}/reserve
            PATCH /reservations/{id}
Storage:    PostgreSQL, Cloudinary
Tech stack: Node.js, NestJS, React, Stripe
```

---

## Example 218

**Intent:**
project management for construction company, sites, tasks, photos, daily reports

**Spec:**
```
Type:       Web application (construction project management)
Auth:       Email + password, roles: manager and site supervisor
Data model: Site(id, name, address, start_date)
            User(id, name, email, password_hash, role)
            Task(id, site_id -> Site, title, status, due_date, assignee_id -> User)
            DailyReport(id, site_id -> Site, author_id -> User, date, weather, workers_on_site, notes)
            Photo(id, report_id -> DailyReport, url, caption)
Features:   - Track tasks per site with due dates
            - File a daily report with weather, headcount and notes
            - Attach site photos to reports from a phone
            - Show managers a timeline of reports per site
            - Export reports as PDF
API:        REST
            GET  /sites
            GET  /sites/{id}/tasks
            POST /sites/{id}/reports
            POST /reports/{id}/photos
            GET  /reports/{id}/pdf
Storage:    PostgreSQL, S3 (photos)
Tech stack: C#, ASP.NET Core, React
```

---

## Example 219

**Intent:**
forum for mental health peer support, has to be safe

**Spec:**
```
Type:       Web application (peer support forum)
Auth:       Email + password, anonymous display names
Data model: User(id, email, password_hash, display_name, role)
            Space(id, name, description)
            Post(id, space_id -> Space, user_id -> User, body, content_warning, created_at, status)
            Reply(id, post_id -> Post, user_id -> User, body)
            Flag(id, post_id -> Post, reason)
Features:   - Post under an anonymous display name
            - Add content warnings that blur sensitive posts
            - Detect crisis language and show helpline numbers
            - Let trained moderators review flagged posts
            - Disable public like counts to reduce comparison
API:        REST
            GET  /spaces/{id}/posts
            POST /posts
            POST /posts/{id}/replies
            POST /posts/{id}/flag
            GET  /mod/flags
Storage:    PostgreSQL
Tech stack: Python, Django, React
```

---

## Example 220

**Intent:**
make me a reading list sharing site

**Spec:**
```
Type:       Web application (reading lists)
Auth:       Email + password
Data model: User(id, username, email, password_hash)
            ReadingList(id, user_id -> User, title, description, is_public)
            ListItem(id, list_id -> ReadingList, url, title, note, position)
Features:   - Create public or private reading lists
            - Add articles, books and links with notes
            - Reorder items
            - Follow other people's lists
API:        REST
            GET  /lists
            POST /lists
            POST /lists/{id}/items
            PATCH /items/{id}
Storage:    SQLite
Tech stack: Python, Flask, Alpine.js
```

---

## Example 221

**Intent:**
a website where people post local lost and found pets

**Spec:**
```
Type:       Web application (lost and found pets)
Auth:       Email + password
Data model: User(id, name, email, phone, password_hash)
            PetReport(id, user_id -> User, type, species, description, photo_url, lat, lng, seen_at, status)
Features:   - Post lost or found pet reports with a photo and location
            - Show reports on a map
            - Match lost and found reports by species and distance
            - Alert users with an email when a matching report is posted
            - Mark a report as reunited
API:        REST
            GET  /reports?type=&near=
            POST /reports
            PATCH /reports/{id}
            GET  /reports/{id}/matches
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: Node.js, Express, React, Leaflet
```

---

## Example 222

**Intent:**
create spec, website for selling tickets to my school theatre play, seat selection

**Spec:**
```
Type:       Web application (seated ticketing)
Auth:       Admin login for the drama teacher, buyers check out as guests
Data model: Performance(id, title, starts_at)
            Seat(id, row, number, section)
            SeatBooking(performance_id -> Performance, seat_id -> Seat, order_id -> Order)
            Order(id, buyer_name, buyer_email, total_cents, paid_at)
Features:   - Show a seat map for each performance
            - Hold selected seats for 10 minutes during checkout
            - Take payment online
            - Email tickets with seat numbers
            - Print a door list for each performance
API:        REST
            GET  /performances
            GET  /performances/{id}/seats
            POST /performances/{id}/hold
            POST /orders
            GET  /admin/performances/{id}/door-list
Storage:    PostgreSQL, Redis (seat holds)
Tech stack: Node.js, Express, React, Stripe
```

---

## Example 223

**Intent:**
help center for my saas with articles in 5 languages

**Spec:**
```
Type:       Web application (multilingual help center)
Auth:       Admin login for support staff
Data model: Article(id, category_id -> Category, slug, updated_at)
            ArticleTranslation(id, article_id -> Article, locale, title, body, status)
            Category(id, slug, position)
Features:   - Write articles once and add translations for 5 languages
            - Show the right language based on the browser
            - Mark translations that are out of date when the source changes
            - Search within the chosen language
            - Fall back to English when a translation is missing
API:        REST
            GET  /{locale}/articles
            GET  /{locale}/articles/{slug}
            POST /admin/articles
            PUT  /admin/articles/{id}/translations/{locale}
Storage:    PostgreSQL
Tech stack: TypeScript, Nuxt, Nuxt i18n, Meilisearch
```

---

## Example 224

**Intent:**
hackathon management site

**Spec:**
```
Type:       Web application (hackathon platform)
Auth:       Email + password or GitHub sign-in
Data model: Hackathon(id, name, starts_at, ends_at)
            Participant(id, name, email, skills)
            Team(id, hackathon_id -> Hackathon, name, idea)
            TeamMember(team_id -> Team, participant_id -> Participant)
            Project(id, team_id -> Team, title, repo_url, demo_url)
            Score(project_id -> Project, judge_id -> Participant, criterion, value)
Features:   - Register participants and form teams
            - Help solo participants find a team by skill
            - Submit projects with repo and demo links
            - Let judges score projects by criteria
            - Show final rankings
API:        REST
            POST /hackathons/{id}/register
            POST /teams
            POST /teams/{id}/join
            POST /teams/{id}/project
            POST /projects/{id}/scores
            GET  /hackathons/{id}/rankings
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Next.js
```

---

## Example 225

**Intent:**
freecodecamp style platform but for learning sql

**Spec:**
```
Type:       Web application (interactive learning platform)
Auth:       Email + password or GitHub sign-in
Data model: Learner(id, email, name)
            Lesson(id, title, explanation, schema_sql, expected_result_json, position)
            Attempt(id, learner_id -> Learner, lesson_id -> Lesson, query, correct, created_at)
Features:   - Explain one SQL concept per lesson
            - Run the learner's query against a sample database in the browser
            - Compare the result with the expected rows
            - Unlock the next lesson when correct
            - Show a progress map of all lessons
API:        REST
            GET  /lessons
            GET  /lessons/{id}
            POST /lessons/{id}/attempts
            GET  /me/progress
Storage:    PostgreSQL (progress), SQLite in the browser (exercises)
Tech stack: TypeScript, React, sql.js, Node.js
```

---

## Example 226

**Intent:**
website for local farmers market vendors to post whats available this week and people preorder

**Spec:**
```
Type:       Web application (farmers market preorders)
Auth:       Email + password for vendors, customers order with email
Data model: Vendor(id, name, email, password_hash, stall_number)
            Product(id, vendor_id -> Vendor, name, unit, price, quantity_this_week)
            Preorder(id, customer_name, customer_email, market_date, status)
            PreorderItem(preorder_id -> Preorder, product_id -> Product, quantity)
Features:   - Let vendors post this week's produce and quantities
            - Let customers preorder from several vendors in one basket
            - Pay online or at pickup
            - Send each vendor their pickup list
            - Reset quantities every week
API:        REST
            GET  /products?week=
            POST /vendor/products
            POST /preorders
            GET  /vendor/pickup-list
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 227

**Intent:**
i want a collaborative playlist website for parties

**Spec:**
```
Type:       Web application (collaborative playlist)
Auth:       Host signs in with Spotify, guests join with a party code
Data model: Party(id, host_spotify_id, code, playlist_id)
            QueuedTrack(id, party_id -> Party, spotify_track_id, title, added_by, votes)
            Vote(track_id -> QueuedTrack, guest_id, value)
Features:   - Create a party linked to the host's Spotify
            - Let guests search songs and add them
            - Upvote and downvote queued songs
            - Play the highest voted song next
            - Limit how many songs each guest can add
API:        REST and WebSocket
            POST /parties
            POST /parties/{code}/tracks
            POST /tracks/{id}/vote
            WS   /parties/{code}
Storage:    Redis
Tech stack: Node.js, Express, Spotify Web API, React
```

---

## Example 228

**Intent:**
event volunteer signup for a music festival with roles and training

**Spec:**
```
Type:       Web application (festival volunteer management)
Auth:       Email + password
Data model: Volunteer(id, name, email, password_hash, phone, tshirt_size)
            Role(id, name, description, required_training)
            Shift(id, role_id -> Role, starts_at, ends_at, slots)
            ShiftSignup(shift_id -> Shift, volunteer_id -> Volunteer)
            TrainingCompletion(volunteer_id -> Volunteer, role_id -> Role, completed_at)
Features:   - Apply as a volunteer with role preferences
            - Complete online training before taking shifts
            - Sign up for a minimum number of shifts to earn a free ticket
            - Check volunteers in on site with a QR code
            - Message all volunteers in a role
API:        REST
            POST /volunteers
            GET  /roles
            POST /roles/{id}/training/complete
            POST /shifts/{id}/signup
            POST /checkin/{qr}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stimulus
```

---

## Example 229

**Intent:**
cms for a newspaper

**Spec:**
```
Type:       Web application (newsroom CMS)
Auth:       Email + password, roles: reporter, editor, admin
Data model: Staff(id, name, email, password_hash, role)
            Article(id, section, headline, standfirst, body, byline_id -> Staff, status, published_at)
            Image(id, url, caption, credit)
            ArticleImage(article_id -> Article, image_id -> Image)
Features:   - Write and edit articles with an editorial workflow
            - Schedule articles and set a homepage priority
            - Manage a photo library with credits
            - Show breaking news banners
            - Publish to the website and AMP pages
API:        REST
            GET  /articles?section=
            POST /articles
            PATCH /articles/{id}
            POST /articles/{id}/publish
            POST /images
Storage:    PostgreSQL, S3 (images)
Tech stack: Python, Django, Wagtail
```

---

## Example 230

**Intent:**
Can you design a SaaS where small landlords track rent payments and tenants can log in to see what they owe?

**Spec:**
```
Type:       Web application (property management SaaS)
Auth:       Email + password, roles: landlord and tenant
Data model: Landlord(id, name, email, password_hash)
            Property(id, landlord_id -> Landlord, address)
            Tenancy(id, property_id -> Property, tenant_id -> Tenant, monthly_rent, due_day, start_date)
            Tenant(id, name, email, password_hash)
            RentPayment(id, tenancy_id -> Tenancy, period, amount, paid_on)
Features:   - Add properties and tenancies
            - Generate monthly rent charges
            - Record payments and show arrears
            - Let tenants see their balance and payment history
            - Email tenants a reminder before rent is due
API:        REST
            GET  /properties
            POST /tenancies
            GET  /tenancies/{id}/ledger
            POST /tenancies/{id}/payments
            GET  /tenant/me
Storage:    PostgreSQL
Tech stack: Laravel, Livewire, MySQL
```

---

## Example 231

**Intent:**
AI tool that turns a blog post into tweets and a linkedin post

**Spec:**
```
Type:       Web application (AI content repurposing)
Auth:       Email + password
Data model: User(id, email, password_hash)
            Source(id, user_id -> User, url, text)
            Output(id, source_id -> Source, platform, content, created_at)
Features:   - Import a blog post from a URL or pasted text
            - Generate a tweet thread, a LinkedIn post and a short summary
            - Keep each output within platform length limits
            - Regenerate one output with a different tone
            - Copy outputs with one click
API:        REST
            POST /sources
            POST /sources/{id}/generate
            POST /outputs/{id}/regenerate
            GET  /sources
Storage:    PostgreSQL
Tech stack: Python, FastAPI, OpenAI API, Svelte
```

---

## Example 232

**Intent:**
mentors and mentees in our company matched for 6 month programmes

**Spec:**
```
Type:       Web application (internal mentoring programme)
Auth:       Google Workspace single sign-on
Data model: Employee(id, name, email, department, seniority)
            Application(id, employee_id -> Employee, role, goals, skills)
            Pairing(id, mentor_id -> Employee, mentee_id -> Employee, cohort, status)
            Meeting(id, pairing_id -> Pairing, date, notes)
Features:   - Apply as mentor or mentee with goals and skills
            - Suggest pairings that avoid same-team matches
            - Let admins confirm pairings for a 6-month cohort
            - Log meetings and notes
            - Collect feedback at the end of the cohort
API:        REST
            POST /applications
            GET  /admin/suggestions
            POST /admin/pairings
            POST /pairings/{id}/meetings
            POST /pairings/{id}/feedback
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 233

**Intent:**
wedding vendors directory with reviews and quote requests

**Spec:**
```
Type:       Web application (vendor directory)
Auth:       Email + password, roles: couple and vendor
Data model: Vendor(id, name, category, region, price_range, email, password_hash, gallery)
            Couple(id, names, email, password_hash, wedding_date)
            QuoteRequest(id, vendor_id -> Vendor, couple_id -> Couple, guests, message, status)
            Review(id, vendor_id -> Vendor, couple_id -> Couple, rating, body)
Features:   - Browse vendors by category, region and price range
            - Send quote requests with the wedding date
            - Let vendors reply to requests from a dashboard
            - Review vendors after the wedding
            - Save favourite vendors
API:        REST
            GET  /vendors?category=&region=
            POST /vendors/{id}/quotes
            PATCH /quotes/{id}
            POST /vendors/{id}/reviews
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, Nuxt
```

---

## Example 234

**Intent:**
need forum 4 my minecraft server players, link there minecraft name

**Spec:**
```
Type:       Web application (game server forum)
Auth:       Email + password, Minecraft account linked by an in-game verification code
Data model: User(id, username, email, password_hash, minecraft_uuid, rank)
            Category(id, name)
            Thread(id, category_id -> Category, user_id -> User, title)
            Post(id, thread_id -> Thread, user_id -> User, body)
            Appeal(id, user_id -> User, reason, status)
Features:   - Link a forum account to a Minecraft name with a code typed in game
            - Show in-game ranks next to usernames
            - Post threads in categories like Announcements and Suggestions
            - Submit ban appeals for staff to review
            - Show the server's online player count
API:        REST
            POST /link/verify
            GET  /categories/{id}/threads
            POST /threads
            POST /threads/{id}/posts
            POST /appeals
Storage:    MySQL
Tech stack: PHP, Laravel, Minecraft server query protocol
```

---

## Example 235

**Intent:**
sell my notes to other students site

**Spec:**
```
Type:       Web application (study notes marketplace)
Auth:       University email registration
Data model: Student(id, name, uni_email, password_hash, university, payout_email)
            Notes(id, seller_id -> Student, course_code, title, preview_url, file_url, price)
            Purchase(id, notes_id -> Notes, buyer_id -> Student, paid_at)
            Rating(notes_id -> Notes, buyer_id -> Student, stars)
Features:   - Upload notes as PDF with a 2-page free preview
            - Search notes by university and course code
            - Buy and download notes
            - Rate notes after buying
            - Pay sellers 70% of each sale monthly
API:        REST
            GET  /notes?uni=&course=
            POST /notes
            POST /notes/{id}/purchase
            GET  /notes/{id}/download
            POST /notes/{id}/ratings
Storage:    PostgreSQL, S3 (PDFs)
Tech stack: Node.js, Express, React, Stripe
```

---

## Example 236

**Intent:**
blog engine in rust

**Spec:**
```
Type:       Web application (blog)
Auth:       Admin login with a single password (Argon2 hashed)
Data model: Post(id, title, slug, body_markdown, html_cache, tags, published_at, draft)
Features:   - Write posts in Markdown and render to HTML
            - Highlight code blocks
            - List posts by tag
            - Generate RSS and sitemap.xml
            - Serve pages fast with caching
API:        REST
            GET  /posts
            GET  /posts/{slug}
            GET  /tags/{tag}
            POST /admin/posts
            GET  /rss.xml
Storage:    SQLite
Tech stack: Rust, Axum, SQLx, pulldown-cmark, Tera templates
```

---

## Example 237

**Intent:**
my wife is a yoga teacher and wants clients to buy class packs (like 10 classes) and book into her weekly classes using credits

**Spec:**
```
Type:       Web application (class pack booking)
Auth:       Email + password for clients, admin login for the teacher
Data model: Client(id, name, email, password_hash, credits)
            ClassPack(id, name, credits, price_cents, valid_days)
            PackPurchase(id, client_id -> Client, pack_id -> ClassPack, expires_on)
            YogaClass(id, title, starts_at, capacity)
            Booking(class_id -> YogaClass, client_id -> Client, status)
Features:   - Sell class packs with an expiry date
            - Book a class using one credit
            - Refund the credit when cancelled more than 12 hours before
            - Show a waitlist when a class is full
            - Show the teacher today's attendee list
API:        REST
            GET  /packs
            POST /packs/{id}/buy
            GET  /classes
            POST /classes/{id}/book
            DELETE /classes/{id}/book
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 238

**Intent:**
build social app for runners in svelte where they post runs and give kudos

**Spec:**
```
Type:       Web application (fitness social network)
Auth:       Email + password or Strava sign-in
Data model: Runner(id, name, email, strava_id)
            Run(id, runner_id -> Runner, distance_km, duration_seconds, route_polyline, date, notes)
            Kudos(run_id -> Run, runner_id -> Runner)
            Follow(follower_id -> Runner, followee_id -> Runner)
Features:   - Post runs manually or import them from Strava
            - Show a feed of runs from people you follow
            - Give kudos and comment on runs
            - Show weekly distance on the profile
            - Draw each run's route on a map
API:        REST
            GET  /feed
            POST /runs
            POST /runs/{id}/kudos
            POST /runners/{id}/follow
            POST /import/strava
Storage:    PostgreSQL
Tech stack: SvelteKit, Drizzle ORM, Strava API, Leaflet
```

---

## Example 239

**Intent:**
plattform for ehrenamt in my village, people say what they can help with (shopping, garden) and old people ask for help. sorry for bad english

**Spec:**
```
Type:       Web application (neighbourhood help exchange)
Auth:       Email + password or phone number with SMS code
Data model: Helper(id, name, phone, email, can_help_with)
            HelpRequest(id, requester_name, phone, category, description, needed_on, status, helper_id -> Helper)
Features:   - Let helpers register what they can help with
            - Let older people or relatives post a help request
            - Notify matching helpers by SMS
            - Let a helper accept a request
            - Show the page in German and English
API:        REST
            POST /helpers
            POST /requests
            GET  /requests?category=
            POST /requests/{id}/accept
Storage:    PostgreSQL
Tech stack: Python, Django, Twilio, Django i18n
```

---

## Example 240

**Intent:**
wikipedia but for my family history

**Spec:**
```
Type:       Web application (family history wiki)
Auth:       Family members invited by email
Data model: Person(id, full_name, born_on, died_on, birthplace, biography, photo_url)
            Relationship(id, person_a_id -> Person, person_b_id -> Person, type)
            Story(id, person_id -> Person, title, body, author_id -> Member)
            Member(id, name, email, password_hash)
Features:   - Create a page for each ancestor with dates and photos
            - Link parents, children and spouses
            - Show an interactive family tree
            - Add stories and old documents to a person
            - Import data from a GEDCOM file
API:        REST
            GET  /people/{id}
            POST /people
            POST /relationships
            POST /people/{id}/stories
            POST /import/gedcom
            GET  /tree
Storage:    PostgreSQL, S3 (documents)
Tech stack: Python, Django, python-gedcom, D3.js
```

---

## Example 241

**Intent:**
q and a website for car mechanics questions where verified mechanics answer

**Spec:**
```
Type:       Web application (expert Q&A)
Auth:       Email + password, mechanics verified with a certification upload
Data model: User(id, name, email, password_hash, is_mechanic, verified)
            Question(id, user_id -> User, car_make, car_model, year, title, body, photos)
            Answer(id, question_id -> Question, user_id -> User, body, accepted)
Features:   - Ask questions with car make, model and year
            - Attach photos or a short video of the problem
            - Show a Verified Mechanic badge on answers
            - Accept the answer that fixed it
            - Search past questions for the same car
API:        REST
            GET  /questions?make=&model=
            POST /questions
            POST /questions/{id}/answers
            POST /answers/{id}/accept
Storage:    PostgreSQL, S3 (media)
Tech stack: Ruby on Rails, Active Storage
```

---

## Example 242

**Intent:**
real estate listings site

**Spec:**
```
Type:       Web application (property listings)
Auth:       Email + password for agents, buyers can save searches with an account
Data model: Agent(id, name, agency, email, password_hash)
            Listing(id, agent_id -> Agent, title, price, bedrooms, bathrooms, area_m2, address, lat, lng, type, status)
            ListingPhoto(id, listing_id -> Listing, url, position)
            SavedSearch(id, user_email, filters_json)
Features:   - Post property listings with photos
            - Search by price, bedrooms, area and type
            - Show listings on a map
            - Contact the agent about a listing
            - Email users when a new listing matches their saved search
API:        REST
            GET  /listings?min_price=&bedrooms=
            POST /listings
            GET  /listings/{id}
            POST /listings/{id}/enquiries
            POST /saved-searches
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: Python, Django, Mapbox
```

---

## Example 243

**Intent:**
i wanna make a site where streamers can get clips voted by fans for a weekly highlight video

**Spec:**
```
Type:       Web application (clip voting)
Auth:       Twitch sign-in
Data model: Streamer(id, twitch_id, name)
            Clip(id, streamer_id -> Streamer, twitch_clip_id, title, submitted_by, week)
            Vote(clip_id -> Clip, viewer_twitch_id)
Features:   - Let fans submit Twitch clips for a streamer
            - Vote once per clip per viewer
            - Show the weekly top 10 clips
            - Let the streamer download the top clips list
            - Reset voting every Monday
API:        REST
            GET  /streamers/{id}/clips?week=
            POST /streamers/{id}/clips
            POST /clips/{id}/vote
            GET  /streamers/{id}/top
Storage:    PostgreSQL
Tech stack: Node.js, Express, Twitch API, React
```

---

## Example 244

**Intent:**
i'm a bit lost, i want an education website for my village school kids to do homework online, the teacher post homework and kids send photos of their work

**Spec:**
```
Type:       Web application (homework submission)
Auth:       Teacher login with email + password, children log in with a simple picture password
Data model: Teacher(id, name, email, password_hash)
            Class(id, teacher_id -> Teacher, name)
            Child(id, class_id -> Class, first_name, picture_password)
            Homework(id, class_id -> Class, title, instructions, due_on)
            Submission(id, homework_id -> Homework, child_id -> Child, photo_url, teacher_comment)
Features:   - Post homework with instructions and a due date
            - Let children upload a photo of their work
            - Let the teacher comment with a sticker or note
            - Show which children have not handed in
            - Work well on cheap tablets and phones
API:        REST
            GET  /homework
            POST /homework
            POST /homework/{id}/submissions
            PATCH /submissions/{id}
Storage:    SQLite, local file storage (photos)
Tech stack: PHP, Laravel, Blade
```

---

## Example 245

**Intent:**
newsletter tool in node

**Spec:**
```
Type:       Web application (newsletter tool)
Auth:       Email + password for the sender
Data model: List(id, name)
            Subscriber(id, list_id -> List, email, status, confirm_token)
            Campaign(id, list_id -> List, subject, html, scheduled_at, sent_at)
            Event(id, campaign_id -> Campaign, subscriber_id -> Subscriber, type, created_at)
Features:   - Manage several subscriber lists
            - Send campaigns now or on a schedule
            - Track opens with a pixel and clicks with redirects
            - Handle bounces and unsubscribes
            - Show campaign stats
API:        REST
            POST /lists/{id}/subscribe
            GET  /confirm/{token}
            POST /campaigns
            POST /campaigns/{id}/send
            GET  /t/open/{id}
            GET  /t/click/{id}
Storage:    PostgreSQL
Tech stack: Node.js, Express, BullMQ, Amazon SES
```

---

## Example 246

**Intent:**
second hand baby stuff marketplace

**Spec:**
```
Type:       Web application (marketplace)
Auth:       Email + password
Data model: Parent(id, name, email, password_hash, city)
            Item(id, seller_id -> Parent, title, category, age_range, condition, price, photos, status)
            Conversation(id, item_id -> Item, buyer_id -> Parent)
            Message(id, conversation_id -> Conversation, sender_id -> Parent, body)
Features:   - List items by category like Strollers, Clothes and Toys
            - Filter by child age range and city
            - Chat with the seller
            - Show recall warnings for car seats and cribs
            - Mark items as sold
API:        REST
            GET  /items?category=&age=
            POST /items
            POST /items/{id}/conversations
            POST /conversations/{id}/messages
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 247

**Intent:**
Our nonprofit needs a grant application portal, organisations apply online and our panel scores them.

**Spec:**
```
Type:       Web application (grant application portal)
Auth:       Email + password, roles: applicant, reviewer, admin
Data model: Organisation(id, name, registration_number, contact_email)
            Round(id, name, opens_at, closes_at, budget)
            ApplicationForm(id, round_id -> Round, organisation_id -> Organisation, answers_json, budget_requested, status)
            Score(id, application_id -> ApplicationForm, reviewer_id -> User, criterion, value, comment)
            User(id, email, password_hash, role)
Features:   - Open funding rounds with deadlines
            - Let organisations save drafts and submit applications
            - Assign applications to reviewers
            - Score applications against criteria
            - Rank applications by average score
API:        REST
            GET  /rounds
            POST /applications
            PUT  /applications/{id}
            POST /applications/{id}/submit
            POST /applications/{id}/scores
            GET  /rounds/{id}/ranking
Storage:    PostgreSQL, S3 (attachments)
Tech stack: C#, ASP.NET Core MVC
```

---

## Example 248

**Intent:**
tiktok style feed but for short cooking videos

**Spec:**
```
Type:       Web application (short video platform)
Auth:       Email + password or Google sign-in
Data model: User(id, username, email)
            Video(id, user_id -> User, video_url, caption, recipe_text, created_at)
            Like(user_id -> User, video_id -> Video)
            View(video_id -> Video, user_id -> User, watched_seconds)
Features:   - Upload short vertical cooking videos with a recipe
            - Show a full-screen swipeable feed
            - Like and save videos
            - Rank the feed by watch time and likes
            - Transcode videos for mobile playback
API:        REST
            GET  /feed?cursor=
            POST /videos
            POST /videos/{id}/like
            POST /videos/{id}/views
Storage:    PostgreSQL, S3 + CloudFront (video)
Tech stack: TypeScript, Next.js, FFmpeg, AWS MediaConvert
```

---

## Example 249

**Intent:**
discussion forum in django

**Spec:**
```
Type:       Web application (forum)
Auth:       Django authentication (email + password)
Data model: User(id, username, email)
            Forum(id, name, slug)
            Topic(id, forum_id -> Forum, user_id -> User, subject, views)
            Post(id, topic_id -> Topic, user_id -> User, content, created_at)
Features:   - List forums and topics
            - Post topics and replies
            - Count topic views
            - Subscribe to topics
            - Moderate posts from the Django admin
API:        REST
            GET  /forums/
            GET  /forums/{slug}/
            POST /topics/
            POST /topics/{id}/reply/
Storage:    PostgreSQL
Tech stack: Python, Django, django-machina
```

---

## Example 250

**Intent:**
platform for people to rate and review apartment buildings in nyc

**Spec:**
```
Type:       Web application (review site)
Auth:       Email + password, reviews published under a username
Data model: User(id, username, email, password_hash)
            Building(id, address, borough, management_company)
            Review(id, building_id -> Building, user_id -> User, rating, noise, heat, pests, landlord_responsiveness, body, lived_from, lived_to)
Features:   - Search buildings by address or borough
            - Write reviews rating noise, heat, pests and management
            - Show average scores per building
            - Show public housing violations from NYC Open Data
            - Report fake reviews
API:        REST
            GET  /buildings?q=
            GET  /buildings/{id}
            POST /buildings/{id}/reviews
            GET  /buildings/{id}/violations
Storage:    PostgreSQL
Tech stack: Python, FastAPI, NYC Open Data (Socrata API), React
```

---

## Example 251

**Intent:**
course platform for corporate training with completion tracking for compliance

**Spec:**
```
Type:       Web application (corporate LMS)
Auth:       Single sign-on via SAML with the company identity provider
Data model: Employee(id, email, name, department, manager_id -> Employee)
            Course(id, title, mandatory, renew_every_months)
            Assignment(id, course_id -> Course, employee_id -> Employee, due_on, completed_at, score)
            Module(id, course_id -> Course, scorm_package_url)
Features:   - Assign mandatory courses by department
            - Play SCORM course packages
            - Record completion and quiz scores
            - Remind employees and managers about overdue training
            - Export a compliance report for auditors
API:        REST
            GET  /me/assignments
            POST /assignments
            POST /assignments/{id}/complete
            GET  /reports/compliance?department=
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, SCORM Again, React
```

---

## Example 252

**Intent:**
something where I can host a book giveaway and pick random winners

**Spec:**
```
Type:       Web application (giveaway)
Auth:       Host login, entrants enter with email
Data model: Giveaway(id, title, book_title, ends_at, winner_count)
            Entry(id, giveaway_id -> Giveaway, name, email, country, created_at)
            Winner(giveaway_id -> Giveaway, entry_id -> Entry)
Features:   - Create a giveaway with an end date and number of winners
            - Let people enter once per email
            - Restrict entries by country
            - Pick random winners when it ends
            - Email winners for their address
API:        REST
            POST /giveaways
            GET  /giveaways/{id}
            POST /giveaways/{id}/entries
            POST /giveaways/{id}/draw
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 253

**Intent:**
a site for my friends to bet fake points on sports games

**Spec:**
```
Type:       Web application (social prediction game)
Auth:       Email + password, private groups by invite
Data model: User(id, name, email, password_hash)
            Group(id, name, invite_code)
            Match(id, sport, home_team, away_team, starts_at, result)
            Prediction(id, match_id -> Match, user_id -> User, group_id -> Group, pick, points_staked)
            Balance(user_id -> User, group_id -> Group, points)
Features:   - Give everyone 1000 starting points per group
            - Predict match results and stake points
            - Lock predictions when the match starts
            - Settle points from real results
            - Show a group leaderboard
API:        REST
            GET  /matches
            POST /predictions
            GET  /groups/{id}/leaderboard
            POST /groups/join
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, React, API-Football
```

---

## Example 254

**Intent:**
digital garden website

**Spec:**
```
Type:       Web application (digital garden)
Data model: Note(id, title, slug, body_markdown, maturity, tags, updated_at)
Features:   - Publish notes marked as seedling, budding or evergreen
            - Link notes with wiki links and show backlinks
            - Show a hover preview of linked notes
            - Show a graph of how notes connect
Storage:    Markdown files in the repo
Tech stack: Eleventy, markdown-it, Netlify
```

---

## Example 255

**Intent:**
can u make me a marketplace for tutors in my country (philippines) where students pay with gcash

**Spec:**
```
Type:       Web application (tutoring marketplace)
Auth:       Email + password or mobile number with OTP
Data model: Tutor(id, name, email, subjects, hourly_rate_php, bio, verified)
            Student(id, name, mobile, email)
            Session(id, tutor_id -> Tutor, student_id -> Student, starts_at, minutes, amount_php, status)
            Payment(id, session_id -> Session, provider, reference, status)
Features:   - Search tutors by subject and price
            - Book a session time
            - Pay with GCash or card through a local payment gateway
            - Pay tutors weekly
            - Rate tutors after sessions
API:        REST
            GET  /tutors?subject=
            POST /sessions
            POST /sessions/{id}/pay
            POST /webhooks/paymongo
            POST /sessions/{id}/rating
Storage:    PostgreSQL
Tech stack: Laravel, Vue.js, PayMongo API
```

---

## Example 256

**Intent:**
tool for writers to get ai feedback on their essay structure, not rewrite it

**Spec:**
```
Type:       Web application (AI writing feedback)
Auth:       Email + password
Data model: User(id, email, password_hash)
            Essay(id, user_id -> User, title, text, created_at)
            FeedbackItem(id, essay_id -> Essay, paragraph_index, type, comment)
Features:   - Paste an essay and split it into paragraphs
            - Comment on thesis, structure and transitions with an LLM
            - Pin each comment to a paragraph
            - Never rewrite the user's text, only suggest
            - Compare feedback between drafts
API:        REST
            POST /essays
            POST /essays/{id}/feedback
            GET  /essays/{id}
Storage:    PostgreSQL
Tech stack: Python, Flask, Anthropic Claude API, htmx
```

---

## Example 257

**Intent:**
build a voting site for our community budget, residents vote on projects

**Spec:**
```
Type:       Web application (participatory budgeting)
Auth:       Residents verify with email and postcode, one vote per resident
Data model: Resident(id, email, postcode, verified)
            Project(id, title, description, cost, neighbourhood, image_url)
            Ballot(id, resident_id -> Resident, submitted_at)
            BallotChoice(ballot_id -> Ballot, project_id -> Project)
Features:   - Show proposed projects with cost and description
            - Let residents choose projects up to the total budget
            - Allow one ballot per verified resident
            - Show results after voting closes
            - Let residents submit project proposals before the vote
API:        REST
            GET  /projects
            POST /proposals
            POST /ballots
            GET  /results
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Decidim
```

---

## Example 258

**Intent:**
forum for diabetics to share tips

**Spec:**
```
Type:       Web application (health community forum)
Auth:       Email + password
Data model: Member(id, username, email, password_hash, diabetes_type)
            Topic(id, member_id -> Member, category, title, body)
            Reply(id, topic_id -> Topic, member_id -> Member, body, helpful_votes)
Features:   - Post in categories like Food, Tech and Exercise
            - Filter topics by Type 1 or Type 2
            - Vote replies as helpful
            - Show a medical disclaimer on every page
API:        REST
            GET  /topics?category=&type=
            POST /topics
            POST /topics/{id}/replies
            POST /replies/{id}/helpful
Storage:    PostgreSQL
Tech stack: Node.js, Express, Handlebars
```

---

## Example 259

**Intent:**
give me a spec for a SaaS that lets bootcamps run coding assessments on applicants

**Spec:**
```
Type:       Web application (coding assessment SaaS)
Auth:       Email + password for bootcamp staff, applicants use a unique invite link
Data model: Bootcamp(id, name, plan)
            Assessment(id, bootcamp_id -> Bootcamp, title, time_limit_minutes)
            Challenge(id, assessment_id -> Assessment, prompt, language, tests)
            Invite(id, assessment_id -> Assessment, applicant_email, token, started_at, submitted_at, score)
Features:   - Create assessments with coding challenges and hidden tests
            - Send applicants a time-limited invite link
            - Run applicants' code in a sandboxed container
            - Score submissions automatically
            - Replay how the applicant typed their solution
API:        REST
            POST /assessments
            POST /assessments/{id}/invites
            GET  /take/{token}
            POST /take/{token}/run
            POST /take/{token}/submit
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, React, Judge0 API
```

---

## Example 260

**Intent:**
rate my professor clone for my uni

**Spec:**
```
Type:       Web application (review site)
Auth:       University email verification, reviews shown anonymously
Data model: Student(id, uni_email, verified)
            Professor(id, name, department)
            Course(id, code, name)
            Rating(id, professor_id -> Professor, course_id -> Course, student_id -> Student, quality, difficulty, would_take_again, comment, created_at)
Features:   - Search professors by name and department
            - Rate quality and difficulty for a specific course
            - Show averages and "would take again" percentage
            - Limit one rating per course per student
            - Flag offensive comments
API:        REST
            GET  /professors?q=
            GET  /professors/{id}
            POST /professors/{id}/ratings
            POST /ratings/{id}/flag
Storage:    PostgreSQL
Tech stack: Python, Django, React
```

---

## Example 261

**Intent:**
crowdfunding pre orders for my hardware gadget

**Spec:**
```
Type:       Web application (pre-order campaign)
Auth:       Backers check out as guests, admin login
Data model: Campaign(id, product_name, goal_units, ends_at, status)
            Tier(id, campaign_id -> Campaign, name, price_cents, limit, sold)
            Preorder(id, tier_id -> Tier, email, shipping_address, payment_method_id, charged)
Features:   - Take pre-orders with early-bird tiers
            - Save card details and charge only when the goal is met
            - Show units sold and days left
            - Email backers production updates
            - Export orders for fulfilment
API:        REST
            GET  /campaign
            POST /tiers/{id}/preorders
            POST /admin/campaign/charge
            GET  /admin/preorders.csv
Storage:    PostgreSQL
Tech stack: Next.js, Stripe SetupIntents, Resend
```

---

## Example 262

**Intent:**
thing to manage my small agency's freelancers, who's working on what and invoices they send me

**Spec:**
```
Type:       Web application (freelancer management)
Auth:       Email + password for the agency owner, freelancers log in by magic link
Data model: Freelancer(id, name, email, day_rate, skills)
            Project(id, name, client, status)
            Assignment(id, project_id -> Project, freelancer_id -> Freelancer, start_date, end_date, days)
            FreelancerInvoice(id, freelancer_id -> Freelancer, project_id -> Project, amount, file_url, status)
Features:   - Keep a list of freelancers with rates and skills
            - Assign freelancers to projects with dates
            - Show who is booked on a timeline
            - Let freelancers upload invoices
            - Mark invoices as approved and paid
API:        REST
            GET  /freelancers
            POST /assignments
            GET  /timeline
            POST /invoices
            PATCH /invoices/{id}
Storage:    PostgreSQL, S3 (invoices)
Tech stack: Python, Django, HTMX
```

---

## Example 263

**Intent:**
a wiki for board game rules in plain english

**Spec:**
```
Type:       Web application (rules wiki)
Auth:       Email + password for editors, public reading
Data model: Game(id, title, players, play_time)
            RulesPage(id, game_id -> Game, setup, turn_structure, scoring, faq, updated_at)
            Revision(id, rules_page_id -> RulesPage, editor_id -> Editor, content, created_at)
            Editor(id, username, email, password_hash)
Features:   - Write a plain-English rules summary for each game
            - Split rules into setup, turns, scoring and FAQ
            - Keep revision history
            - Let readers suggest corrections
            - Show a printable one-page cheat sheet
API:        REST
            GET  /games/{id}/rules
            PUT  /games/{id}/rules
            POST /games/{id}/suggestions
            GET  /games/{id}/cheatsheet
Storage:    PostgreSQL
Tech stack: Python, Flask, WeasyPrint
```

---

## Example 264

**Intent:**
i need kanban but for my hiring pipeline

**Spec:**
```
Type:       Web application (applicant tracking)
Auth:       Email + password, team invites
Data model: Job(id, title, department, status)
            Candidate(id, name, email, cv_url, source)
            Application(id, job_id -> Job, candidate_id -> Candidate, stage, rating)
            Note(id, application_id -> Application, author, body, created_at)
Features:   - Show candidates on a board with stages like Applied, Interview and Offer
            - Drag candidates between stages
            - Upload CVs and add interview notes
            - Rate candidates out of 5
            - Email candidates using templates when they move stage
API:        REST
            GET  /jobs/{id}/applications
            POST /candidates
            PATCH /applications/{id}
            POST /applications/{id}/notes
Storage:    PostgreSQL, S3 (CVs)
Tech stack: Node.js, Express, React, react-beautiful-dnd
```

---

## Example 265

**Intent:**
wordpress-like cms but faster, in go

**Spec:**
```
Type:       Web application (CMS)
Auth:       Email + password, roles: admin, editor, author
Data model: User(id, email, password_hash, role)
            Page(id, title, slug, blocks_json, status, template)
            Post(id, title, slug, body, author_id -> User, published_at)
            Media(id, filename, url, alt_text)
Features:   - Build pages from content blocks
            - Write blog posts with a rich-text editor
            - Upload and resize images
            - Choose a theme template for each page
            - Cache rendered pages for fast loading
API:        REST
            GET  /{slug}
            POST /admin/pages
            POST /admin/posts
            POST /admin/media
Storage:    PostgreSQL, local disk (media)
Tech stack: Go, Chi, templ, HTMX
```

---

## Example 266

**Intent:**
voluntering website for animal shelter dog walking slots

**Spec:**
```
Type:       Web application (volunteer scheduling)
Auth:       Email + password, volunteers approved after orientation
Data model: Volunteer(id, name, email, password_hash, approved, experience_level)
            Dog(id, name, size, walk_level, notes)
            WalkSlot(id, dog_id -> Dog, starts_at, volunteer_id -> Volunteer, completed)
Features:   - Show available walking slots for each dog
            - Only show dogs that match the volunteer's experience level
            - Book and cancel walk slots
            - Log notes after a walk
            - Let staff approve new volunteers
API:        REST
            GET  /slots
            POST /slots/{id}/book
            DELETE /slots/{id}/book
            POST /slots/{id}/notes
            PATCH /admin/volunteers/{id}
Storage:    PostgreSQL
Tech stack: Python, Flask, SQLAlchemy
```

---

## Example 267

**Intent:**
An online gallery where artists from my art school can show their final year work and visitors leave comments

**Spec:**
```
Type:       Web application (virtual exhibition)
Auth:       Student accounts created by staff, visitors comment with a name and email
Data model: Student(id, name, email, password_hash, programme)
            Artwork(id, student_id -> Student, title, medium, statement, images, video_url)
            Comment(id, artwork_id -> Artwork, visitor_name, body, approved)
Features:   - Give each student an exhibition page
            - Show artworks with images, video and an artist statement
            - Let visitors leave comments after moderation
            - Filter by programme
            - Show a random featured work on the home page
API:        REST
            GET  /students
            GET  /artworks/{id}
            POST /artworks/{id}/comments
            POST /artworks
Storage:    PostgreSQL, Cloudinary
Tech stack: Next.js, Prisma, Cloudinary
```

---

## Example 268

**Intent:**
something like patreon for local artists

**Spec:**
```
Type:       Web application (creator membership platform)
Auth:       Email + password, roles: creator and supporter
Data model: Creator(id, name, email, password_hash, bio, stripe_account_id)
            Tier(id, creator_id -> Creator, name, monthly_price, perks)
            Subscription(id, tier_id -> Tier, supporter_id -> Supporter, status, stripe_subscription_id)
            Supporter(id, email, password_hash)
            Post(id, creator_id -> Creator, min_tier_id -> Tier, title, body, media_url)
Features:   - Create monthly membership tiers
            - Subscribe supporters with recurring payments
            - Lock posts to a minimum tier
            - Pay creators through Stripe Connect
            - Show creators their monthly earnings
API:        REST
            GET  /creators/{id}
            POST /tiers/{id}/subscribe
            POST /posts
            GET  /creators/{id}/posts
            POST /webhooks/stripe
Storage:    PostgreSQL, S3 (media)
Tech stack: Ruby on Rails, Stripe Connect, Stripe Billing
```

---

## Example 269

**Intent:**
shared expenses site for a group trip

**Spec:**
```
Type:       Web application (expense splitting)
Auth:       No accounts, the trip is accessed by a secret link
Data model: Trip(id, name, currency, secret_token)
            Participant(id, trip_id -> Trip, name)
            Expense(id, trip_id -> Trip, payer_id -> Participant, amount, description, date)
            ExpenseShare(expense_id -> Expense, participant_id -> Participant, share)
Features:   - Add expenses and who they were split between
            - Calculate who owes whom with the fewest payments
            - Support expenses in different currencies
            - Share the trip by link
API:        REST
            POST /trips
            GET  /trips/{token}
            POST /trips/{token}/expenses
            GET  /trips/{token}/settle
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 270

**Intent:**
forum where you can only post during certain hours lol like a cafe that opens and closes

**Spec:**
```
Type:       Web application (time-limited forum)
Auth:       Email + password
Data model: User(id, username, email, password_hash)
            OpeningHours(weekday, opens_at, closes_at)
            Thread(id, user_id -> User, title, body, created_at)
            Reply(id, thread_id -> Thread, user_id -> User, body)
Features:   - Allow posting only during set opening hours
            - Show a countdown until the forum opens or closes
            - Keep threads readable while closed
            - Archive threads at closing time each day
API:        REST
            GET  /status
            GET  /threads
            POST /threads
            POST /threads/{id}/replies
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix LiveView, Oban
```

---

## Example 271

**Intent:**
job board aggregator that pulls jobs from other sites for climate tech

**Spec:**
```
Type:       Web application (job aggregator)
Data model: Source(id, name, feed_url, type)
            Job(id, source_id -> Source, external_id, title, company, location, remote, url, posted_at, category)
            Subscriber(id, email, categories)
Features:   - Import jobs from RSS feeds and company ATS boards every 6 hours
            - Remove duplicates across sources
            - Tag jobs by climate category such as Energy and Food
            - Search and filter jobs
            - Email subscribers a weekly digest
API:        REST
            GET  /jobs?category=&remote=
            GET  /jobs/{id}
            POST /subscribers
Storage:    PostgreSQL
Tech stack: Python, FastAPI, APScheduler, Greenhouse and Lever job board APIs
```

---

## Example 272

**Intent:**
invite-only community for female founders with directory and events

**Spec:**
```
Type:       Web application (private community)
Auth:       Invite-only email + password, application reviewed by admins
Data model: Member(id, name, email, password_hash, company, industry, stage, city, approved)
            Application(id, email, answers_json, status)
            Event(id, title, starts_at, location, online_url)
            RSVP(event_id -> Event, member_id -> Member)
Features:   - Apply to join and be reviewed by admins
            - Search the member directory by industry, stage and city
            - RSVP to online and in-person events
            - Post asks and offers on a community board
            - Send a monthly member newsletter
API:        REST
            POST /applications
            GET  /members?industry=&city=
            GET  /events
            POST /events/{id}/rsvp
            POST /board/posts
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Supabase
```

---

## Example 273

**Intent:**
forum for beekeepers

**Spec:**
```
Type:       Web application (forum)
Auth:       Email + password
Data model: Beekeeper(id, username, email, password_hash, region, hives_count)
            Board(id, name)
            Thread(id, board_id -> Board, author_id -> Beekeeper, title, season)
            Post(id, thread_id -> Thread, author_id -> Beekeeper, body, photos)
Features:   - Discuss in boards like Swarms, Pests and Honey Harvest
            - Tag threads by season
            - Show each member's region so advice fits the climate
            - Attach hive photos to posts
API:        REST
            GET  /boards
            GET  /boards/{id}/threads
            POST /threads
            POST /threads/{id}/posts
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 274

**Intent:**
hi, im from vietnam, i want make website for people learn cooking vietnamese food with video and buy ingredient kit

**Spec:**
```
Type:       Web application (cooking course and shop)
Auth:       Email + password
Data model: Customer(id, name, email, password_hash, address)
            Recipe(id, title, video_url, difficulty, steps)
            IngredientKit(id, recipe_id -> Recipe, price, stock)
            Order(id, customer_id -> Customer, total, status, created_at)
            OrderItem(order_id -> Order, kit_id -> IngredientKit, quantity)
Features:   - Watch step-by-step cooking videos
            - Buy the ingredient kit for a recipe
            - Track order and delivery status
            - Show recipes in Vietnamese and English
            - Rate recipes after cooking
API:        REST
            GET  /recipes
            GET  /recipes/{id}
            POST /orders
            GET  /orders/{id}
            POST /recipes/{id}/ratings
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, Next.js, Stripe
```

---

## Example 275

**Intent:**
a site where people trade services instead of money, like timebanking

**Spec:**
```
Type:       Web application (timebank)
Auth:       Email + password
Data model: Member(id, name, email, password_hash, hour_balance)
            ServiceOffer(id, member_id -> Member, title, category, description)
            Exchange(id, offer_id -> ServiceOffer, receiver_id -> Member, hours, status, confirmed_at)
Features:   - Offer services like tutoring or repairs
            - Request a service from another member
            - Transfer hours when both sides confirm the exchange
            - Give new members 2 starting hours
            - Show each member's hour balance and history
API:        REST
            GET  /offers?category=
            POST /offers
            POST /offers/{id}/exchanges
            POST /exchanges/{id}/confirm
            GET  /me/balance
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire
```

---

## Example 276

**Intent:**
wiki for our D2C brand's product specs, only staff

**Spec:**
```
Type:       Web application (internal product wiki)
Auth:       Google Workspace sign-in
Data model: Product(id, sku, name, category)
            SpecSheet(id, product_id -> Product, materials, dimensions, care_instructions, supplier, updated_at)
            Attachment(id, product_id -> Product, file_url, label)
Features:   - Keep a spec sheet for every SKU
            - Attach supplier files and photos
            - Search by SKU, name or material
            - Show the change history of a spec sheet
            - Export a spec sheet as PDF
API:        REST
            GET  /products?q=
            GET  /products/{id}/spec
            PUT  /products/{id}/spec
            POST /products/{id}/attachments
Storage:    PostgreSQL, Google Cloud Storage
Tech stack: Python, FastAPI, React
```

---

## Example 277

**Intent:**
online course platform but you pay what you want

**Spec:**
```
Type:       Web application (pay-what-you-want courses)
Auth:       Email + password
Data model: Course(id, title, description, min_price_cents, suggested_price_cents)
            Lesson(id, course_id -> Course, title, content, video_url)
            Student(id, email, password_hash)
            Enrollment(course_id -> Course, student_id -> Student, amount_paid_cents)
Features:   - Let students choose a price at or above the minimum
            - Show the suggested price and average paid
            - Allow free enrollment when the minimum is 0
            - Unlock lessons after enrollment
            - Thank students who pay above the suggested price
API:        REST
            GET  /courses
            POST /courses/{id}/enroll
            GET  /courses/{id}/lessons
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 278

**Intent:**
plz make sum site for my gaming clan, roster, events, recruit applications

**Spec:**
```
Type:       Web application (gaming clan site)
Auth:       Discord sign-in
Data model: Member(id, discord_id, name, rank, joined_on)
            Event(id, title, game, starts_at)
            EventSignup(event_id -> Event, member_id -> Member, role)
            RecruitApplication(id, discord_id, game_name, hours_played, why_join, status)
Features:   - Show the clan roster with ranks
            - Post raids and events with sign-ups by role
            - Accept recruit applications
            - Let officers approve or reject applicants
            - Post new events to Discord with a webhook
API:        REST
            GET  /roster
            GET  /events
            POST /events/{id}/signup
            POST /applications
            PATCH /applications/{id}
Storage:    SQLite
Tech stack: Node.js, Express, Vue.js, Discord webhooks
```

---

## Example 279

**Intent:**
website where students find roommates

**Spec:**
```
Type:       Web application (roommate matching)
Auth:       University email registration
Data model: Student(id, name, uni_email, budget, move_in_date, sleep_schedule, cleanliness, smoker, bio)
            Like(from_id -> Student, to_id -> Student)
            Conversation(id, student_a_id -> Student, student_b_id -> Student)
            Message(id, conversation_id -> Conversation, sender_id -> Student, body)
Features:   - Fill in a lifestyle profile with budget and habits
            - Show a compatibility score for other students
            - Like profiles and chat when it is mutual
            - Filter by budget and move-in date
            - Report fake profiles
API:        REST
            GET  /matches
            POST /likes
            GET  /conversations
            POST /conversations/{id}/messages
Storage:    PostgreSQL
Tech stack: Python, FastAPI, React
```

---

## Example 280

**Intent:**
blog with nextjs and contentful

**Spec:**
```
Type:       Web application (blog)
Auth:       Contentful web app login for editors
Data model: BlogPost(id, title, slug, excerpt, body_rich_text, hero_image, author, published_date)
            Author(id, name, avatar)
Features:   - Write posts in Contentful
            - Build static pages with incremental regeneration
            - Preview drafts before publishing
            - Show related posts by tag
            - Rebuild pages when content changes via webhook
API:        REST
            GET  /blog
            GET  /blog/{slug}
            POST /api/revalidate
            GET  /api/preview
Storage:    Contentful
Tech stack: Next.js, Contentful Content Delivery API, Vercel
```

---

## Example 281

**Intent:**
I'd love a site for neighbours to organise street parties: plan the date, who brings what, road closure forms...

**Spec:**
```
Type:       Web application (event planning)
Auth:       Organiser email + password, neighbours join by link
Data model: Party(id, street, date, organiser_email, share_code)
            Household(id, party_id -> Party, house_number, name)
            ContributionItem(id, party_id -> Party, item, claimed_by -> Household)
            Task(id, party_id -> Party, title, done, due_on)
Features:   - Pick a date with a neighbour poll
            - Make a list of food and equipment for households to claim
            - Track tasks like the road closure application
            - Remind the organiser of council deadlines
            - Share an invite flyer as PDF
API:        REST
            POST /parties
            GET  /parties/{code}
            POST /parties/{code}/households
            POST /items/{id}/claim
            PATCH /tasks/{id}
Storage:    SQLite
Tech stack: Python, Flask, WeasyPrint
```

---

## Example 282

**Intent:**
Make marketplace for freelance photographers and clients book them by hour

**Spec:**
```
Type:       Web application (photographer booking marketplace)
Auth:       Email + password, roles: photographer and client
Data model: Photographer(id, name, city, hourly_rate, specialties, portfolio_urls)
            Client(id, name, email, password_hash)
            Availability(id, photographer_id -> Photographer, date, start_time, end_time)
            Booking(id, photographer_id -> Photographer, client_id -> Client, starts_at, hours, total, status)
Features:   - Browse photographers by city and specialty
            - Book hours from the photographer's availability
            - Pay upfront and release payment after the gallery is delivered
            - Deliver photos through a private gallery link
            - Review the photographer
API:        REST
            GET  /photographers?city=
            GET  /photographers/{id}/availability
            POST /bookings
            POST /bookings/{id}/deliver
Storage:    PostgreSQL, S3 (galleries)
Tech stack: Python, Django, Stripe Connect
```

---

## Example 283

**Intent:**
ai summariser for podcasts episodes

**Spec:**
```
Type:       Web application (AI summariser)
Auth:       Email + password
Data model: User(id, email, password_hash)
            Episode(id, feed_url, title, audio_url, transcript, summary, status)
            Subscription(user_id -> User, feed_url)
Features:   - Subscribe to podcast RSS feeds
            - Transcribe new episodes with speech-to-text
            - Summarise each episode with key takeaways and quotes
            - Email summaries when new episodes come out
            - Search across transcripts
API:        REST
            POST /subscriptions
            GET  /episodes
            GET  /episodes/{id}
            GET  /search?q=
Storage:    PostgreSQL, S3 (audio)
Tech stack: Python, FastAPI, Celery, OpenAI Whisper API, Anthropic Claude API
```

---

## Example 284

**Intent:**
Our church small groups need a site to find a group near them by day of week and topic

**Spec:**
```
Type:       Web application (small group finder)
Auth:       Leader login with email + password
Data model: Group(id, name, leader_id -> Leader, topic, weekday, time, area, capacity, open)
            Leader(id, name, email, password_hash)
            JoinRequest(id, group_id -> Group, name, email, phone, message)
Features:   - List groups by area, weekday and topic
            - Show groups on a map
            - Send a join request to the leader
            - Let leaders open or close their group
            - Show how many places are left
API:        REST
            GET  /groups?area=&weekday=&topic=
            POST /groups/{id}/requests
            PATCH /groups/{id}
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Leaflet
```

---

## Example 285

**Intent:**
browser-based team password sharing for small companies, saas

**Spec:**
```
Type:       Web application (password manager SaaS)
Auth:       Email + master password with client-side key derivation, two-factor authentication
Data model: Organization(id, name, plan)
            User(id, organization_id -> Organization, email, public_key, encrypted_private_key)
            Vault(id, organization_id -> Organization, name)
            VaultAccess(vault_id -> Vault, user_id -> User, encrypted_vault_key)
            Secret(id, vault_id -> Vault, encrypted_blob, updated_at)
Features:   - Encrypt secrets in the browser before upload
            - Share vaults with team members using public-key encryption
            - Revoke access when someone leaves
            - Log who viewed which secret
            - Generate strong passwords
API:        REST
            GET  /vaults
            POST /vaults
            POST /vaults/{id}/access
            GET  /vaults/{id}/secrets
            POST /vaults/{id}/secrets
            GET  /audit
Storage:    PostgreSQL (ciphertext only)
Tech stack: TypeScript, React, Web Crypto API, Node.js, Fastify
```

---

## Example 286

**Intent:**
reviews of remote work tools

**Spec:**
```
Type:       Web application (software review site)
Auth:       Email + password or LinkedIn sign-in
Data model: Reviewer(id, name, job_title, company_size, linkedin_verified)
            Tool(id, name, category, website, pricing)
            Review(id, tool_id -> Tool, reviewer_id -> Reviewer, rating, pros, cons, use_case, created_at)
Features:   - Browse tools by category like Video Calls and Docs
            - Write reviews with pros, cons and company size
            - Compare two tools side by side
            - Show verified-reviewer badges
            - Rank tools per category
API:        REST
            GET  /tools?category=
            GET  /tools/{id}/reviews
            POST /tools/{id}/reviews
            GET  /compare?a=&b=
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, Next.js
```

---

## Example 287

**Intent:**
a site that matches volunteers who speak other languages with refugees needing translation at appointments

**Spec:**
```
Type:       Web application (volunteer interpreter matching)
Auth:       Email + password for volunteers and caseworkers
Data model: Interpreter(id, name, email, phone, languages, area, vetted)
            Caseworker(id, name, organisation, email, password_hash)
            AppointmentRequest(id, caseworker_id -> Caseworker, language, location, starts_at, duration_minutes, interpreter_id -> Interpreter, status)
Features:   - Let caseworkers request an interpreter for a language, place and time
            - Notify vetted interpreters who speak that language
            - Let the first available interpreter accept
            - Send both sides a confirmation and reminder
            - Keep refugee personal details out of the system
API:        REST
            POST /requests
            GET  /requests/open
            POST /requests/{id}/accept
            GET  /me/appointments
Storage:    PostgreSQL
Tech stack: Python, Django, Twilio
```

---

## Example 288

**Intent:**
open source alternative to calendly but for teams

**Spec:**
```
Type:       Web application (scheduling SaaS)
Auth:       Google and Microsoft OAuth with calendar access
Data model: User(id, email, name, calendar_provider, timezone)
            Team(id, name, slug)
            EventType(id, team_id -> Team, title, duration_minutes, routing)
            Booking(id, event_type_id -> EventType, host_id -> User, guest_email, starts_at, status)
Features:   - Read team members' calendars to find free slots
            - Offer round-robin and collective event types
            - Book a slot and create calendar events for host and guest
            - Send confirmation and reminder emails
            - Let guests reschedule or cancel
API:        REST
            GET  /{team}/{event}
            GET  /event-types/{id}/slots?date=
            POST /bookings
            PATCH /bookings/{id}
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Google Calendar API, Microsoft Graph API
```

---

## Example 289

**Intent:**
newsletter for job seekers that matches jobs to their profile every week

**Spec:**
```
Type:       Web application (job alert newsletter)
Auth:       Email magic-link login
Data model: Seeker(id, email, title_keywords, locations, remote_only, min_salary)
            Job(id, title, company, location, salary_min, url, posted_at)
            SentJob(seeker_id -> Seeker, job_id -> Job, sent_at)
Features:   - Set up a job profile in one short form
            - Match new jobs to each profile
            - Send a weekly email with the top 10 matches
            - Never send the same job twice
            - Unsubscribe with one click
API:        REST
            POST /seekers
            PUT  /seekers/me
            GET  /unsubscribe/{token}
Storage:    PostgreSQL
Tech stack: Python, Django, Celery, Postmark
```

---

## Example 290

**Intent:**
collaborative spreadsheet thing for tracking our band gigs and money

**Spec:**
```
Type:       Web application (band management)
Auth:       Email + password, band members invited
Data model: Band(id, name)
            Member(id, band_id -> Band, name, email)
            Gig(id, band_id -> Band, venue, date, fee, paid)
            Expense(id, band_id -> Band, description, amount, paid_by -> Member, gig_id -> Gig)
Features:   - Track gigs with venue, date and fee
            - Log expenses and who paid
            - Split gig income between members
            - Show who is owed money
            - Export the year to a spreadsheet for taxes
API:        REST
            GET  /gigs
            POST /gigs
            POST /expenses
            GET  /balances
            GET  /export.xlsx
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, ExcelJS
```

---

## Example 291

**Intent:**
knowledge base for IT helpdesk with ticket deflection

**Spec:**
```
Type:       Web application (IT knowledge base)
Auth:       Microsoft Entra ID single sign-on
Data model: Article(id, title, body, tags, views, helpful_votes)
            SearchLog(id, query, results_count, created_at)
            Ticket(id, requester_email, subject, description, status)
Features:   - Publish how-to articles for common IT issues
            - Suggest articles while employees type a ticket
            - Track whether the article solved it
            - Show searches with no results to the IT team
            - Create a ticket only if no article helped
API:        REST
            GET  /articles?q=
            POST /articles
            POST /articles/{id}/helpful
            POST /tickets
            GET  /admin/failed-searches
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Azure AI Search
```

---

## Example 292

**Intent:**
im making a site for my roleplay community where people make characters and write stories together

**Spec:**
```
Type:       Web application (collaborative roleplay)
Auth:       Email + password
Data model: User(id, username, email, password_hash)
            Character(id, user_id -> User, name, bio, avatar_url)
            Story(id, title, setting, created_by -> User)
            StoryPost(id, story_id -> Story, character_id -> Character, body, created_at)
Features:   - Create characters with bios and avatars
            - Start stories and invite characters
            - Write turns posting as a character
            - Notify players when it is their turn
            - Show a character's appearances across stories
API:        REST
            POST /characters
            POST /stories
            POST /stories/{id}/invites
            POST /stories/{id}/posts
            GET  /characters/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Channels
```

---

## Example 293

**Intent:**
ebook store where i sell my own books, pdf and epub

**Spec:**
```
Type:       Web application (ebook store)
Auth:       Customers check out as guests, optional library account
Data model: Book(id, title, description, price_cents, cover_url, pdf_key, epub_key)
            Order(id, email, book_id -> Book, paid_at)
            Library(email, book_id -> Book)
Features:   - Sell ebooks with Stripe Checkout
            - Deliver PDF and EPUB downloads after payment
            - Watermark each PDF with the buyer's email
            - Let buyers re-download from their library
            - Send free sample chapters by email
API:        REST
            GET  /books
            POST /checkout
            POST /webhooks/stripe
            GET  /library
            GET  /download/{token}
Storage:    PostgreSQL, S3 (files)
Tech stack: Python, Flask, Stripe, pypdf
```

---

## Example 294

**Intent:**
hey can you design a site for my local soccer league, tables, fixtures, results entered by refs

**Spec:**
```
Type:       Web application (sports league)
Auth:       Email + password for referees and admins
Data model: Team(id, name, division)
            Fixture(id, home_team_id -> Team, away_team_id -> Team, kickoff_at, pitch, referee_id -> Referee)
            Result(fixture_id -> Fixture, home_goals, away_goals, submitted_by -> Referee)
            Referee(id, name, email, password_hash)
Features:   - Generate a round-robin fixture list
            - Let referees enter results after matches
            - Calculate league tables automatically
            - Show fixtures and results per team
            - Publish a top scorers list
API:        REST
            GET  /fixtures
            POST /fixtures/{id}/result
            GET  /tables/{division}
            GET  /teams/{id}
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 295

**Intent:**
medium sized SaaS needs status page

**Spec:**
```
Type:       Web application (status page)
Auth:       Admin login for engineers, subscribers by email
Data model: Component(id, name, status)
            Incident(id, title, status, impact, started_at, resolved_at)
            IncidentUpdate(id, incident_id -> Incident, body, created_at)
            Subscriber(id, email)
Features:   - Show the status of each component
            - Post incidents and updates
            - Show 90-day uptime per component
            - Email subscribers when an incident is opened or resolved
            - Check endpoints every minute and mark components down
API:        REST
            GET  /status
            GET  /incidents
            POST /admin/incidents
            POST /admin/incidents/{id}/updates
            POST /subscribe
Storage:    PostgreSQL
Tech stack: Go, Templ, Postmark
```

---

## Example 296

**Intent:**
forum where every post is reviewed by ai for toxicity before going live

**Spec:**
```
Type:       Web application (AI-moderated forum)
Auth:       Email + password
Data model: User(id, username, email, password_hash, strikes)
            Thread(id, user_id -> User, title, created_at)
            Post(id, thread_id -> Thread, user_id -> User, body, toxicity_score, status)
Features:   - Score each post for toxicity before publishing
            - Publish low-scoring posts instantly
            - Send borderline posts to a human moderator queue
            - Suggest a kinder rewording to the author
            - Give strikes for removed posts
API:        REST
            POST /threads
            POST /threads/{id}/posts
            GET  /mod/queue
            PATCH /mod/posts/{id}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Perspective API, React
```

---

## Example 297

**Intent:**
web app to manage a scout troop, badges, camps and parent permission forms

**Spec:**
```
Type:       Web application (youth group management)
Auth:       Email + password, roles: leader and parent
Data model: Scout(id, name, birth_date, parent_id -> Parent, patrol)
            Parent(id, name, email, password_hash, phone)
            Badge(id, name, requirements)
            BadgeProgress(scout_id -> Scout, badge_id -> Badge, completed_requirements, awarded_on)
            Camp(id, title, starts_on, ends_on, cost)
            Permission(camp_id -> Camp, scout_id -> Scout, signed_by, signed_at, medical_notes)
Features:   - Track badge requirements per scout
            - Create camps and collect online permission forms
            - Collect medical notes securely
            - Take camp payments
            - Show parents their child's progress
API:        REST
            GET  /scouts/{id}/badges
            POST /scouts/{id}/badges
            POST /camps
            POST /camps/{id}/permissions
            GET  /me/children
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe
```

---

## Example 298

**Intent:**
classifieds website for my country like craigslist

**Spec:**
```
Type:       Web application (classifieds)
Auth:       Email + password with phone verification
Data model: User(id, email, phone, password_hash)
            Category(id, name, parent_id -> Category)
            Ad(id, user_id -> User, category_id -> Category, title, body, price, city, photos, expires_at, status)
Features:   - Post ads in nested categories
            - Search ads by keyword, city and price
            - Contact sellers through a relay email
            - Expire ads after 30 days
            - Let users renew or delete their ads
API:        REST
            GET  /ads?q=&city=&category=
            POST /ads
            POST /ads/{id}/contact
            POST /ads/{id}/renew
            DELETE /ads/{id}
Storage:    PostgreSQL, S3 (photos)
Tech stack: PHP, Laravel, Meilisearch
```

---

## Example 299

**Intent:**
an api-backed site where devs share code snippets with syntax highlighting

**Spec:**
```
Type:       Web application (code snippet sharing)
Auth:       GitHub sign-in
Data model: User(id, github_username)
            Snippet(id, user_id -> User, title, language, code, is_public, created_at)
            Star(user_id -> User, snippet_id -> Snippet)
Features:   - Paste code with automatic syntax highlighting
            - Make snippets public or secret by link
            - Star and fork snippets
            - Search by language and keyword
            - Embed snippets on other sites
API:        REST
            GET  /snippets?lang=
            POST /snippets
            GET  /snippets/{id}
            POST /snippets/{id}/star
            POST /snippets/{id}/fork
Storage:    PostgreSQL
Tech stack: Go, Fiber, Chroma, Svelte
```

---

## Example 300

**Intent:**
crowdfunding for open source maintainers

**Spec:**
```
Type:       Web application (open source funding)
Auth:       GitHub OAuth sign-in
Data model: Maintainer(id, github_username, stripe_account_id)
            Project(id, maintainer_id -> Maintainer, repo, monthly_goal_cents)
            Sponsorship(id, project_id -> Project, sponsor_email, amount_cents, recurring, status)
            Expense(id, project_id -> Project, description, amount_cents)
Features:   - Create a funding page for a GitHub repository
            - Accept one-time and monthly sponsorships
            - Show a progress bar toward the monthly goal
            - Publish expenses openly
            - Show sponsor logos in a README badge
API:        REST
            GET  /projects/{repo}
            POST /projects
            POST /projects/{id}/sponsor
            POST /projects/{id}/expenses
            GET  /badges/{repo}.svg
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Stripe Connect, GitHub API
```

---

## Example 301

**Intent:**
My kid's school PTA wants an online place to sell uniforms secondhand and run the bake sale preorders. Can you plan this?

**Spec:**
```
Type:       Web application (school PTA shop)
Auth:       Parent login with email + password, PTA volunteer role
Data model: Parent(id, name, email, password_hash)
            UniformItem(id, seller_id -> Parent, type, size, price, status)
            BakeSale(id, date, preorder_deadline)
            BakeItem(id, sale_id -> BakeSale, name, price, quantity)
            Preorder(id, parent_id -> Parent, sale_id -> BakeSale, items_json, paid)
Features:   - List used uniforms by type and size
            - Reserve uniforms and pay online
            - Preorder bake sale items before the deadline
            - Give volunteers a pickup list by class
            - Send all money to the PTA account
API:        REST
            GET  /uniforms?size=
            POST /uniforms
            POST /uniforms/{id}/reserve
            GET  /bake-sales/{id}
            POST /bake-sales/{id}/preorders
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 302

**Intent:**
AI chatbot for my online course that answers questions from the lecture content

**Spec:**
```
Type:       Web application (AI course assistant)
Auth:       Uses the course platform login (LTI 1.3 launch)
Data model: Course(id, lti_context_id, title)
            LectureChunk(id, course_id -> Course, lecture_title, timestamp, text, embedding)
            Question(id, course_id -> Course, student_id, text, answer, created_at)
Features:   - Import lecture transcripts and slides
            - Answer questions using retrieved lecture chunks
            - Link answers to the exact lecture timestamp
            - Show the instructor the most asked questions
            - Refuse to give answers to graded quizzes
API:        REST
            POST /lti/launch
            POST /courses/{id}/ingest
            POST /courses/{id}/ask
            GET  /courses/{id}/faq
Storage:    PostgreSQL with pgvector
Tech stack: Python, FastAPI, PyLTI1p3, OpenAI API
```

---

## Example 303

**Intent:**
site where musicians post covers and others vote, monthly challenge song

**Spec:**
```
Type:       Web application (music challenge community)
Auth:       Email + password or Google sign-in
Data model: Musician(id, name, email, instrument)
            Challenge(id, song_title, month, ends_at)
            Cover(id, challenge_id -> Challenge, musician_id -> Musician, video_url, description)
            Vote(cover_id -> Cover, musician_id -> Musician)
Features:   - Announce a challenge song each month
            - Submit a cover as a YouTube link
            - Vote for favourite covers
            - Show the winner and past challenges
            - Comment on covers
API:        REST
            GET  /challenges/current
            POST /challenges/{id}/covers
            POST /covers/{id}/vote
            GET  /challenges
Storage:    PostgreSQL
Tech stack: Node.js, Express, Svelte, YouTube embeds
```

---

## Example 304

**Intent:**
course platform built with moodle

**Spec:**
```
Type:       Web application (learning management system)
Auth:       Moodle accounts with email self-registration
Data model: Course(id, fullname, category)
            User(id, email, firstname, lastname)
            Enrolment(course_id -> Course, user_id -> User, role)
            Grade(user_id -> User, item_id, grade)
Features:   - Create courses with lessons, quizzes and assignments
            - Enrol students manually or by payment
            - Grade assignments with rubrics
            - Issue badges and certificates on completion
            - Track student progress
API:        REST (Moodle Web Services)
            POST /webservice/rest/server.php?wsfunction=core_course_get_courses
Storage:    MariaDB, Moodle data directory
Tech stack: Moodle, PHP, Docker
```

---

## Example 305

**Intent:**
a site for local bands to post gigs so people know whats on this weekend

**Spec:**
```
Type:       Web application (gig listings)
Auth:       Band accounts with email + password
Data model: Band(id, name, genre, email, password_hash, links)
            Venue(id, name, address)
            Gig(id, band_id -> Band, venue_id -> Venue, starts_at, ticket_price, ticket_url)
Features:   - Let bands post gigs with venue and time
            - Show this weekend's gigs on the home page
            - Filter by genre and price
            - Add gigs to a calendar
            - Show each band's upcoming gigs
API:        REST
            GET  /gigs?from=&to=&genre=
            POST /gigs
            GET  /bands/{id}
            GET  /gigs/{id}.ics
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Turbo
```

---

## Example 306

**Intent:**
i want to make reviewing platform for beauty products, with ingredients

**Spec:**
```
Type:       Web application (product review site)
Auth:       Email + password
Data model: User(id, username, email, password_hash, skin_type)
            Product(id, brand, name, category, ingredients)
            Ingredient(id, name, function, irritant)
            Review(id, product_id -> Product, user_id -> User, rating, body, skin_type)
Features:   - Show the ingredient list for each product
            - Flag common irritants in the list
            - Write reviews tagged with skin type
            - Filter reviews by skin type
            - Search products without a chosen ingredient
API:        REST
            GET  /products?exclude_ingredient=
            GET  /products/{id}
            POST /products/{id}/reviews
            GET  /ingredients/{id}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 307

**Intent:**
kanban + chat for remote teams in one, using supabase realtime

**Spec:**
```
Type:       Web application (team collaboration)
Auth:       Supabase Auth (magic link)
Data model: Team(id, name)
            Profile(id, team_id -> Team, name)
            Board(id, team_id -> Team, name)
            Card(id, board_id -> Board, title, column, assignee_id -> Profile, position)
            Message(id, team_id -> Team, card_id -> Card, author_id -> Profile, body, created_at)
Features:   - Move cards across board columns
            - Chat in a team channel
            - Open a chat thread on any card
            - Update boards and chat live with Supabase Realtime
            - Mention teammates to notify them
Storage:    Supabase (PostgreSQL with row-level security)
Tech stack: Supabase, React, Supabase Realtime
```

---

## Example 308

**Intent:**
blog for my nonprofit with donate button in every post

**Spec:**
```
Type:       Web application (nonprofit blog)
Auth:       Admin login for staff
Data model: Post(id, title, slug, body, image_url, campaign_id -> Campaign, published_at)
            Campaign(id, name, stripe_price_id)
            Donation(id, campaign_id -> Campaign, amount_cents, donor_email, created_at)
Features:   - Publish stories from the field
            - Add a donate button linked to a campaign on each post
            - Show how much each post has raised
            - Accept monthly donations
            - Send donors a thank-you email
API:        REST
            GET  /posts
            GET  /posts/{slug}
            POST /donate
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: Python, Wagtail, Stripe
```

---

## Example 309

**Intent:**
website for language school, students see their timetable and teachers mark attendance

**Spec:**
```
Type:       Web application (school management)
Auth:       Email + password, roles: student, teacher, admin
Data model: Student(id, name, email, password_hash, level)
            Teacher(id, name, email, password_hash)
            Group(id, level, teacher_id -> Teacher, room)
            Lesson(id, group_id -> Group, starts_at)
            Attendance(lesson_id -> Lesson, student_id -> Student, present)
Features:   - Show each student their weekly timetable
            - Let teachers mark attendance per lesson
            - Warn admins when attendance drops below 80%
            - Move students between groups
            - Print attendance certificates
API:        REST
            GET  /me/timetable
            GET  /lessons/{id}/attendance
            PUT  /lessons/{id}/attendance
            GET  /admin/low-attendance
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Thymeleaf
```

---

## Example 310

**Intent:**
Hacker community site where members post their side projects and get feedback, also monthly demo day voting

**Spec:**
```
Type:       Web application (maker community)
Auth:       GitHub sign-in
Data model: Maker(id, github_username, name)
            SideProject(id, maker_id -> Maker, title, pitch, url, stage)
            FeedbackComment(id, project_id -> SideProject, maker_id -> Maker, body)
            DemoDay(id, month)
            DemoVote(demo_day_id -> DemoDay, project_id -> SideProject, maker_id -> Maker)
Features:   - Post side projects with a short pitch and link
            - Ask for specific feedback and comment
            - Enter projects into monthly demo day
            - Vote for 3 projects each demo day
            - Show past winners
API:        REST
            GET  /projects
            POST /projects
            POST /projects/{id}/feedback
            POST /demo-days/{id}/entries
            POST /demo-days/{id}/votes
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 311

**Intent:**
quora clone

**Spec:**
```
Type:       Web application (Q&A community)
Auth:       Email + password or Google sign-in
Data model: User(id, name, email, credentials, bio)
            Topic(id, name)
            Question(id, user_id -> User, title, topic_ids, created_at)
            Answer(id, question_id -> Question, user_id -> User, body, upvotes)
            TopicFollow(user_id -> User, topic_id -> Topic)
Features:   - Ask questions tagged with topics
            - Write long-form answers with images
            - Upvote answers
            - Follow topics and see a personalised feed
            - Request answers from specific users
API:        REST
            GET  /feed
            POST /questions
            POST /questions/{id}/answers
            POST /answers/{id}/upvote
            POST /topics/{id}/follow
Storage:    PostgreSQL
Tech stack: Python, Django, React
```

---

## Example 312

**Intent:**
site 2 sell my crochet patterns + show my finished stuff

**Spec:**
```
Type:       Web application (pattern shop and portfolio)
Auth:       Admin login for the owner, buyers check out as guests
Data model: Pattern(id, name, difficulty, yarn_weight, price_cents, pdf_key, photos)
            Finished(id, title, photo_url, pattern_id -> Pattern)
            Order(id, email, pattern_id -> Pattern, paid_at)
Features:   - Show finished pieces in a gallery
            - Sell PDF patterns with instant download
            - Filter patterns by difficulty and yarn weight
            - Link gallery pieces to their pattern
API:        REST
            GET  /patterns
            POST /checkout
            GET  /gallery
            GET  /download/{token}
Storage:    SQLite, S3 (PDFs)
Tech stack: Next.js, Stripe, Vercel
```

---

## Example 313

**Intent:**
tool that makes a newsletter automatically from my teams slack highlights every friday

**Spec:**
```
Type:       Web application (AI newsletter generator)
Auth:       Slack OAuth
Data model: Workspace(id, slack_team_id, bot_token)
            WatchedChannel(id, workspace_id -> Workspace, channel_id)
            Issue(id, workspace_id -> Workspace, week, draft_html, status, sent_at)
Features:   - Collect messages with a chosen emoji reaction from selected channels
            - Summarise the week's highlights with an LLM
            - Let a manager edit the draft
            - Email the newsletter to the team every Friday
            - Keep an archive of past issues
API:        REST
            GET  /slack/oauth/callback
            POST /channels
            GET  /issues/{id}
            PUT  /issues/{id}
            POST /issues/{id}/send
Storage:    PostgreSQL
Tech stack: Python, Flask, Slack Web API, OpenAI API, APScheduler
```

---

## Example 314

**Intent:**
i need volunteer tracking for a hospital, hours, background checks, departments

**Spec:**
```
Type:       Web application (hospital volunteer management)
Auth:       Email + password, roles: volunteer and coordinator
Data model: Volunteer(id, name, email, password_hash, phone, background_check_status, check_expires_on)
            Department(id, name, supervisor)
            Shift(id, department_id -> Department, starts_at, ends_at)
            HoursLog(id, volunteer_id -> Volunteer, shift_id -> Shift, clock_in, clock_out)
Features:   - Track background check status and expiry
            - Block shift sign-up when a check has expired
            - Clock in and out at a kiosk
            - Report hours per department
            - Remind volunteers before checks expire
API:        REST
            GET  /shifts
            POST /shifts/{id}/signup
            POST /kiosk/clock
            GET  /reports/hours?department=
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Blazor
```

---

## Example 315

**Intent:**
marketplace for used bikes

**Spec:**
```
Type:       Web application (marketplace)
Auth:       Email + password
Data model: User(id, name, email, password_hash, city)
            Bike(id, seller_id -> User, brand, type, frame_size, year, price, serial_number, photos, status)
            Message(id, bike_id -> Bike, sender_id -> User, body)
Features:   - List bikes with frame size, type and photos
            - Check the serial number against a stolen bike register
            - Filter by type, frame size and city
            - Message sellers
            - Mark bikes as sold
API:        REST
            GET  /bikes?type=&size=
            POST /bikes
            POST /bikes/{id}/messages
            PATCH /bikes/{id}
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, Bike Index API
```

---

## Example 316

**Intent:**
Ich brauche eine Webseite für unseren Sportverein, mit Mitglieder, Beiträge und Trainingszeiten (please answer in english)

**Spec:**
```
Type:       Web application (sports club management)
Auth:       Email + password, roles: member, trainer, board
Data model: Member(id, name, email, password_hash, birth_date, iban, membership_type)
            Fee(id, member_id -> Member, year, amount, paid)
            Training(id, team, weekday, time, location, trainer_id -> Member)
Features:   - Manage the member list and membership types
            - Collect yearly fees by SEPA direct debit
            - Show training times per team
            - Send newsletters to members
            - Export member data for the association register
API:        REST
            GET  /members
            POST /members
            GET  /trainings
            POST /fees/collect
            GET  /export.csv
Storage:    PostgreSQL
Tech stack: PHP, Symfony, SEPA XML library
```

---

## Example 317

**Intent:**
online course platform for musicians with practice tracking

**Spec:**
```
Type:       Web application (music education platform)
Auth:       Email + password
Data model: Student(id, email, password_hash, instrument)
            Course(id, title, instrument, level)
            Lesson(id, course_id -> Course, title, video_url, sheet_url, backing_track_url)
            PracticeSession(id, student_id -> Student, lesson_id -> Lesson, minutes, tempo_bpm, date)
Features:   - Watch lessons with sheet music and backing tracks
            - Log practice time and tempo reached
            - Show a practice streak and weekly minutes
            - Slow down backing tracks without changing pitch
            - Recommend the next lesson
API:        REST
            GET  /courses?instrument=
            GET  /lessons/{id}
            POST /practice
            GET  /me/stats
Storage:    PostgreSQL, S3 (media)
Tech stack: TypeScript, React, Tone.js, Node.js, Express
```

---

## Example 318

**Intent:**
website for neighborhood watch alerts

**Spec:**
```
Type:       Web application (community alerts)
Auth:       Email + password with address verification by a coordinator
Data model: Resident(id, name, email, phone, street, verified)
            Alert(id, author_id -> Resident, category, description, location, created_at)
            AlertComment(id, alert_id -> Alert, author_id -> Resident, body)
Features:   - Post alerts like suspicious activity or lost keys
            - Send SMS and email to verified residents nearby
            - Comment on alerts
            - Hide alerts from unverified users
            - Remind people to call the police in emergencies
API:        REST
            GET  /alerts
            POST /alerts
            POST /alerts/{id}/comments
            PATCH /admin/residents/{id}
Storage:    PostgreSQL
Tech stack: Node.js, Express, Twilio, React
```

---

## Example 319

**Intent:**
wiki 4 my programming notes, private, markdown

**Spec:**
```
Type:       Web application (personal wiki)
Auth:       Single-user password login
Data model: Note(id, path, title, body_markdown, updated_at)
            Tag(id, name)
            NoteTag(note_id -> Note, tag_id -> Tag)
Features:   - Write notes in Markdown with code highlighting
            - Organise notes in folders
            - Tag and search notes
            - Back up notes to a Git repository nightly
API:        REST
            GET  /notes?q=
            GET  /notes/{path}
            PUT  /notes/{path}
            DELETE /notes/{path}
Storage:    SQLite, Git repository (backup)
Tech stack: Python, FastAPI, Markdown, Pygments
```

---

## Example 320

**Intent:**
a social site for gardeners to show their gardens through the seasons

**Spec:**
```
Type:       Web application (gardening social network)
Auth:       Email + password
Data model: Gardener(id, name, email, password_hash, climate_zone)
            Garden(id, gardener_id -> Gardener, name, size_m2)
            Snapshot(id, garden_id -> Garden, photo_url, season, year, note)
            Follow(follower_id -> Gardener, garden_id -> Garden)
            Comment(id, snapshot_id -> Snapshot, gardener_id -> Gardener, body)
Features:   - Post seasonal photos of a garden
            - Show a before-and-after timeline per garden
            - Follow gardens and comment
            - Filter gardens by climate zone
            - Tag plants in photos
API:        REST
            POST /gardens
            POST /gardens/{id}/snapshots
            GET  /gardens/{id}/timeline
            POST /gardens/{id}/follow
            GET  /feed
Storage:    PostgreSQL, S3 (photos)
Tech stack: Ruby on Rails, Active Storage
```

---

## Example 321

**Intent:**
job board for people with disabilities, accessible employers

**Spec:**
```
Type:       Web application (inclusive job board)
Auth:       Email + password, roles: employer and seeker
Data model: Employer(id, name, email, password_hash, accessibility_commitments)
            Job(id, employer_id -> Employer, title, location, remote, accommodations, salary_range)
            Seeker(id, name, email, password_hash, preferences)
            Application(job_id -> Job, seeker_id -> Seeker, status)
Features:   - List accommodations offered for each job
            - Filter by remote, part-time and accommodations
            - Apply with a stored profile
            - Build the site to WCAG 2.2 AA with full keyboard and screen reader support
            - Show employer accessibility commitments
API:        REST
            GET  /jobs?accommodation=&remote=
            POST /jobs
            POST /jobs/{id}/apply
            GET  /employers/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, server-rendered HTML
```

---

## Example 322

**Intent:**
build me a website that lets my coworkers swap shifts, nurses mostly

**Spec:**
```
Type:       Web application (shift swap)
Auth:       Employee number + password
Data model: Employee(id, employee_no, name, unit, role)
            Shift(id, employee_id -> Employee, unit, starts_at, ends_at)
            SwapRequest(id, shift_id -> Shift, offered_by -> Employee, taken_by -> Employee, status, approved_by)
Features:   - Post a shift you want to give away
            - Take a shift posted by a coworker with the same role
            - Require manager approval for each swap
            - Notify both employees when approved
            - Show the updated roster
API:        REST
            GET  /swaps/open
            POST /shifts/{id}/swap
            POST /swaps/{id}/take
            POST /swaps/{id}/approve
            GET  /roster
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Vue.js
```

---

## Example 323

**Intent:**
site to rate local takeaways and order from them

**Spec:**
```
Type:       Web application (food ordering and reviews)
Auth:       Email + password for customers and restaurant owners
Data model: Restaurant(id, name, cuisine, address, delivery_radius_km, owner_id -> User)
            MenuItem(id, restaurant_id -> Restaurant, name, price)
            Order(id, restaurant_id -> Restaurant, customer_id -> User, items_json, total, status)
            Review(id, restaurant_id -> Restaurant, customer_id -> User, rating, body)
            User(id, email, password_hash, role)
Features:   - Browse takeaways by cuisine and rating
            - Order from the menu and pay online
            - Let restaurants accept and update order status
            - Review only after a completed order
            - Show delivery radius
API:        REST
            GET  /restaurants?cuisine=
            GET  /restaurants/{id}/menu
            POST /orders
            PATCH /orders/{id}
            POST /restaurants/{id}/reviews
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, React, Stripe
```

---

## Example 324

**Intent:**
notion style docs + comments + mentions, but in angular

**Spec:**
```
Type:       Web application (collaborative docs)
Auth:       Email + password
Data model: User(id, name, email, password_hash)
            Doc(id, owner_id -> User, title, content_json, updated_at)
            DocShare(doc_id -> Doc, user_id -> User, permission)
            Comment(id, doc_id -> Doc, user_id -> User, anchor, body, resolved)
            Mention(id, comment_id -> Comment, user_id -> User)
Features:   - Write docs in a block editor
            - Share docs with view, comment or edit rights
            - Comment on selected text
            - Mention teammates with @ and notify them
            - Resolve comment threads
API:        REST
            GET  /docs
            POST /docs
            PUT  /docs/{id}
            POST /docs/{id}/share
            POST /docs/{id}/comments
Storage:    PostgreSQL
Tech stack: TypeScript, Angular, Node.js, NestJS, Quill
```

---

## Example 325

**Intent:**
my students make podcasts, need a place to publish them for class, private

**Spec:**
```
Type:       Web application (private class podcast platform)
Auth:       Teacher account, students log in with school Google accounts
Data model: Class(id, teacher_email, name)
            Student(id, google_id, name, class_id -> Class)
            Episode(id, class_id -> Class, student_id -> Student, title, audio_url, published, created_at)
            Comment(id, episode_id -> Episode, student_id -> Student, body)
Features:   - Upload podcast episodes as audio files
            - Let the teacher approve episodes before classmates hear them
            - Play episodes in the browser
            - Comment on classmates' episodes
            - Keep everything visible only to the class
API:        REST
            GET  /classes/{id}/episodes
            POST /episodes
            PATCH /episodes/{id}
            POST /episodes/{id}/comments
Storage:    PostgreSQL, Google Cloud Storage
Tech stack: Python, Flask, Google Identity
```

---

## Example 326

**Intent:**
site where small businesses get matched with student interns for summer projects

**Spec:**
```
Type:       Web application (internship matching)
Auth:       Email + password, roles: business and student
Data model: Business(id, name, email, password_hash, sector)
            Project(id, business_id -> Business, title, description, skills, weeks, paid)
            Student(id, name, email, password_hash, university, skills, cv_url)
            Application(project_id -> Project, student_id -> Student, cover_note, status)
Features:   - Post summer projects with skills and duration
            - Recommend projects to students by skills
            - Apply with a short cover note
            - Let businesses shortlist and accept
            - Collect feedback from both sides at the end
API:        REST
            GET  /projects?skill=
            POST /projects
            POST /projects/{id}/applications
            PATCH /applications/{id}
            POST /projects/{id}/feedback
Storage:    PostgreSQL
Tech stack: Node.js, Express, Next.js
```

---

## Example 327

**Intent:**
comment section with ai that summarises the discussion for news articles

**Spec:**
```
Type:       Web application (comments with AI summaries)
Auth:       Email + password for commenters
Data model: Article(id, url, title)
            Comment(id, article_id -> Article, user_id -> User, parent_id -> Comment, body, likes)
            User(id, username, email, password_hash)
            DiscussionSummary(article_id -> Article, summary, viewpoints_json, updated_at)
Features:   - Post and reply to comments under an article
            - Summarise the main viewpoints with an LLM
            - Update the summary every 50 new comments
            - Show the summary above the comments
            - Moderate comments with a report button
API:        REST
            GET  /articles/{id}/comments
            POST /articles/{id}/comments
            GET  /articles/{id}/summary
            POST /comments/{id}/report
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Anthropic Claude API, Preact widget
```

---

## Example 328

**Intent:**
forum for ex-pats from India living in Canada

**Spec:**
```
Type:       Web application (diaspora community forum)
Auth:       Email + password or Google sign-in
Data model: Member(id, name, email, home_state, province, city)
            Category(id, name)
            Thread(id, category_id -> Category, member_id -> Member, title, province)
            Post(id, thread_id -> Thread, member_id -> Member, body)
Features:   - Discuss in categories like Immigration, Jobs, Housing and Festivals
            - Filter threads by province
            - Post local community events
            - Find members from the same home state
API:        REST
            GET  /threads?category=&province=
            POST /threads
            POST /threads/{id}/posts
            GET  /members?home_state=
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 329

**Intent:**
give me spec: subscription box company website, customers pick box and skip months

**Spec:**
```
Type:       Web application (subscription box store)
Auth:       Email + password
Data model: Customer(id, email, password_hash, address, stripe_customer_id)
            Plan(id, name, price_cents, interval)
            Subscription(id, customer_id -> Customer, plan_id -> Plan, status, next_ship_on)
            Skip(subscription_id -> Subscription, month)
Features:   - Choose a box plan and subscribe
            - Skip upcoming months
            - Pause or cancel from the account page
            - Charge automatically before each shipment
            - Give the warehouse a monthly packing list
API:        REST
            GET  /plans
            POST /subscriptions
            POST /subscriptions/{id}/skip
            PATCH /subscriptions/{id}
            GET  /admin/packing-list
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe Billing
```

---

## Example 330

**Intent:**
social reading app where friends highlight passages of ebooks and see each others highlights

**Spec:**
```
Type:       Web application (social reading)
Auth:       Email + password
Data model: Reader(id, name, email, password_hash)
            Book(id, title, author, epub_url)
            Highlight(id, reader_id -> Reader, book_id -> Book, cfi_range, text, note, created_at)
            Friendship(reader_id -> Reader, friend_id -> Reader)
Features:   - Read EPUB books in the browser
            - Highlight passages and add notes
            - Show friends' highlights in the margin
            - Show a feed of friends' highlights
            - Export your highlights as Markdown
API:        REST
            GET  /books/{id}
            POST /books/{id}/highlights
            GET  /books/{id}/highlights?friends=true
            GET  /feed
Storage:    PostgreSQL, S3 (EPUBs)
Tech stack: TypeScript, React, epub.js, Node.js
```

---

## Example 331

**Intent:**
wedding photo sharing site where guests upload pics from a qr code

**Spec:**
```
Type:       Web application (event photo sharing)
Auth:       Couple login, guests upload without accounts via QR link
Data model: Event(id, couple_email, name, upload_token, date)
            Photo(id, event_id -> Event, url, uploader_name, uploaded_at, hidden)
Features:   - Generate a QR code that opens the upload page
            - Let guests upload many photos from their phone
            - Show a live slideshow during the party
            - Let the couple hide photos
            - Download all photos as a ZIP
API:        REST
            POST /events
            GET  /u/{token}
            POST /u/{token}/photos
            GET  /events/{id}/photos
            GET  /events/{id}/download.zip
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, FastAPI, Svelte, qrcode
```

---

## Example 332

**Intent:**
project management tool for film productions, call sheets, shooting schedule, crew contacts

**Spec:**
```
Type:       Web application (film production management)
Auth:       Email + password, production invites
Data model: Production(id, title)
            CrewMember(id, production_id -> Production, name, department, phone, email)
            Scene(id, production_id -> Production, number, location, int_ext, day_night, pages)
            ShootDay(id, production_id -> Production, date, call_time)
            ShootDayScene(shoot_day_id -> ShootDay, scene_id -> Scene, order)
Features:   - Break the script into scenes
            - Plan shoot days by dragging scenes onto dates
            - Generate a call sheet PDF for each day
            - Email call sheets to the crew
            - Keep a crew contact list by department
API:        REST
            POST /productions/{id}/scenes
            POST /shoot-days
            PUT  /shoot-days/{id}/scenes
            GET  /shoot-days/{id}/call-sheet.pdf
            POST /shoot-days/{id}/send
Storage:    PostgreSQL
Tech stack: Python, Django, WeasyPrint, React
```

---

## Example 333

**Intent:**
website for elderly people to find someone to chat with on the phone, like a friendly call service

**Spec:**
```
Type:       Web application (befriending service)
Auth:       Volunteers register with email + password and pass a check, older people sign up by phone with a coordinator
Data model: Volunteer(id, name, email, phone, languages, availability, approved)
            Senior(id, name, phone, interests, preferred_times)
            Pairing(id, volunteer_id -> Volunteer, senior_id -> Senior, weekly_slot, status)
            CallLog(id, pairing_id -> Pairing, called_at, minutes, notes)
Features:   - Pair seniors with approved volunteers by interests and times
            - Show volunteers their weekly call schedule
            - Log each call and any concerns
            - Alert the coordinator about welfare concerns
            - Hide seniors' phone numbers using a call relay
API:        REST
            POST /volunteers
            POST /admin/seniors
            POST /admin/pairings
            POST /pairings/{id}/calls
            GET  /admin/concerns
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Twilio Voice
```

---

## Example 334

**Intent:**
saas for schools to run parents evening bookings

**Spec:**
```
Type:       Web application (multi-tenant booking SaaS)
Auth:       Email + password for school staff, parents log in with a code from the school
Data model: School(id, name, subdomain)
            Teacher(id, school_id -> School, name, email)
            Evening(id, school_id -> School, date, slot_minutes)
            Slot(id, evening_id -> Evening, teacher_id -> Teacher, starts_at, parent_name, student_name)
Features:   - Create an evening with slot length per school
            - Let parents book one slot with each of their child's teachers
            - Prevent overlapping bookings for a parent
            - Give each teacher a printable schedule
            - Support video calls for remote meetings
API:        REST
            POST /evenings
            GET  /evenings/{id}/slots?teacher=
            POST /slots/{id}/book
            GET  /teachers/{id}/schedule
Storage:    PostgreSQL with schema per tenant
Tech stack: Python, Django, django-tenants, Jitsi
```

---

## Example 335

**Intent:**
a reviews site for coding bootcamps with verified graduate reviews

**Spec:**
```
Type:       Web application (review site)
Auth:       LinkedIn sign-in to verify graduates
Data model: Bootcamp(id, name, website, locations, price, length_weeks)
            Graduate(id, name, linkedin_url, bootcamp_id -> Bootcamp, graduated_on, verified)
            Review(id, bootcamp_id -> Bootcamp, graduate_id -> Graduate, curriculum, instructors, job_support, overall, body, got_job)
Features:   - List bootcamps with price, length and locations
            - Write reviews with separate scores
            - Verify graduates through LinkedIn education history
            - Show the share of reviewers who got a job
            - Let bootcamps respond to reviews
API:        REST
            GET  /bootcamps
            GET  /bootcamps/{id}/reviews
            POST /bootcamps/{id}/reviews
            POST /reviews/{id}/response
Storage:    PostgreSQL
Tech stack: Node.js, Express, React
```

---

## Example 336

**Intent:**
something for my writing group to submit poems weekly and critique each other

**Spec:**
```
Type:       Web application (writing workshop)
Auth:       Email + password, invite only
Data model: Writer(id, name, email, password_hash)
            Week(id, starts_on, prompt)
            Submission(id, week_id -> Week, writer_id -> Writer, title, body)
            Critique(id, submission_id -> Submission, writer_id -> Writer, body, line_notes_json)
Features:   - Post a weekly prompt
            - Submit one poem per week
            - Critique others' poems with line-by-line notes
            - Hide critiques until the author opens them
            - Show each writer's archive
API:        REST
            GET  /weeks/current
            POST /weeks/{id}/submissions
            POST /submissions/{id}/critiques
            GET  /writers/{id}/archive
Storage:    SQLite
Tech stack: Python, Flask, Alpine.js
```

---

## Example 337

**Intent:**
crowdfunding platform with equity for startups

**Spec:**
```
Type:       Web application (equity crowdfunding)
Auth:       Email + password with KYC identity verification for investors
Data model: Investor(id, name, email, password_hash, kyc_status, accredited)
            Startup(id, name, pitch, valuation, target_amount, min_investment, closes_on)
            Investment(id, startup_id -> Startup, investor_id -> Investor, amount, shares, status)
            Document(id, startup_id -> Startup, title, file_url)
Features:   - Verify investor identity before investing
            - Show startup pitches, documents and terms
            - Enforce minimum investment and investor limits
            - Hold funds in escrow until the round closes
            - Issue share certificates when the round succeeds
API:        REST
            GET  /startups
            GET  /startups/{id}
            POST /startups/{id}/investments
            POST /kyc
            GET  /me/portfolio
Storage:    PostgreSQL, S3 (documents)
Tech stack: Java, Spring Boot, React, Onfido API
```

---

## Example 338

**Intent:**
website for a mosque with prayer times, events and donations

**Spec:**
```
Type:       Web application (community site)
Auth:       Admin login for committee members
Data model: PrayerTimetable(date, fajr, dhuhr, asr, maghrib, isha, jummah)
            Event(id, title, starts_at, description)
            Donation(id, fund, amount_cents, donor_email, recurring, created_at)
Features:   - Show daily prayer times from an uploaded yearly timetable
            - List events and classes
            - Accept one-time and monthly donations to different funds
            - Display prayer times on a screen in the mosque
            - Send event announcements by email
API:        REST
            GET  /prayer-times?date=
            POST /admin/timetable
            GET  /events
            POST /donations
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 339

**Intent:**
app for my coding club where members do weekly challenges and get points

**Spec:**
```
Type:       Web application (coding challenge club)
Auth:       GitHub sign-in
Data model: Member(id, github_username, points)
            Challenge(id, title, description, tests, week, points)
            Submission(id, challenge_id -> Challenge, member_id -> Member, code, language, passed, submitted_at)
Features:   - Post a weekly coding challenge
            - Run submissions against tests in a sandbox
            - Award points for passing and bonus points for first solve
            - Show a season leaderboard
            - Show solutions after the week ends
API:        REST
            GET  /challenges/current
            POST /challenges/{id}/submissions
            GET  /leaderboard
            GET  /challenges/{id}/solutions
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Docker sandbox, Svelte
```

---

## Example 340

**Intent:**
blog where readers can pay to unlock premium posts with crypto

**Spec:**
```
Type:       Web application (paywalled blog)
Auth:       Wallet sign-in (Sign-In with Ethereum)
Data model: Reader(id, wallet_address)
            Post(id, title, slug, preview, body, price_usdc, premium)
            Unlock(reader_id -> Reader, post_id -> Post, tx_hash, unlocked_at)
Features:   - Show free previews of premium posts
            - Pay in USDC to unlock a post
            - Verify the payment transaction on-chain
            - Remember unlocked posts for the wallet
            - Let the author see earnings
API:        REST
            GET  /posts
            GET  /posts/{slug}
            POST /auth/siwe
            POST /posts/{id}/unlock
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, viem, SIWE
```

---

## Example 341

**Intent:**
internal tool for our marketing team to request designs from the design team

**Spec:**
```
Type:       Web application (request management)
Auth:       Google Workspace sign-in
Data model: Employee(id, name, email, team)
            DesignRequest(id, requester_id -> Employee, title, brief, format, due_date, priority, status, assignee_id -> Employee)
            Asset(id, request_id -> DesignRequest, file_url, version)
            Comment(id, request_id -> DesignRequest, author_id -> Employee, body)
Features:   - Submit design requests with a brief, format and due date
            - Triage and assign requests to designers
            - Upload drafts as versions
            - Approve or request changes
            - Show the design team's workload
API:        REST
            POST /requests
            GET  /requests?status=
            PATCH /requests/{id}
            POST /requests/{id}/assets
            POST /requests/{id}/comments
Storage:    PostgreSQL, Google Drive (files)
Tech stack: Node.js, Express, React, Google Drive API
```

---

## Example 342

**Intent:**
car sharing between neighbours website

**Spec:**
```
Type:       Web application (peer-to-peer car sharing)
Auth:       Email + password with driving licence verification
Data model: Member(id, name, email, password_hash, licence_verified)
            Car(id, owner_id -> Member, make, model, seats, price_per_hour, location)
            Booking(id, car_id -> Car, renter_id -> Member, starts_at, ends_at, km_start, km_end, total, status)
Features:   - List a car with hourly price and location
            - Book a car for a time window
            - Record odometer readings at pickup and return
            - Charge by hour plus kilometres driven
            - Verify driving licences before booking
API:        REST
            GET  /cars?near=
            POST /cars
            POST /cars/{id}/bookings
            POST /bookings/{id}/start
            POST /bookings/{id}/end
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe, Onfido
```

---

## Example 343

**Intent:**
im a tattoo artist n want a site where ppl send me ideas and i send quote back

**Spec:**
```
Type:       Web application (quote request portal)
Auth:       Artist admin login, clients use a private link per request
Data model: Request(id, name, email, idea, placement, size_cm, reference_images, budget, status, token)
            Quote(id, request_id -> Request, price, sessions, message, deposit_cents)
Features:   - Collect tattoo ideas with placement, size and reference images
            - Reply with a quote and number of sessions
            - Let the client accept and pay a deposit
            - Show the artist all requests by status
            - Email the client when a quote is ready
API:        REST
            POST /requests
            GET  /r/{token}
            POST /admin/requests/{id}/quote
            POST /r/{token}/accept
Storage:    PostgreSQL, S3 (images)
Tech stack: Next.js, Stripe, Resend
```

---

## Example 344

**Intent:**
education platform where teachers make interactive flashcard decks and share them

**Spec:**
```
Type:       Web application (flashcard platform)
Auth:       Email + password or Google sign-in
Data model: User(id, email, name)
            Deck(id, owner_id -> User, title, subject, is_public)
            Card(id, deck_id -> Deck, front, back, image_url)
            Review(id, user_id -> User, card_id -> Card, ease, due_on)
Features:   - Create decks of cards with text and images
            - Share decks publicly or with a class code
            - Study with spaced repetition scheduling
            - Copy and edit someone else's public deck
            - Show which cards students struggle with
API:        REST
            GET  /decks?subject=
            POST /decks
            POST /decks/{id}/cards
            GET  /study/due
            POST /cards/{id}/review
Storage:    PostgreSQL
Tech stack: Python, Django, React
```

---

## Example 345

**Intent:**
newsletter about local real estate, auto generated from listings data each week

**Spec:**
```
Type:       Web application (automated newsletter)
Auth:       Admin login, subscribers by email only
Data model: Subscriber(id, email, areas, confirmed)
            ListingSnapshot(id, area, week, median_price, new_listings, avg_days_on_market)
            Issue(id, week, html, sent_at)
Features:   - Import listing data weekly from a feed
            - Compute median price and days on market per area
            - Generate a newsletter with charts per subscriber area
            - Write a short commentary with an LLM for admin review
            - Send to confirmed subscribers
API:        REST
            POST /subscribe
            GET  /issues
            POST /admin/issues/{id}/approve
Storage:    PostgreSQL
Tech stack: Python, pandas, matplotlib, Django, Amazon SES
```

---

## Example 346

**Intent:**
Platform for climbing gyms where climbers log routes they sent

**Spec:**
```
Type:       Web application (climbing logbook)
Auth:       Email + password, gym staff role
Data model: Gym(id, name, city)
            Route(id, gym_id -> Gym, wall, grade, colour, setter, set_on, removed_on)
            Climber(id, name, email, password_hash)
            Ascent(id, route_id -> Route, climber_id -> Climber, style, sent_on, rating)
Features:   - Let gym staff post new routes with grade and wall
            - Log ascents as flash, redpoint or attempt
            - Rate routes and suggest grades
            - Show personal grade pyramids
            - Hide routes after they are stripped
API:        REST
            GET  /gyms/{id}/routes
            POST /gyms/{id}/routes
            POST /routes/{id}/ascents
            GET  /me/pyramid
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Chart.js
```

---

## Example 347

**Intent:**
hi i need help with web site where my customers write reviews about my dentist clinic and they appear on google too

**Spec:**
```
Type:       Web application (review collection)
Auth:       Admin login for the clinic, patients use a link from email
Data model: Patient(id, name, email, last_visit_on)
            ReviewInvite(id, patient_id -> Patient, token, sent_at)
            Review(id, invite_id -> ReviewInvite, rating, body, published, created_at)
Features:   - Email patients a review link after their visit
            - Collect star ratings and comments
            - Send happy patients on to the Google review page
            - Show private feedback to the clinic for low ratings
            - Display approved reviews on the clinic website with schema markup
API:        REST
            POST /admin/invites
            GET  /review/{token}
            POST /review/{token}
            GET  /reviews/public
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Google Business Profile link
```

---

## Example 348

**Intent:**
a minimal forum, no js

**Spec:**
```
Type:       Web application (forum)
Auth:       Username + password, session cookies
Data model: User(id, username, password_hash)
            Thread(id, user_id -> User, title, created_at, last_post_at)
            Post(id, thread_id -> Thread, user_id -> User, body, created_at)
Features:   - List threads by latest activity
            - Post threads and replies with plain HTML forms
            - Render posts with basic Markdown
            - Paginate threads
API:        REST
            GET  /
            GET  /t/{id}
            POST /t
            POST /t/{id}/reply
Storage:    SQLite
Tech stack: Go, net/http, html/template
```

---

## Example 349

**Intent:**
something where companies post open source bounties and devs claim them

**Spec:**
```
Type:       Web application (bounty marketplace)
Auth:       GitHub OAuth sign-in
Data model: Company(id, name, stripe_customer_id)
            Bounty(id, company_id -> Company, issue_url, amount_cents, status)
            Claim(id, bounty_id -> Bounty, developer_github, pr_url, status)
            Payout(id, claim_id -> Claim, amount_cents, paid_at)
Features:   - Attach a bounty to a GitHub issue
            - Let developers claim a bounty and link a pull request
            - Release payment when the pull request is merged
            - Show open bounties by language
            - Comment the bounty amount on the GitHub issue
API:        REST
            GET  /bounties?lang=
            POST /bounties
            POST /bounties/{id}/claims
            POST /webhooks/github
            POST /webhooks/stripe
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Octokit, Stripe Connect
```

---

## Example 350

**Intent:**
hey i manage a youth orchestra, need a site where students get their part sheets and practice schedule and parents pay fees

**Spec:**
```
Type:       Web application (orchestra management)
Auth:       Email + password for parents and students, admin role
Data model: Student(id, name, instrument, parent_id -> Parent)
            Parent(id, name, email, password_hash)
            Piece(id, title, composer)
            Part(id, piece_id -> Piece, instrument, pdf_url)
            Rehearsal(id, date, location, pieces)
            Fee(id, student_id -> Student, term, amount_cents, paid)
Features:   - Show each student only the parts for their instrument
            - Publish the rehearsal schedule
            - Pay term fees online
            - Send reminders before concerts
            - Track who has paid
API:        REST
            GET  /me/parts
            GET  /rehearsals
            GET  /fees
            POST /fees/{id}/pay
Storage:    PostgreSQL, S3 (sheet music)
Tech stack: Python, Django, Stripe
```

---

## Example 351

**Intent:**
marketplace for selling unused gift cards

**Spec:**
```
Type:       Web application (gift card resale marketplace)
Auth:       Email + password with phone verification
Data model: User(id, email, password_hash, phone_verified)
            GiftCard(id, seller_id -> User, brand, face_value, asking_price, code_encrypted, verified, status)
            Sale(id, card_id -> GiftCard, buyer_id -> User, paid_at, disputed)
Features:   - List gift cards at a discount
            - Check the balance with the brand before listing where supported
            - Encrypt card codes and reveal them only after payment
            - Pay sellers after a 7-day dispute window
            - Handle disputes for invalid cards
API:        REST
            GET  /cards?brand=
            POST /cards
            POST /cards/{id}/buy
            GET  /purchases/{id}/code
            POST /purchases/{id}/dispute
Storage:    PostgreSQL
Tech stack: Node.js, NestJS, Stripe, AWS KMS
```

---

## Example 352

**Intent:**
twitch style live streaming for teachers to stream classes

**Spec:**
```
Type:       Web application (live class streaming)
Auth:       Email + password, roles: teacher and student
Data model: Teacher(id, name, email, stream_key)
            Stream(id, teacher_id -> Teacher, title, subject, started_at, ended_at, vod_url)
            ChatMessage(id, stream_id -> Stream, user_id -> User, body, created_at)
            User(id, name, email, password_hash)
Features:   - Give each teacher a stream key for OBS
            - Play live streams in the browser with low latency
            - Chat during the stream with raised-hand questions
            - Save recordings for replay
            - Show which classes are live now
API:        REST and WebSocket
            GET  /streams/live
            POST /streams
            GET  /streams/{id}
            WS   /streams/{id}/chat
Storage:    PostgreSQL, S3 (recordings)
Tech stack: Node.js, Mux Live Streaming, React, Socket.IO
```

---

## Example 353

**Intent:**
wiki for nurses with drug calculation guides, offline too

**Spec:**
```
Type:       Web application (offline-capable reference wiki)
Auth:       Email + password for editors, public read
Data model: Guide(id, title, category, body, formula, updated_at)
            Revision(id, guide_id -> Guide, editor_id -> Editor, body, created_at)
            Editor(id, name, email, password_hash)
Features:   - Publish dosage calculation guides with worked examples
            - Include a calculator for each formula
            - Work offline as a progressive web app
            - Keep a reviewed revision history
            - Search guides by drug or category
API:        REST
            GET  /guides?q=
            GET  /guides/{id}
            PUT  /guides/{id}
            GET  /guides/{id}/revisions
Storage:    PostgreSQL, browser cache via service worker
Tech stack: Vue.js, Workbox, Python, FastAPI
```

---

## Example 354

**Intent:**
I'm a career coach. Can you plan a site where clients book sessions, fill in a questionnaire before, and get homework after?

**Spec:**
```
Type:       Web application (coaching portal)
Auth:       Email + password for clients, admin for the coach
Data model: Client(id, name, email, password_hash)
            Session(id, client_id -> Client, starts_at, video_link, status)
            Questionnaire(id, session_id -> Session, answers_json)
            Homework(id, session_id -> Session, task, due_on, done)
Features:   - Book sessions from the coach's availability
            - Fill in a questionnaire before the first session
            - Join sessions with a video link
            - Receive homework tasks after a session
            - Tick off homework and add reflections
API:        REST
            GET  /availability
            POST /sessions
            POST /sessions/{id}/questionnaire
            POST /sessions/{id}/homework
            PATCH /homework/{id}
Storage:    PostgreSQL
Tech stack: Python, Django, Cal.com API, Zoom API
```

---

## Example 355

**Intent:**
social platform for amateur astronomers sharing observations

**Spec:**
```
Type:       Web application (astronomy community)
Auth:       Email + password
Data model: Observer(id, name, email, password_hash, location, telescope)
            Observation(id, observer_id -> Observer, object_name, catalog_id, observed_at, seeing, notes, image_url)
            Like(observation_id -> Observation, observer_id -> Observer)
Features:   - Log observations with object, conditions and equipment
            - Upload astrophotos
            - Browse observations by object
            - Show what is visible tonight for your location
            - Like and comment on observations
API:        REST
            POST /observations
            GET  /observations?object=
            GET  /tonight?lat=&lng=
            POST /observations/{id}/like
Storage:    PostgreSQL, S3 (images)
Tech stack: Python, Django, Astropy
```

---

## Example 356

**Intent:**
web app for teams to run planning poker

**Spec:**
```
Type:       Web application (planning poker)
Auth:       No accounts, players join a room with a name
Data model: Room(id, code, moderator_token, current_story)
            Player(id, room_id -> Room, name)
            Estimate(room_id -> Room, player_id -> Player, story, value)
Features:   - Create a room and share its link
            - Vote on a story with Fibonacci cards
            - Hide votes until the moderator reveals them
            - Show the average and spread
            - Start a new round
API:        REST and WebSocket
            POST /rooms
            GET  /rooms/{code}
            WS   /rooms/{code}
Storage:    In-memory store with Redis
Tech stack: Node.js, ws, React
```

---

## Example 357

**Intent:**
forum for small business owners sharing advice with paid expert AMAs

**Spec:**
```
Type:       Web application (business community forum)
Auth:       Email + password, paid membership for AMA access
Data model: Member(id, name, email, password_hash, business_type, membership)
            Thread(id, member_id -> Member, category, title, body)
            Reply(id, thread_id -> Thread, member_id -> Member, body)
            Ama(id, expert_name, topic, starts_at, ends_at)
            AmaQuestion(id, ama_id -> Ama, member_id -> Member, question, answer, upvotes)
Features:   - Discuss in categories like Marketing, Tax and Hiring
            - Host live AMAs with experts
            - Upvote AMA questions so the best ones get answered
            - Restrict AMAs to paying members
            - Archive AMA answers
API:        REST
            GET  /threads
            POST /threads
            GET  /amas
            POST /amas/{id}/questions
            POST /ama-questions/{id}/upvote
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe
```

---

## Example 358

**Intent:**
site to sell second hand school books where the school checks condition

**Spec:**
```
Type:       Web application (school book exchange)
Auth:       Parent login with email + password, staff role
Data model: Parent(id, name, email, password_hash)
            BookTitle(id, isbn, title, grade)
            Copy(id, book_title_id -> BookTitle, seller_id -> Parent, condition, price, status)
            Purchase(id, copy_id -> Copy, buyer_id -> Parent, paid)
Features:   - Show the required book list for each grade
            - List copies for sale before drop-off
            - Let staff grade the condition at drop-off
            - Buy copies online and collect at school
            - Pay sellers after collection
API:        REST
            GET  /grades/{n}/books
            POST /copies
            PATCH /staff/copies/{id}
            POST /copies/{id}/buy
Storage:    PostgreSQL
Tech stack: Python, Flask, Stripe
```

---

## Example 359

**Intent:**
AI meeting notes for zoom, auto join and summarise

**Spec:**
```
Type:       Web application (AI meeting assistant)
Auth:       Google sign-in with calendar access
Data model: User(id, email, google_token)
            Meeting(id, user_id -> User, title, zoom_url, starts_at, transcript, summary)
            ActionItem(id, meeting_id -> Meeting, text, owner)
Features:   - Read upcoming Zoom meetings from the user's calendar
            - Send a recording bot to join the meeting
            - Transcribe and summarise the meeting
            - Extract action items and owners
            - Email the summary to attendees
API:        REST
            GET  /meetings
            GET  /meetings/{id}
            POST /webhooks/recall
            POST /meetings/{id}/share
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Recall.ai API, Google Calendar API, OpenAI API
```

---

## Example 360

**Intent:**
website for collecting stories from older people in our town, audio interviews archive

**Spec:**
```
Type:       Web application (oral history archive)
Auth:       Volunteer login for interviewers and editors
Data model: Narrator(id, name, born_year, consent_signed)
            Interview(id, narrator_id -> Narrator, interviewer, recorded_on, audio_url, transcript, summary)
            Tag(id, name)
            InterviewTag(interview_id -> Interview, tag_id -> Tag)
Features:   - Upload audio interviews with consent records
            - Transcribe audio automatically and let volunteers correct it
            - Tag interviews by place, decade and theme
            - Let the public listen and search transcripts
            - Hide interviews without signed consent
API:        REST
            GET  /interviews?tag=&q=
            POST /interviews
            PUT  /interviews/{id}/transcript
            GET  /tags
Storage:    PostgreSQL, S3 (audio)
Tech stack: Python, Django, OpenAI Whisper
```

---

## Example 361

**Intent:**
help me design reddit-like site for sharing deals and coupons

**Spec:**
```
Type:       Web application (deal sharing community)
Auth:       Email + password
Data model: User(id, username, email, password_hash)
            Deal(id, user_id -> User, title, url, store, price, original_price, coupon_code, expires_at, temperature)
            Vote(user_id -> User, deal_id -> Deal, value)
            Comment(id, deal_id -> Deal, user_id -> User, body)
Features:   - Post deals with price, store and coupon code
            - Vote deals hot or cold
            - Mark expired deals automatically
            - Get alerts for keywords
            - Sort by hottest and newest
API:        REST
            GET  /deals?sort=
            POST /deals
            POST /deals/{id}/vote
            POST /deals/{id}/comments
            POST /alerts
Storage:    PostgreSQL
Tech stack: PHP, Symfony, Vue.js
```

---

## Example 362

**Intent:**
knowledge sharing site for farmers in africa, works on slow internet, sms too

**Spec:**
```
Type:       Web application (low-bandwidth knowledge platform)
Auth:       Phone number login with SMS code
Data model: Farmer(id, phone, name, region, crops, language)
            Article(id, title, crop, language, body, audio_url)
            Question(id, farmer_id -> Farmer, crop, body, via, created_at)
            Answer(id, question_id -> Question, expert_name, body)
Features:   - Serve light pages under 100 KB
            - Ask questions by SMS or on the web
            - Let agronomists answer questions
            - Send answers back by SMS
            - Offer articles in local languages with audio
API:        REST
            POST /auth/otp
            GET  /articles?crop=&lang=
            POST /questions
            POST /sms/inbound
            POST /questions/{id}/answers
Storage:    PostgreSQL
Tech stack: Python, Django, Africa's Talking SMS API
```

---

## Example 363

**Intent:**
whats needed for a saas where gyms sell online workouts to members, per gym branding

**Spec:**
```
Type:       Web application (white-label fitness SaaS)
Auth:       Email + password per gym tenant, Stripe subscriptions for members
Data model: Gym(id, name, subdomain, logo_url, brand_color, stripe_account_id)
            Member(id, gym_id -> Gym, email, password_hash, subscription_status)
            Workout(id, gym_id -> Gym, title, video_url, duration_minutes, level)
            Program(id, gym_id -> Gym, title, weeks)
Features:   - Give each gym a branded site on its own subdomain
            - Upload workout videos and group them into programs
            - Sell memberships with payments going to the gym
            - Track which workouts members completed
            - Charge gyms a platform fee
API:        REST
            GET  /workouts
            POST /workouts
            POST /programs
            POST /checkout
            POST /workouts/{id}/complete
Storage:    PostgreSQL, Mux (video)
Tech stack: Ruby on Rails, Stripe Connect, Mux
```

---

## Example 364

**Intent:**
q&a for my product's users

**Spec:**
```
Type:       Web application (community Q&A)
Auth:       Single sign-on from the product via OAuth
Data model: User(id, external_id, name, is_staff)
            Question(id, user_id -> User, title, body, solved)
            Answer(id, question_id -> Question, user_id -> User, body, accepted)
Features:   - Ask and answer questions about the product
            - Mark answers from staff
            - Accept a solution
            - Search before asking
API:        REST
            GET  /questions?q=
            POST /questions
            POST /questions/{id}/answers
            POST /answers/{id}/accept
Storage:    PostgreSQL
Tech stack: Node.js, Fastify, React
```

---

## Example 365

**Intent:**
An online writing course where students submit assignments, the AI gives first feedback, and then I review it before sending.

**Spec:**
```
Type:       Web application (AI-assisted course feedback)
Auth:       Email + password, roles: instructor and student
Data model: Student(id, name, email, password_hash)
            Assignment(id, title, prompt, rubric)
            Submission(id, assignment_id -> Assignment, student_id -> Student, text, ai_draft_feedback, final_feedback, status)
Features:   - Submit written assignments
            - Draft feedback against the rubric with an LLM
            - Let the instructor edit and approve the feedback
            - Send approved feedback to the student
            - Show the instructor a queue of pending reviews
API:        REST
            GET  /assignments
            POST /assignments/{id}/submissions
            GET  /instructor/queue
            PUT  /submissions/{id}/feedback
            POST /submissions/{id}/release
Storage:    PostgreSQL
Tech stack: Python, Django, Anthropic Claude API
```

---

## Example 366

**Intent:**
hiking club website with trip reports and gear swap

**Spec:**
```
Type:       Web application (outdoor club site)
Auth:       Email + password for members
Data model: Member(id, name, email, password_hash)
            TripReport(id, member_id -> Member, title, route, date, body, photos, gpx_url)
            GearItem(id, member_id -> Member, name, condition, price, status)
Features:   - Post trip reports with photos and GPX tracks
            - Show routes on a map
            - List gear for sale or swap
            - Message members about gear
            - Filter reports by region and season
API:        REST
            GET  /reports?region=
            POST /reports
            GET  /gear
            POST /gear
            POST /gear/{id}/messages
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Flask, Leaflet
```

---

## Example 367

**Intent:**
news aggregator for my niche (ev cars), users submit links and vote

**Spec:**
```
Type:       Web application (news aggregator)
Auth:       Email + password
Data model: User(id, username, email, password_hash)
            Link(id, user_id -> User, url, title, domain, score, created_at)
            Vote(user_id -> User, link_id -> Link)
            Comment(id, link_id -> Link, user_id -> User, parent_id -> Comment, body)
Features:   - Submit EV news links
            - Upvote links
            - Rank the front page by votes and age
            - Detect duplicate URLs
            - Discuss links in threaded comments
API:        REST
            GET  /
            POST /links
            POST /links/{id}/vote
            GET  /links/{id}
            POST /links/{id}/comments
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Turbo
```

---

## Example 368

**Intent:**
tool for nonprofits to collect and showcase impact stories from beneficiaries

**Spec:**
```
Type:       Web application (impact story collection)
Auth:       Staff login with email + password
Data model: Organisation(id, name)
            Story(id, organisation_id -> Organisation, title, body, photo_url, program, consent_given, published)
            Metric(id, organisation_id -> Organisation, name, value, period)
Features:   - Collect stories with a simple form and consent checkbox
            - Approve stories before publishing
            - Tag stories by program
            - Show an embeddable impact wall on the nonprofit's website
            - Show key metrics next to stories
API:        REST
            POST /stories
            PATCH /stories/{id}
            GET  /orgs/{id}/wall
            POST /metrics
Storage:    PostgreSQL, S3 (photos)
Tech stack: Node.js, Express, Preact embed
```

---

## Example 369

**Intent:**
Design a site where cosplayers commission props from prop makers, with progress updates

**Spec:**
```
Type:       Web application (commission marketplace)
Auth:       Email + password, roles: maker and client
Data model: Maker(id, name, email, password_hash, specialties, gallery)
            Commission(id, maker_id -> Maker, client_id -> Client, description, price, deadline, status)
            Milestone(id, commission_id -> Commission, title, amount, paid)
            ProgressUpdate(id, commission_id -> Commission, photo_url, note, created_at)
            Client(id, name, email, password_hash)
Features:   - Request a commission with references and deadline
            - Split payment into milestones
            - Post progress photos
            - Release milestone payments when approved
            - Review makers when done
API:        REST
            GET  /makers
            POST /commissions
            POST /commissions/{id}/milestones
            POST /commissions/{id}/updates
            POST /milestones/{id}/release
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, Stripe Connect
```

---

## Example 370

**Intent:**
comunity site 4 skaters w/ spots map

**Spec:**
```
Type:       Web application (skate spot community)
Auth:       Email + password or Instagram sign-in
Data model: Skater(id, username, email)
            Spot(id, name, type, lat, lng, bust_level, added_by -> Skater)
            SpotPhoto(id, spot_id -> Spot, url, skater_id -> Skater)
            Clip(id, spot_id -> Spot, video_url, skater_id -> Skater)
Features:   - Add skate spots to a map with type like ledge or bowl
            - Rate how likely security is to kick you out
            - Upload photos and clips at a spot
            - Find spots near you
            - Comment on spots
API:        REST
            GET  /spots?near=
            POST /spots
            POST /spots/{id}/photos
            POST /spots/{id}/clips
Storage:    PostgreSQL with PostGIS, S3 (media)
Tech stack: Node.js, Express, React, Mapbox
```

---

## Example 371

**Intent:**
platform for local makers markets, vendors apply for stalls and organisers approve

**Spec:**
```
Type:       Web application (market stall applications)
Auth:       Email + password, roles: vendor and organiser
Data model: Vendor(id, business_name, email, password_hash, category, photos)
            Market(id, name, date, location, stall_count, fee)
            StallApplication(id, market_id -> Market, vendor_id -> Vendor, status, paid)
            StallAssignment(application_id -> StallApplication, stall_number)
Features:   - Publish upcoming markets with stall fees
            - Let vendors apply with photos of their products
            - Approve vendors while balancing categories
            - Collect stall fees after approval
            - Assign stall numbers on a layout
API:        REST
            GET  /markets
            POST /markets/{id}/applications
            PATCH /applications/{id}
            POST /applications/{id}/pay
            PUT  /applications/{id}/stall
Storage:    PostgreSQL
Tech stack: Laravel, Inertia.js, React, Stripe
```

---

## Example 372

**Intent:**
discourse alternative written in python

**Spec:**
```
Type:       Web application (forum)
Auth:       Email + password, OAuth with Google and GitHub
Data model: User(id, username, email, trust_level)
            Category(id, name, color)
            Topic(id, category_id -> Category, user_id -> User, title, views, pinned)
            Post(id, topic_id -> Topic, user_id -> User, raw, cooked_html, reply_to_id -> Post)
            Notification(id, user_id -> User, type, data_json, read)
Features:   - Post topics and replies with Markdown
            - Raise trust levels automatically based on activity
            - Notify users about replies and mentions
            - Load more posts as the user scrolls
            - Send email digests of popular topics
API:        REST
            GET  /latest
            GET  /c/{id}
            POST /topics
            GET  /t/{id}
            POST /t/{id}/posts
            GET  /notifications
Storage:    PostgreSQL, Redis
Tech stack: Python, FastAPI, Celery, React
```

---

## Example 373

**Intent:**
language exchange events site for cafes

**Spec:**
```
Type:       Web application (event listings)
Auth:       Organiser email + password, attendees RSVP with email
Data model: Organiser(id, name, email, password_hash)
            Event(id, organiser_id -> Organiser, cafe_name, address, starts_at, languages, capacity)
            Rsvp(event_id -> Event, name, email, languages_spoken)
Features:   - List language exchange evenings by city
            - RSVP with the languages you speak
            - Show the language balance of attendees
            - Remind attendees the day before
API:        REST
            GET  /events?city=
            POST /events
            POST /events/{id}/rsvp
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 374

**Intent:**
give me a web app where photographers upload client galleries and clients pick favourites

**Spec:**
```
Type:       Web application (client photo proofing)
Auth:       Photographer email + password, clients open galleries with a password
Data model: Photographer(id, name, email, password_hash)
            Gallery(id, photographer_id -> Photographer, client_name, password_hash, expires_on)
            Photo(id, gallery_id -> Gallery, url, filename)
            Favourite(gallery_id -> Gallery, photo_id -> Photo)
Features:   - Upload a gallery of photos for a client
            - Protect galleries with a password and expiry date
            - Let clients mark favourites for editing
            - Export favourite filenames for Lightroom
            - Allow clients to download approved photos
API:        REST
            POST /galleries
            POST /galleries/{id}/photos
            GET  /g/{id}
            POST /g/{id}/favourites
            GET  /galleries/{id}/favourites.txt
Storage:    PostgreSQL, Backblaze B2 (photos)
Tech stack: Node.js, Fastify, Svelte
```

---

## Example 375

**Intent:**
crowdfunding for community solar panels, neighbours invest small amounts

**Spec:**
```
Type:       Web application (community energy investment)
Auth:       Email + password with identity verification
Data model: Investor(id, name, email, password_hash, address, kyc_status)
            SolarProject(id, site_name, capacity_kw, target_amount, share_price, expected_return_percent, status)
            Holding(id, project_id -> SolarProject, investor_id -> Investor, shares)
            Dividend(id, project_id -> SolarProject, year, amount_per_share)
Features:   - Show solar projects with capacity and expected return
            - Buy shares from a minimum amount
            - Show energy generated each month
            - Pay yearly dividends to investors
            - Give priority to investors living nearby
API:        REST
            GET  /projects
            POST /projects/{id}/holdings
            GET  /me/holdings
            GET  /projects/{id}/generation
Storage:    PostgreSQL
Tech stack: Python, Django, GoCardless
```

---

## Example 376

**Intent:**
for my company i want ai assistant website that answers HR questions from our handbook

**Spec:**
```
Type:       Web application (AI HR assistant)
Auth:       Okta single sign-on
Data model: HandbookSection(id, title, text, embedding, updated_at)
            Conversation(id, employee_email, created_at)
            Turn(id, conversation_id -> Conversation, question, answer, sources)
Features:   - Import the employee handbook and split it into sections
            - Answer questions with links to the relevant section
            - Say "ask HR" when the handbook has no answer
            - Show HR the most common questions
            - Never store answers about specific employees
API:        REST
            POST /ask
            GET  /conversations/{id}
            POST /admin/handbook
            GET  /admin/top-questions
Storage:    PostgreSQL with pgvector
Tech stack: TypeScript, Next.js, OpenAI API, LangChain.js
```

---

## Example 377

**Intent:**
create site where teenagers can find summer jobs near them safely

**Spec:**
```
Type:       Web application (youth job board)
Auth:       Email + password, parental consent for under-16s, employers verified
Data model: Teen(id, name, email, birth_year, parent_email, consent_given)
            Employer(id, name, address, verified)
            Job(id, employer_id -> Employer, title, min_age, hours_per_week, pay, location)
            Application(job_id -> Job, teen_id -> Teen, status)
Features:   - Show only jobs suitable for the teen's age
            - Verify employers before they can post
            - Require parental consent before applying
            - Hide the teen's contact details until they accept an interview
            - Explain legal working hours for minors
API:        REST
            GET  /jobs?near=
            POST /jobs
            POST /jobs/{id}/apply
            POST /consent/{token}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire
```

---

## Example 378

**Intent:**
a site for comparing courses from different universities online

**Spec:**
```
Type:       Web application (course comparison)
Data model: University(id, name, country, ranking)
            Program(id, university_id -> University, title, level, duration_months, tuition, language, online)
            Comparison(id, program_ids, share_code)
Features:   - Search programs by subject, level and country
            - Compare up to 4 programs side by side
            - Filter by tuition and language
            - Share a comparison with a link
API:        REST
            GET  /programs?subject=&level=
            GET  /programs/{id}
            POST /comparisons
            GET  /comparisons/{code}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js
```

---

## Example 379

**Intent:**
im building a community for indie hackers to share revenue numbers publicly

**Spec:**
```
Type:       Web application (open revenue community)
Auth:       Email + password or Twitter/X sign-in
Data model: Maker(id, name, handle)
            Product(id, maker_id -> Maker, name, url, stripe_verified)
            RevenueReport(id, product_id -> Product, month, mrr, source)
            Comment(id, product_id -> Product, maker_id -> Maker, body)
Features:   - Connect Stripe with a read-only key to verify revenue
            - Post monthly MRR updates
            - Show a leaderboard of verified products
            - Chart each product's revenue over time
            - Comment on products
API:        REST
            GET  /products?sort=mrr
            POST /products
            POST /products/{id}/stripe
            GET  /products/{id}/revenue
            POST /products/{id}/comments
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, Stripe API, Chart.js
```

---

## Example 380

**Intent:**
Can you make me site where I post homework help videos for maths, organised by grade and topic

**Spec:**
```
Type:       Web application (video library)
Auth:       Admin login for the teacher
Data model: Grade(id, number)
            Topic(id, grade_id -> Grade, name)
            Video(id, topic_id -> Topic, title, youtube_id, worksheet_url, views)
Features:   - Organise videos by grade and topic
            - Embed YouTube videos with a worksheet download
            - Search videos by keyword
            - Show most watched videos
API:        REST
            GET  /grades/{n}/topics
            GET  /topics/{id}/videos
            GET  /search?q=
            POST /admin/videos
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 381

**Intent:**
I want something like Upwork but just for accountants and bookkeepers, small businesses post monthly bookkeeping jobs

**Spec:**
```
Type:       Web application (accounting services marketplace)
Auth:       Email + password, accountants submit qualifications for verification
Data model: Business(id, name, email, password_hash, industry)
            Accountant(id, name, email, password_hash, qualifications, software_skills, verified)
            Job(id, business_id -> Business, scope, software, monthly_budget, status)
            Proposal(id, job_id -> Job, accountant_id -> Accountant, monthly_fee, message, status)
            Contract(id, job_id -> Job, accountant_id -> Accountant, monthly_fee, started_on)
Features:   - Post monthly bookkeeping jobs with the accounting software used
            - Let verified accountants send proposals
            - Start a recurring contract with monthly billing
            - Share documents securely
            - Review accountants after 3 months
API:        REST
            GET  /jobs
            POST /jobs
            POST /jobs/{id}/proposals
            POST /proposals/{id}/accept
            POST /contracts/{id}/documents
Storage:    PostgreSQL, S3 (encrypted documents)
Tech stack: Python, Django, Stripe Billing
```

---

## Example 382

**Intent:**
mini wiki for a video game guild with build guides

**Spec:**
```
Type:       Web application (guild wiki)
Auth:       Discord sign-in
Data model: Member(id, discord_id, name, guild_role)
            Guide(id, author_id -> Member, title, class_name, content, patch_version, votes)
            GuideVote(guide_id -> Guide, member_id -> Member)
Features:   - Write build guides per class
            - Tag guides with the patch version
            - Mark guides outdated after a new patch
            - Vote on guides
            - Restrict editing to guild officers
API:        REST
            GET  /guides?class=
            POST /guides
            PUT  /guides/{id}
            POST /guides/{id}/vote
Storage:    SQLite
Tech stack: Node.js, Express, Vue.js
```

---

## Example 383

**Intent:**
marketplace where people sell homemade dog treats

**Spec:**
```
Type:       Web application (marketplace)
Auth:       Email + password, sellers must upload a food hygiene certificate
Data model: Seller(id, shop_name, email, password_hash, certificate_url, approved)
            Treat(id, seller_id -> Seller, name, ingredients, allergens, price, stock)
            Order(id, buyer_email, seller_id -> Seller, total, status, shipping_address)
Features:   - Approve sellers after checking their hygiene certificate
            - List treats with ingredients and allergens
            - Filter treats by allergen
            - Pay by card and split payment to sellers
            - Notify sellers of new orders
API:        REST
            GET  /treats?exclude_allergen=
            POST /treats
            POST /orders
            PATCH /admin/sellers/{id}
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Stripe Connect, React
```

---

## Example 384

**Intent:**
my uni society needs website: events, membership payment, committee blog

**Spec:**
```
Type:       Web application (student society site)
Auth:       University SSO for students, committee admin role
Data model: Student(id, uni_id, name, email)
            Membership(id, student_id -> Student, year, paid)
            Event(id, title, starts_at, location, members_only, capacity)
            Ticket(event_id -> Event, student_id -> Student)
            BlogPost(id, author_id -> Student, title, body, published_at)
Features:   - Pay yearly membership online
            - Book tickets for events, some members only
            - Write committee blog posts
            - Check tickets at the door with a list
            - Email members about new events
API:        REST
            POST /membership/checkout
            GET  /events
            POST /events/{id}/tickets
            GET  /blog
            POST /blog
Storage:    PostgreSQL
Tech stack: Python, Django, Stripe
```

---

## Example 385

**Intent:**
collaborative trip planner where friends add places and vote

**Spec:**
```
Type:       Web application (group trip planner)
Auth:       Email + password or Google sign-in, invite by link
Data model: Trip(id, name, destination, start_date, end_date, invite_code)
            Traveller(id, trip_id -> Trip, user_id, name)
            Place(id, trip_id -> Trip, name, lat, lng, added_by -> Traveller, day)
            PlaceVote(place_id -> Place, traveller_id -> Traveller, value)
Features:   - Add places to a shared trip map
            - Vote on which places to visit
            - Drag places into a day-by-day itinerary
            - Sync changes live for everyone
            - Export the itinerary to Google Maps
API:        REST and WebSocket
            POST /trips
            POST /trips/{code}/join
            POST /trips/{id}/places
            POST /places/{id}/vote
            WS   /trips/{id}
Storage:    PostgreSQL
Tech stack: TypeScript, React, Google Maps JavaScript API, Node.js, Socket.IO
```

---

## Example 386

**Intent:**
blog about personal finance with calculators embedded

**Spec:**
```
Type:       Web application (blog with calculators)
Auth:       Admin login
Data model: Post(id, title, slug, body_mdx, published_at, category)
            Calculator(id, name, type, config_json)
Features:   - Publish articles in MDX
            - Embed interactive calculators like compound interest and loan payoff
            - Show charts that update as numbers change
            - Collect newsletter emails
API:        REST
            GET  /posts
            GET  /posts/{slug}
            POST /api/subscribe
Storage:    MDX files in the repo, ConvertKit (subscribers)
Tech stack: Next.js, MDX, Recharts, ConvertKit API
```

---

## Example 387

**Intent:**
platform where small orgs post board seats and people volunteer to join nonprofit boards

**Spec:**
```
Type:       Web application (board volunteer matching)
Auth:       Email + password, roles: organisation and candidate
Data model: Organisation(id, name, cause, email, password_hash)
            BoardSeat(id, organisation_id -> Organisation, role, skills_needed, time_commitment, status)
            Candidate(id, name, email, password_hash, skills, causes, linkedin_url)
            Expression(seat_id -> BoardSeat, candidate_id -> Candidate, message, status)
Features:   - Post board roles with skills needed
            - Let candidates express interest
            - Suggest candidates whose skills match
            - Track candidates through intro, meeting and appointed
            - Offer short training resources for new trustees
API:        REST
            GET  /seats?cause=&skill=
            POST /seats
            POST /seats/{id}/interest
            PATCH /interest/{id}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stimulus
```

---

## Example 388

**Intent:**
website where pple post photos of street art and map them

**Spec:**
```
Type:       Web application (street art map)
Auth:       Email + password
Data model: User(id, username, email, password_hash)
            Artwork(id, user_id -> User, artist_name, photo_url, lat, lng, still_there, spotted_on)
            Confirmation(artwork_id -> Artwork, user_id -> User, still_there, created_at)
Features:   - Upload photos of street art with location from EXIF
            - Show all pieces on a map
            - Confirm if a piece is still there
            - Search by artist
            - Make walking tours of nearby pieces
API:        REST
            GET  /artworks?bbox=
            POST /artworks
            POST /artworks/{id}/confirm
            GET  /tours?near=
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: Python, Django, Leaflet, Pillow
```

---

## Example 389

**Intent:**
sell and schedule tutoring for music theory online, all in laravel

**Spec:**
```
Type:       Web application (online tutoring)
Auth:       Email + password, Laravel Breeze
Data model: Student(id, name, email, password_hash, level)
            Package(id, name, lessons, price)
            Purchase(id, student_id -> Student, package_id -> Package, lessons_left)
            Lesson(id, student_id -> Student, starts_at, meeting_link, notes)
Features:   - Sell lesson packages
            - Book lessons from available times
            - Deduct a lesson from the package on booking
            - Add lesson notes and exercises
            - Send email reminders
API:        REST
            GET  /packages
            POST /packages/{id}/purchase
            GET  /availability
            POST /lessons
            PATCH /lessons/{id}
Storage:    MySQL
Tech stack: PHP, Laravel, Laravel Breeze, Laravel Cashier
```

---

## Example 390

**Intent:**
dashboard for my online community: who is active, new members, top posters

**Spec:**
```
Type:       Data dashboard (community analytics)
Auth:       Admin login
Data model: Member(id, joined_at, last_active_at)
            ActivityEvent(id, member_id -> Member, type, created_at)
            DailyStat(date, active_members, new_members, posts)
Features:   - Import activity events from the forum database nightly
            - Show daily and monthly active members
            - Show new member signups over time
            - List top posters this month
            - Flag members who stopped posting
API:        REST
            GET  /stats/daily
            GET  /stats/top-posters?month=
            GET  /stats/churn-risk
Storage:    PostgreSQL
Tech stack: Python, Streamlit, pandas, SQLAlchemy
```

---

## Example 391

**Intent:**
Can you plan a web app for my dog training school where owners watch training videos and upload their own clips for feedback?

**Spec:**
```
Type:       Web application (training feedback platform)
Auth:       Email + password
Data model: Owner(id, name, email, password_hash, dog_name)
            Lesson(id, title, video_url, level)
            Clip(id, owner_id -> Owner, lesson_id -> Lesson, video_url, uploaded_at)
            TrainerFeedback(id, clip_id -> Clip, body, created_at)
Features:   - Watch training lessons by level
            - Upload a clip of practising a lesson
            - Get written feedback from a trainer
            - Track which lessons the dog has mastered
            - Notify owners when feedback arrives
API:        REST
            GET  /lessons
            POST /lessons/{id}/clips
            GET  /trainer/queue
            POST /clips/{id}/feedback
Storage:    PostgreSQL, S3 (video)
Tech stack: Node.js, Express, React, Mux
```

---

## Example 392

**Intent:**
forum 4 truck drivers

**Spec:**
```
Type:       Web application (forum)
Auth:       Email + password
Data model: Driver(id, username, email, password_hash, region)
            Board(id, name)
            Thread(id, board_id -> Board, driver_id -> Driver, title)
            Post(id, thread_id -> Thread, driver_id -> Driver, body)
            Stop(id, name, lat, lng, rating)
Features:   - Discuss in boards like Routes, Pay and Equipment
            - Rate truck stops and parking spots
            - Post road condition updates
            - Use a simple layout that works on phones in the cab
API:        REST
            GET  /boards/{id}/threads
            POST /threads
            POST /threads/{id}/posts
            GET  /stops?near=
            POST /stops/{id}/ratings
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Leaflet
```

---

## Example 393

**Intent:**
i want an ai that helps me write grant applications for my charity on a website

**Spec:**
```
Type:       Web application (AI grant writing assistant)
Auth:       Email + password
Data model: Charity(id, name, mission, programs_json)
            User(id, charity_id -> Charity, email, password_hash)
            Grant(id, charity_id -> Charity, funder, deadline, questions_json)
            Draft(id, grant_id -> Grant, question_index, text, updated_at)
Features:   - Save the charity's mission and programs once
            - Paste a funder's application questions
            - Draft answers with an LLM using the charity profile
            - Respect word limits for each answer
            - Track deadlines for grants in progress
API:        REST
            PUT  /charity
            POST /grants
            POST /grants/{id}/drafts/generate
            PUT  /drafts/{id}
            GET  /grants?due_before=
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Anthropic Claude API, React
```

---

## Example 394

**Intent:**
review site for camping spots

**Spec:**
```
Type:       Web application (review site)
Auth:       Email + password
Data model: User(id, username, email, password_hash)
            Campsite(id, name, lat, lng, type, amenities, price)
            Review(id, campsite_id -> Campsite, user_id -> User, rating, visited_on, body, photos)
Features:   - Find campsites on a map
            - Filter by amenities like water, toilets and fires allowed
            - Review with photos and visit date
            - Show recent reviews first
API:        REST
            GET  /campsites?bbox=&amenities=
            GET  /campsites/{id}
            POST /campsites/{id}/reviews
Storage:    PostgreSQL with PostGIS
Tech stack: Node.js, Express, Vue.js, Leaflet
```

---

## Example 395

**Intent:**
substack style but for audio, people subscribe to creators podcasts with private rss

**Spec:**
```
Type:       Web application (paid podcast platform)
Auth:       Email + password, Stripe subscriptions
Data model: Creator(id, name, email, password_hash, stripe_account_id)
            Show(id, creator_id -> Creator, title, price_monthly)
            Episode(id, show_id -> Show, title, audio_url, published_at)
            Subscriber(id, email, show_id -> Show, feed_token, status)
Features:   - Upload episodes and publish them
            - Sell monthly subscriptions to a show
            - Give each subscriber a private RSS feed URL
            - Revoke the feed when a subscription ends
            - Show creators subscriber counts and revenue
API:        REST
            POST /shows/{id}/episodes
            POST /shows/{id}/subscribe
            GET  /feeds/{token}.xml
            POST /webhooks/stripe
Storage:    PostgreSQL, S3 (audio)
Tech stack: Python, Django, Stripe Connect
```

---

## Example 396

**Intent:**
Wiki that auto generates docs from our codebase and lets devs add notes

**Spec:**
```
Type:       Web application (code documentation wiki)
Auth:       GitHub OAuth, restricted to organisation members
Data model: Repository(id, name, default_branch, last_synced_sha)
            Module(id, repository_id -> Repository, path, generated_doc, updated_at)
            Note(id, module_id -> Module, author, body, created_at)
Features:   - Sync repositories on every push
            - Generate module docs from docstrings and code with an LLM
            - Let developers add notes to any module
            - Show which docs are stale since the last change
            - Search modules and notes
API:        REST
            POST /webhooks/github
            GET  /repos/{id}/modules
            GET  /modules/{id}
            POST /modules/{id}/notes
            GET  /search?q=
Storage:    PostgreSQL
Tech stack: Python, FastAPI, tree-sitter, OpenAI API, React
```

---

## Example 397

**Intent:**
project tracker for a renovation, rooms, tasks, budget, contractors

**Spec:**
```
Type:       Web application (renovation project tracker)
Auth:       Email + password, share with partner
Data model: Project(id, name, budget)
            Room(id, project_id -> Project, name)
            Task(id, room_id -> Room, title, status, contractor_id -> Contractor, due_date)
            Contractor(id, name, trade, phone)
            Expense(id, room_id -> Room, description, amount, receipt_url)
Features:   - Track tasks per room
            - Log expenses with receipts
            - Compare spending with the budget per room
            - Keep contractor contacts
            - Share the project with a partner
API:        REST
            GET  /projects/{id}
            POST /rooms/{id}/tasks
            POST /rooms/{id}/expenses
            GET  /projects/{id}/budget
Storage:    SQLite
Tech stack: Python, Flask, Chart.js
```

---

## Example 398

**Intent:**
course platform with live coding exercises for javascript

**Spec:**
```
Type:       Web application (interactive coding course)
Auth:       Email + password or GitHub sign-in
Data model: Learner(id, email, name)
            Chapter(id, title, position)
            Exercise(id, chapter_id -> Chapter, prompt, starter_code, tests)
            Attempt(id, exercise_id -> Exercise, learner_id -> Learner, code, passed, created_at)
Features:   - Edit code in the browser with instant preview
            - Run tests in a sandboxed iframe
            - Show hints after failed attempts
            - Track completion per chapter
            - Award a certificate at the end
API:        REST
            GET  /chapters
            GET  /exercises/{id}
            POST /exercises/{id}/attempts
            GET  /me/certificate
Storage:    PostgreSQL
Tech stack: TypeScript, React, CodeMirror, Node.js
```

---

## Example 399

**Intent:**
Wanna make social site for vintage clothes lovers, post outfits and tag where you bought them

**Spec:**
```
Type:       Web application (fashion social network)
Auth:       Email + password or Instagram sign-in
Data model: User(id, username, email)
            Outfit(id, user_id -> User, photo_url, caption, era, created_at)
            ItemTag(id, outfit_id -> Outfit, x, y, item_name, shop_name, shop_url)
            Like(user_id -> User, outfit_id -> Outfit)
Features:   - Post outfit photos
            - Tag items in the photo with where they were bought
            - Browse by decade like 70s or 90s
            - Like and save outfits
            - Show a list of the most tagged vintage shops
API:        REST
            GET  /outfits?era=
            POST /outfits
            POST /outfits/{id}/tags
            POST /outfits/{id}/like
            GET  /shops/top
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, React
```

---

## Example 400

**Intent:**
rotation schedule website for my volunteer fire department

**Spec:**
```
Type:       Web application (duty roster)
Auth:       Email + password, roles: firefighter and officer
Data model: Firefighter(id, name, email, phone, qualifications)
            DutyShift(id, starts_at, ends_at, required_qualifications)
            Assignment(shift_id -> DutyShift, firefighter_id -> Firefighter)
            Unavailability(id, firefighter_id -> Firefighter, from_date, to_date)
Features:   - Generate a fair duty rotation for the month
            - Respect unavailability and required qualifications per shift
            - Let firefighters swap shifts with officer approval
            - Send SMS reminders before duty
            - Show hours served per person
API:        REST
            POST /rosters/generate
            GET  /rosters?month=
            POST /unavailability
            POST /swaps
            GET  /reports/hours
Storage:    PostgreSQL
Tech stack: Python, Django, OR-Tools, Twilio
```

---

## Example 401

**Intent:**
Open-source alternative to Linktree for musicians that also shows tour dates

**Spec:**
```
Type:       Web application (musician landing page)
Auth:       Email + password
Data model: Artist(id, slug, name, bio, photo_url)
            Link(id, artist_id -> Artist, label, url, position)
            TourDate(id, artist_id -> Artist, date, city, venue, ticket_url)
Features:   - Build a page at /artist-slug with streaming and social links
            - Show upcoming tour dates with ticket links
            - Import tour dates from Bandsintown
            - Count link clicks
            - Self-host with one Docker image
API:        REST
            GET  /{slug}
            POST /api/links
            POST /api/tour-dates
            POST /api/import/bandsintown
Storage:    SQLite
Tech stack: Go, templ, Bandsintown API, Docker
```

---

## Example 402

**Intent:**
mentoring platform for first generation college students

**Spec:**
```
Type:       Web application (student mentoring)
Auth:       University SSO for students, email + password for alumni mentors
Data model: Student(id, name, email, major, year, needs)
            Mentor(id, name, email, password_hash, major, industry, capacity)
            Match(id, student_id -> Student, mentor_id -> Mentor, status, started_on)
            CheckIn(id, match_id -> Match, date, topics, notes)
Features:   - Match students with alumni from the same major
            - Schedule monthly check-ins
            - Share resources on financial aid and internships
            - Let staff see which matches are inactive
            - Collect end-of-year feedback
API:        REST
            GET  /mentors?major=
            POST /matches
            POST /matches/{id}/check-ins
            GET  /admin/inactive-matches
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 403

**Intent:**
a site where people can swap houses for holidays

**Spec:**
```
Type:       Web application (home exchange)
Auth:       Email + password with ID verification
Data model: Member(id, name, email, password_hash, verified)
            Home(id, member_id -> Member, city, country, bedrooms, description, photos)
            Availability(id, home_id -> Home, from_date, to_date)
            SwapRequest(id, from_home_id -> Home, to_home_id -> Home, dates, status)
            Review(id, swap_id -> SwapRequest, rating, body)
Features:   - List your home with photos and available dates
            - Search homes by destination and dates
            - Request a reciprocal swap
            - Confirm swaps and exchange contact details
            - Review each other after the stay
API:        REST
            GET  /homes?city=&from=&to=
            POST /homes
            POST /swaps
            PATCH /swaps/{id}
            POST /swaps/{id}/review
Storage:    PostgreSQL, S3 (photos)
Tech stack: Node.js, NestJS, Next.js
```

---

## Example 404

**Intent:**
newsletter platform for schools to send weekly updates to parents in multiple languages

**Spec:**
```
Type:       Web application (school newsletter)
Auth:       Staff login with email + password, parents subscribe with email and language
Data model: School(id, name)
            Parent(id, school_id -> School, email, language)
            Newsletter(id, school_id -> School, title, body_html, sent_at)
            Translation(id, newsletter_id -> Newsletter, language, body_html)
Features:   - Write the weekly newsletter once
            - Translate it automatically into each parent's language
            - Let staff check translations before sending
            - Send each parent the version in their language
            - Archive past newsletters
API:        REST
            POST /newsletters
            POST /newsletters/{id}/translate
            PUT  /translations/{id}
            POST /newsletters/{id}/send
            POST /subscribe
Storage:    PostgreSQL
Tech stack: Python, Django, DeepL API, Amazon SES
```

---

## Example 405

**Intent:**
pls i want website like olx for my town in kenya, pay with mpesa

**Spec:**
```
Type:       Web application (classifieds marketplace)
Auth:       Phone number login with SMS one-time code
Data model: User(id, phone, name, town)
            Ad(id, user_id -> User, category, title, price_kes, photos, status, featured_until)
            Payment(id, ad_id -> Ad, mpesa_receipt, amount_kes, paid_at)
Features:   - Post ads with photos and price in KES
            - Search ads by category and town
            - Call or WhatsApp the seller from the ad
            - Pay with M-Pesa to feature an ad
            - Remove sold ads
API:        REST
            POST /auth/otp
            GET  /ads?category=&town=
            POST /ads
            POST /ads/{id}/feature
            POST /mpesa/callback
Storage:    PostgreSQL, S3 (photos)
Tech stack: Python, Django, Safaricom Daraja API
```

---

## Example 406

**Intent:**
blog with comments n likes, nothing fancy, vue

**Spec:**
```
Type:       Web application (blog)
Auth:       Email + password for commenters, admin role for the author
Data model: User(id, name, email, password_hash, is_admin)
            Post(id, title, slug, body, published_at)
            Comment(id, post_id -> Post, user_id -> User, body)
            Like(user_id -> User, post_id -> Post)
Features:   - Publish posts from an admin page
            - Comment on posts
            - Like posts
            - Show newest posts first
API:        REST
            GET  /posts
            GET  /posts/{slug}
            POST /posts/{id}/comments
            POST /posts/{id}/like
Storage:    SQLite
Tech stack: Vue.js, Node.js, Express
```

---

## Example 407

**Intent:**
Good day, I am pharmacist and I want make knowledge base website for pharmacy students where they study drugs and do quizzes, maybe teachers add content.

**Spec:**
```
Type:       Web application (pharmacy learning platform)
Auth:       Email + password, roles: student and teacher
Data model: User(id, name, email, password_hash, role)
            Drug(id, name, drug_class, mechanism, indications, side_effects, interactions)
            QuizQuestion(id, drug_id -> Drug, question, options, answer)
            QuizAttempt(id, user_id -> User, score, taken_at)
Features:   - Browse drug monographs by class
            - Let teachers add and edit drug pages
            - Generate quizzes from chosen drug classes
            - Track student quiz scores
            - Search drugs by name or indication
API:        REST
            GET  /drugs?class=
            POST /drugs
            PUT  /drugs/{id}
            POST /quizzes
            POST /quizzes/{id}/attempts
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Vue.js
```

---

## Example 408

**Intent:**
marketplace 4 used musical instruments

**Spec:**
```
Type:       Web application (marketplace)
Auth:       Email + password
Data model: User(id, name, email, password_hash, city)
            Instrument(id, seller_id -> User, type, brand, model, year, condition, price, photos, sound_clip_url, status)
            Offer(id, instrument_id -> Instrument, buyer_id -> User, amount, status)
Features:   - List instruments with photos and a sound clip
            - Filter by type, brand and city
            - Make offers
            - Offer local pickup or tracked shipping
            - Rate buyers and sellers
API:        REST
            GET  /instruments?type=&brand=
            POST /instruments
            POST /instruments/{id}/offers
            PATCH /offers/{id}
Storage:    PostgreSQL, S3 (media)
Tech stack: Ruby on Rails, Stripe
```

---

## Example 409

**Intent:**
i run a discord for designers and want a job board that posts new jobs into the discord too

**Spec:**
```
Type:       Web application (community job board)
Auth:       Discord sign-in for members, email + password for employers
Data model: Employer(id, company, email, password_hash)
            Job(id, employer_id -> Employer, title, type, location, salary, url, approved, posted_at)
            Member(id, discord_id, name)
Features:   - Let employers post design jobs for a fee
            - Approve jobs before they go live
            - Post approved jobs to a Discord channel
            - Let members save jobs
            - Filter by full-time, contract and remote
API:        REST
            GET  /jobs
            POST /jobs
            PATCH /admin/jobs/{id}
            POST /jobs/{id}/save
Storage:    PostgreSQL
Tech stack: Node.js, Express, discord.js, React, Stripe
```

---

## Example 410

**Intent:**
ai that summarises long email threads, web app connected to gmail

**Spec:**
```
Type:       Web application (AI email summariser)
Auth:       Google OAuth with Gmail read-only scope
Data model: User(id, email, google_refresh_token)
            ThreadSummary(id, user_id -> User, gmail_thread_id, subject, summary, decisions, open_questions, created_at)
Features:   - List long Gmail threads
            - Summarise a thread into the key points, decisions and open questions
            - Draft a reply based on the summary
            - Never store full email bodies
            - Refresh summaries when new messages arrive
API:        REST
            GET  /threads
            POST /threads/{id}/summary
            POST /threads/{id}/draft-reply
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Gmail API, Anthropic Claude API
```

---

## Example 411

**Intent:**
kickstarter style for community theatre productions

**Spec:**
```
Type:       Web application (crowdfunding)
Auth:       Email + password for theatre groups, backers check out as guests
Data model: Theatre(id, name, email, password_hash)
            Production(id, theatre_id -> Theatre, title, goal_cents, raised_cents, ends_at)
            Reward(id, production_id -> Production, title, price_cents, includes_ticket)
            Pledge(id, reward_id -> Reward, email, amount_cents, status)
Features:   - Launch a campaign for a new production
            - Offer rewards like tickets and a name in the programme
            - Charge pledges only if the goal is met
            - Send ticket codes to backers before opening night
            - Show a list of backers for the programme
API:        REST
            GET  /productions
            POST /productions
            POST /rewards/{id}/pledges
            GET  /productions/{id}/backers
Storage:    PostgreSQL
Tech stack: Python, Flask, Stripe
```

---

## Example 412

**Intent:**
an intranet wiki for a hospital ward, protocols and who's on call

**Spec:**
```
Type:       Web application (ward intranet)
Auth:       Hospital Active Directory login via LDAP
Data model: Protocol(id, title, category, body, review_due_on, approved_by)
            OnCall(id, date, role, staff_name, bleep)
            ProtocolAck(protocol_id -> Protocol, staff_id, acknowledged_at)
Features:   - Publish ward protocols with review dates
            - Require staff to acknowledge new protocols
            - Show today's on-call staff and bleep numbers
            - Flag protocols past their review date
            - Search protocols quickly
API:        REST
            GET  /protocols?q=
            POST /protocols
            POST /protocols/{id}/ack
            GET  /oncall/today
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, LDAP
```

---

## Example 413

**Intent:**
a site to share 3d printing models and print settings

**Spec:**
```
Type:       Web application (3D model sharing)
Auth:       Email + password
Data model: User(id, username, email, password_hash)
            Model(id, user_id -> User, title, stl_url, license, images)
            PrintProfile(id, model_id -> Model, user_id -> User, printer, material, layer_height, infill, photo_url)
            Like(user_id -> User, model_id -> Model)
Features:   - Upload STL files with images and a licence
            - Show a 3D preview in the browser
            - Share print settings that worked
            - Show photos of others' prints of the model
            - Like and remix models
API:        REST
            GET  /models?q=
            POST /models
            GET  /models/{id}
            POST /models/{id}/profiles
            POST /models/{id}/like
Storage:    PostgreSQL, S3 (STL files)
Tech stack: TypeScript, Next.js, three.js, Prisma
```

---

## Example 414

**Intent:**
create spec for a SaaS that hosts webinar for small business, register, attend, replay

**Spec:**
```
Type:       Web application (webinar SaaS)
Auth:       Email + password for hosts, attendees register with email
Data model: Host(id, name, email, password_hash, plan)
            Webinar(id, host_id -> Host, title, starts_at, replay_url)
            Registration(id, webinar_id -> Webinar, name, email, attended, join_token)
            Question(id, webinar_id -> Webinar, registration_id -> Registration, body, answered)
Features:   - Create a webinar with a registration page
            - Send reminder emails with a personal join link
            - Stream video with live chat and Q&A
            - Record the webinar and email the replay
            - Show attendance stats to the host
API:        REST
            POST /webinars
            POST /webinars/{id}/register
            GET  /join/{token}
            POST /webinars/{id}/questions
            GET  /webinars/{id}/stats
Storage:    PostgreSQL, S3 (recordings)
Tech stack: Node.js, NestJS, LiveKit, React, Stripe
```

---

## Example 415

**Intent:**
forum for women in tech

**Spec:**
```
Type:       Web application (community forum)
Auth:       Email + password, membership application
Data model: Member(id, name, email, password_hash, role_title, approved)
            Channel(id, name)
            Discussion(id, channel_id -> Channel, member_id -> Member, title, body)
            Reply(id, discussion_id -> Discussion, member_id -> Member, body)
Features:   - Approve membership applications
            - Discuss in channels like Career, Salary and Leadership
            - Post anonymously in sensitive channels
            - Share job openings
            - Enforce a code of conduct with reporting
API:        REST
            POST /applications
            GET  /channels/{id}/discussions
            POST /discussions
            POST /discussions/{id}/replies
            POST /reports
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 416

**Intent:**
site where parents rate kids birthday party venues

**Spec:**
```
Type:       Web application (review site)
Auth:       Email + password
Data model: Parent(id, name, email, password_hash)
            Venue(id, name, type, city, age_range, price_per_child)
            Review(id, venue_id -> Venue, parent_id -> Parent, rating, child_age, value_rating, body)
Features:   - Search venues by city, type and age range
            - Review venues with the child's age
            - Show value for money ratings
            - Show price per child
API:        REST
            GET  /venues?city=&age=
            GET  /venues/{id}
            POST /venues/{id}/reviews
Storage:    PostgreSQL
Tech stack: Node.js, Express, EJS
```

---

## Example 417

**Intent:**
AI website that turns lecture slides into study notes and flashcards

**Spec:**
```
Type:       Web application (AI study tool)
Auth:       Email + password or Google sign-in
Data model: Student(id, email)
            Deck(id, student_id -> Student, title, source_pdf_url)
            StudyNote(id, deck_id -> Deck, slide_number, note)
            Flashcard(id, deck_id -> Deck, front, back)
Features:   - Upload lecture slides as PDF or PowerPoint
            - Extract text per slide
            - Write study notes for each slide with an LLM
            - Generate flashcards from the notes
            - Export flashcards to Anki
API:        REST
            POST /decks
            GET  /decks/{id}/notes
            GET  /decks/{id}/flashcards
            GET  /decks/{id}/export.apkg
Storage:    PostgreSQL, S3 (uploads)
Tech stack: Python, FastAPI, PyMuPDF, python-pptx, genanki, OpenAI API
```

---

## Example 418

**Intent:**
we need a booking site for our community hall, groups book rooms and pay

**Spec:**
```
Type:       Web application (venue booking)
Auth:       Email + password for hirers, admin role for the hall manager
Data model: Hirer(id, name, organisation, email, password_hash)
            Room(id, name, capacity, hourly_rate)
            Booking(id, room_id -> Room, hirer_id -> Hirer, starts_at, ends_at, purpose, status, total)
            Invoice(id, booking_id -> Booking, amount, paid)
Features:   - Show room availability on a calendar
            - Request bookings for one-off or weekly sessions
            - Let the manager approve bookings
            - Invoice hirers and take card payments
            - Apply a discount for charities
API:        REST
            GET  /rooms/{id}/availability
            POST /bookings
            PATCH /admin/bookings/{id}
            GET  /invoices
            POST /invoices/{id}/pay
Storage:    PostgreSQL
Tech stack: PHP, Laravel, FullCalendar, Stripe
```

---

## Example 419

**Intent:**
plan a website for a youth football coaches community to share drills with diagrams

**Spec:**
```
Type:       Web application (coaching drills library)
Auth:       Email + password
Data model: Coach(id, name, email, password_hash, licence_level)
            Drill(id, coach_id -> Coach, title, age_group, focus, players_needed, diagram_json, instructions)
            Session(id, coach_id -> Coach, title, drill_ids)
            Rating(drill_id -> Drill, coach_id -> Coach, stars)
Features:   - Draw drill diagrams with players, cones and arrows
            - Filter drills by age group and focus
            - Build training sessions from several drills
            - Rate drills
            - Print a session plan
API:        REST
            GET  /drills?age=&focus=
            POST /drills
            POST /sessions
            GET  /sessions/{id}/print
            POST /drills/{id}/ratings
Storage:    PostgreSQL
Tech stack: TypeScript, React, Konva.js, Node.js
```

---

## Example 420

**Intent:**
link shortener saas with analytics for marketers

**Spec:**
```
Type:       Web application (link shortener SaaS)
Auth:       Email + password, team workspaces
Data model: Workspace(id, name, plan, custom_domain)
            Link(id, workspace_id -> Workspace, slug, target_url, utm_json, created_at)
            Click(id, link_id -> Link, clicked_at, country, referrer, device)
Features:   - Create short links with custom slugs and UTM tags
            - Redirect quickly from a custom domain
            - Record clicks with country, referrer and device
            - Show click charts per link
            - Limit links per month by plan
API:        REST
            POST /links
            GET  /links
            GET  /links/{id}/stats
            GET  /{slug}
Storage:    PostgreSQL, ClickHouse (clicks)
Tech stack: Go, Fiber, React, MaxMind GeoLite2
```

---

## Example 421

**Intent:**
a site where people leave anonymous thank-you notes for healthcare workers

**Spec:**
```
Type:       Web application (gratitude wall)
Data model: Note(id, message, hospital, author_initials, created_at, approved)
            Hospital(id, name, city)
Features:   - Post a short thank-you note without an account
            - Choose a hospital to send it to
            - Hold notes for moderation
            - Show approved notes on a wall
            - Let hospitals download their notes
API:        REST
            GET  /notes?hospital=
            POST /notes
            PATCH /admin/notes/{id}
            GET  /hospitals/{id}/notes.pdf
Storage:    PostgreSQL
Tech stack: Python, Flask, WeasyPrint
```

---

## Example 422

**Intent:**
help desk for my landscaping company where clients request quotes and track jobs

**Spec:**
```
Type:       Web application (client job portal)
Auth:       Email + password for clients, staff role
Data model: Client(id, name, email, password_hash, address)
            QuoteRequest(id, client_id -> Client, service, description, photos, status)
            Quote(id, request_id -> QuoteRequest, amount, valid_until, accepted)
            Job(id, quote_id -> Quote, scheduled_on, crew, status)
Features:   - Request a quote with photos of the garden
            - Send quotes the client can accept online
            - Schedule accepted jobs with a crew
            - Show clients the job status
            - Send an invoice when the job is done
API:        REST
            POST /requests
            POST /requests/{id}/quote
            POST /quotes/{id}/accept
            GET  /me/jobs
            PATCH /jobs/{id}
Storage:    PostgreSQL, S3 (photos)
Tech stack: Ruby on Rails, Stripe Invoicing
```

---
