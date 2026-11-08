## Example 1

**Intent:**
aquarium controller that keeps my reef tank temp and lights right

**Spec:**
```
Type:       IoT system (aquarium controller)
Data model: Tank(id, name, volume_l)
            Reading(id, tank_id -> Tank, temp_c, ph, recorded_at)
            LightSchedule(id, tank_id -> Tank, on_time, off_time, intensity_pct)
Features:   - Read water temperature and pH every minute
            - Switch the heater relay on and off to hold a target temperature
            - Dim LED lights on a sunrise and sunset schedule
            - Alert by push notification when temperature leaves the safe range
            - Show live and 7-day readings on a local web page
API:        REST
            GET  /tanks/{id}/readings
            PUT  /tanks/{id}/light-schedule
Storage:    SQLite on the controller
Tech stack: Raspberry Pi, Python, DS18B20 sensor, Atlas Scientific pH probe, Flask
```

---

## Example 2

**Intent:**
Hydroponics nutrient doser

**Spec:**
```
Type:       IoT system (hydroponics doser)
Data model: Reservoir(id, name, target_ec, target_ph)
            DoseEvent(id, reservoir_id -> Reservoir, pump, ml, dosed_at)
            SensorReading(id, reservoir_id -> Reservoir, ec, ph, recorded_at)
Features:   - Measure EC and pH of the nutrient reservoir every 10 minutes
            - Run peristaltic pumps to add nutrient A, nutrient B or pH-down
            - Limit dosing to a maximum ml per hour to avoid overshoot
            - Log every dose with the reading before and after
            - Warn when a stock bottle is estimated to be nearly empty
Storage:    SQLite
Tech stack: ESP32, MicroPython, MQTT, Node-RED dashboard
```

---

## Example 3

**Intent:**
I keep 6 beehives at the edge of our orchard and I'd love to know the weight of each hive and the temperature inside without opening them up all the time, because opening disturbs the bees. Ideally I check it from my phone.

**Spec:**
```
Type:       IoT system (beehive monitoring)
Data model: Hive(id, name, location, installed_at)
            HiveReading(id, hive_id -> Hive, weight_kg, inner_temp_c, humidity_pct, recorded_at)
Features:   - Weigh each hive with a load cell under the stand every hour
            - Measure brood temperature and humidity inside the hive
            - Send readings over LoRaWAN to a gateway
            - Detect a sudden weight drop and alert as a possible swarm
            - Chart weight gain per hive over the honey season on a mobile-friendly page
API:        REST
            GET  /hives
            GET  /hives/{id}/readings?from={date}
Storage:    InfluxDB
Tech stack: Arduino MKR WAN 1310, HX711 load cell amplifier, The Things Network, Grafana
```

---

## Example 4

**Intent:**
hens keep getting out late, want the coop hatch to shut itself after dusk and pop open at dawn

**Spec:**
```
Type:       IoT system (coop door controller)
Data model: DoorEvent(id, action, trigger, happened_at)
            Settings(latitude, longitude, open_offset_min, close_offset_min)
Features:   - Calculate sunrise and sunset times from the coop location
            - Drive a linear actuator to open and close the door
            - Confirm the door position with a reed switch and retry on failure
            - Send an SMS if the door fails to close at night
            - Allow manual open and close from a small web page
Storage:    JSON file on the device
Tech stack: ESP8266, Arduino C++, Twilio SMS API
```

---

## Example 5

**Intent:**
we deliver vaccines and need proof the boxes stayed between 2 and 8 degrees the whole trip

**Spec:**
```
Type:       IoT system (cold-chain logging)
Data model: Shipment(id, reference, origin, destination, departed_at, arrived_at)
            Logger(id, serial, battery_pct)
            TempReading(id, shipment_id -> Shipment, logger_id -> Logger, temp_c, recorded_at)
            Excursion(id, shipment_id -> Shipment, started_at, ended_at, max_temp_c)
Features:   - Upload readings from a Bluetooth data logger when the box is opened
            - Detect excursions outside 2 to 8 °C and record their duration
            - Generate a signed PDF temperature report per shipment
            - Share a read-only report link with the receiving clinic
            - Flag loggers with low battery before dispatch
API:        REST
            POST /shipments
            POST /shipments/{id}/readings
            GET  /shipments/{id}/report.pdf
Storage:    PostgreSQL
Tech stack: Python, Django, React Native (logger upload app), WeasyPrint
```

---

## Example 6

**Intent:**
Freezer alarm for my restaurant walk-in, text me if it goes above -15

**Spec:**
```
Type:       IoT system (freezer alarm)
Data model: Freezer(id, name, threshold_c)
            Reading(id, freezer_id -> Freezer, temp_c, recorded_at)
            Alert(id, freezer_id -> Freezer, sent_at, acknowledged_at)
Features:   - Read the freezer temperature every 2 minutes
            - Send an SMS when the temperature stays above -15 °C for 10 minutes
            - Repeat the alert every 15 minutes until someone acknowledges it
            - Keep a daily temperature log for health inspections
            - Export the log to CSV
Storage:    SQLite
Tech stack: Raspberry Pi Zero W, Python, DS18B20 waterproof probe, Twilio
```

---

## Example 7

**Intent:**
Water leak sensors under sinks and washing machine, shut the main valve if leak

**Spec:**
```
Type:       IoT system (leak detection)
Data model: Sensor(id, location, battery_pct)
            LeakEvent(id, sensor_id -> Sensor, detected_at, cleared_at)
            ValveAction(id, action, reason, happened_at)
Features:   - Detect water on the floor with Zigbee leak sensors
            - Close a motorized main water valve as soon as a leak is reported
            - Send a push notification naming the room
            - Let the user reopen the valve from the app after the leak is cleared
            - Warn when a sensor battery is low
Storage:    SQLite
Tech stack: Home Assistant, Zigbee2MQTT, Zigbee leak sensors, motorized ball valve
```

---

## Example 8

**Intent:**
tell me when the post arrives in my mailbox at the end of the driveway

**Spec:**
```
Type:       IoT system (smart mailbox)
Data model: MailEvent(id, type, happened_at)
            Device(id, battery_v, last_seen_at)
Features:   - Detect the mailbox flap opening with a tilt switch
            - Distinguish a delivery from a pickup by checking if the door was opened after
            - Send a phone notification when mail arrives
            - Sleep between events to run for months on batteries
            - Report battery voltage once a day
Tech stack: ESP32 with deep sleep, LoRa radio, Pushover API
```

---

## Example 9

**Intent:**
Parking occupancy sensors for our office garage so people know if there's a free spot before driving in

**Spec:**
```
Type:       IoT system (parking occupancy)
Data model: Level(id, name)
            Space(id, level_id -> Level, code, is_ev)
            OccupancyEvent(id, space_id -> Space, occupied, changed_at)
Features:   - Detect a car in each space with an ultrasonic sensor
            - Update each space status in real time
            - Show free spaces per level on a display at the entrance
            - Show the same map on an internal web page
            - Report average occupancy by hour for facility planning
API:        REST
            GET  /levels
            GET  /levels/{id}/spaces
            GET  /reports/occupancy?date={date}
Storage:    PostgreSQL, Redis (live status)
Tech stack: ESP32, HC-SR04 sensors, MQTT, Node.js, Vue.js
```

---

## Example 10

**Intent:**
count how many people come into our small shop each hour

**Spec:**
```
Type:       IoT system (people counter)
Data model: CountEvent(id, direction, happened_at)
            HourlyTotal(date, hour, entries, exits)
Features:   - Detect people passing the door with a pair of infrared beams
            - Work out direction from which beam breaks first
            - Aggregate entries and exits per hour
            - Show today's count and busiest hours on a dashboard
            - Export monthly totals to CSV
Storage:    SQLite
Tech stack: Raspberry Pi, Python, IR break-beam sensors, Streamlit
```

---

## Example 11

**Intent:**
A noise meter for my classroom that shows green yellow red so the kids know when they're too loud

**Spec:**
```
Type:       IoT system (classroom noise meter)
Data model: NoiseSample(id, db_level, recorded_at)
            Settings(yellow_db, red_db)
Features:   - Measure sound level with a microphone module several times a second
            - Light an LED strip green, yellow or red based on thresholds
            - Let the teacher adjust thresholds with two buttons
            - Log the average level per lesson
            - Show a weekly chart of noisy periods
Storage:    SD card (CSV)
Tech stack: Arduino Nano, MAX4466 microphone, WS2812B LED strip
```

---

## Example 12

**Intent:**
school bell system that rings on schedule and has different timetables for exam days

**Spec:**
```
Type:       IoT system (school bell scheduler)
Data model: Timetable(id, name)
            BellTime(id, timetable_id -> Timetable, weekday, time, sound)
            CalendarDay(date, timetable_id -> Timetable)
Features:   - Store multiple timetables such as normal, exam and half day
            - Assign a timetable to each calendar date
            - Trigger the bell relay and play a chosen sound at each bell time
            - Silence bells on holidays automatically
            - Let staff ring the bell manually from the web panel
API:        REST
            GET  /timetables
            POST /timetables/{id}/bells
            PUT  /calendar/{date}
Storage:    SQLite
Tech stack: Raspberry Pi, Python, Flask, relay module, NTP time sync
```

---

## Example 13

**Intent:**
i run a small gym and want to know which machines actually get used, thinking of selling some

**Spec:**
```
Type:       IoT system (gym equipment usage)
Data model: Machine(id, name, zone)
            UsageSession(id, machine_id -> Machine, started_at, ended_at)
Features:   - Detect use of each machine with a vibration or motion sensor
            - Group movement into usage sessions with start and end time
            - Calculate daily minutes in use per machine
            - Rank machines by usage over the last 90 days
            - Show peak hours per machine on a dashboard
Storage:    TimescaleDB
Tech stack: ESP32, MPU-6050 accelerometer, MQTT, Python, Grafana
```

---

## Example 14

**Intent:**
OEE dashboard for our 4 CNC machines

**Spec:**
```
Type:       Data dashboard (OEE tracking)
Data model: Machine(id, name, ideal_cycle_s)
            Shift(id, name, start_time, end_time)
            StateEvent(id, machine_id -> Machine, state, started_at)
            PartCount(id, machine_id -> Machine, good, scrap, counted_at)
Features:   - Collect run, idle and down states from each machine controller
            - Calculate availability, performance and quality per shift
            - Show OEE per machine as a live gauge
            - List the top downtime reasons for the week
            - Export shift reports to Excel
API:        REST
            GET  /machines/{id}/oee?shift={id}
            GET  /downtime/reasons?week={n}
Storage:    PostgreSQL
Tech stack: Python, OPC UA client, FastAPI, React, Recharts
```

---

## Example 15

**Intent:**
put vibration sensors on our pumps and warn us before the bearing fails

**Spec:**
```
Type:       IoT system (predictive maintenance)
Data model: Asset(id, name, type, rpm)
            VibrationSample(id, asset_id -> Asset, rms_g, peak_freq_hz, recorded_at)
            Alarm(id, asset_id -> Asset, level, reason, raised_at)
Features:   - Sample 3-axis vibration on each pump at 1 kHz
            - Compute RMS and an FFT spectrum on the edge device
            - Compare readings with a baseline learned in the first two weeks
            - Raise warning and critical alarms when bearing frequencies grow
            - Show the trend per asset to the maintenance team
API:        REST
            GET  /assets/{id}/trend
            GET  /alarms?open=true
Storage:    InfluxDB
Tech stack: ESP32, ADXL345 accelerometer, Python, NumPy, SciPy, Grafana
```

---

## Example 16

**Intent:**
Solar panel monitor for my roof, I have an inverter with modbus

**Spec:**
```
Type:       IoT system (solar monitoring)
Data model: InverterReading(id, ac_power_w, dc_voltage, energy_today_kwh, recorded_at)
            DailySummary(date, energy_kwh, peak_w)
Features:   - Poll the inverter over Modbus TCP every 30 seconds
            - Store power and energy readings
            - Show current output and today's production on a dashboard
            - Compare daily production with the forecast for the location
            - Alert when production is near zero on a sunny day
Storage:    InfluxDB
Tech stack: Python, pymodbus, InfluxDB, Grafana, Solcast API
```

---

## Example 17

**Intent:**
charge my electric car only when electricity is cheapest at night

**Spec:**
```
Type:       Scheduled script (EV charging scheduler)
Data model: PriceSlot(start_at, price_per_kwh)
            ChargePlan(id, target_soc_pct, ready_by, created_at)
            ChargeSession(id, plan_id -> ChargePlan, started_at, ended_at, kwh)
Features:   - Fetch next-day hourly electricity prices from the supplier
            - Estimate how many hours are needed to reach the target charge
            - Pick the cheapest hours before the ready-by time
            - Start and stop the wallbox over OCPP at the chosen hours
            - Report the cost of each charging session
Storage:    SQLite
Tech stack: Python, Nord Pool price API, OCPP 1.6 (python-ocpp), cron
```

---

## Example 18

**Intent:**
My boat is in a marina 2 hours away and I worry about the bilge filling up with water or the battery dying in winter. I want something that checks the bilge pump and battery and messages me.

**Spec:**
```
Type:       IoT system (boat monitoring)
Data model: Boat(id, name, berth)
            Reading(id, boat_id -> Boat, battery_v, bilge_level_cm, pump_running, recorded_at)
            Alert(id, boat_id -> Boat, type, sent_at)
Features:   - Measure house battery voltage and bilge water level
            - Count how often and how long the bilge pump runs
            - Send readings every 15 minutes over a 4G modem
            - Alert by SMS when the battery is low or the bilge pump runs too often
            - Show the last 30 days of readings on a web page
Storage:    PostgreSQL
Tech stack: ESP32 with SIM7000 LTE module, MQTT, Python, Telegram Bot API
```

---

## Example 19

**Intent:**
ham radio logbook app that can export ADIF

**Spec:**
```
Type:       Desktop application (ham radio logging)
Data model: Contact(id, callsign, frequency_mhz, band, mode, rst_sent, rst_rcvd, grid, logged_at)
            Station(id, my_callsign, my_grid)
Features:   - Log a contact with callsign, band, mode and signal reports
            - Read the current frequency and mode from the rig via CAT
            - Look up the operator name and grid square by callsign
            - Mark duplicate contacts during a contest
            - Import and export logs in ADIF format
Storage:    SQLite
Tech stack: Python, PySide6, Hamlib, QRZ.com XML API
```

---

## Example 20

**Intent:**
drone flight log for our survey company, need pilot hours and battery cycles for compliance

**Spec:**
```
Type:       Web application (drone flight log)
Data model: Pilot(id, name, licence_no)
            Drone(id, model, serial, registration)
            Battery(id, drone_id -> Drone, serial, cycle_count)
            Flight(id, pilot_id -> Pilot, drone_id -> Drone, battery_id -> Battery, site, takeoff_at, landing_at, max_altitude_m)
Features:   - Import flights from DJI flight log files
            - Record pilot, drone, battery and site per flight
            - Total flight hours per pilot for licence renewal
            - Count battery cycles and warn when a battery needs retirement
            - Export a compliance report per date range as PDF
API:        REST
            POST /flights/import
            GET  /pilots/{id}/hours
            GET  /batteries?needs_retirement=true
Storage:    PostgreSQL
Tech stack: Python, Django, Django REST Framework, React
```

---

## Example 21

**Intent:**
robotics competition scoring app for judges at the field

**Spec:**
```
Type:       Web application (competition scoring)
Data model: Team(id, number, name, school)
            Match(id, round, field, red_team_ids, blue_team_ids, status)
            Score(id, match_id -> Match, team_id -> Team, auto_pts, teleop_pts, penalties)
Features:   - Show the match schedule per field
            - Enter autonomous and teleop scores on a tablet
            - Apply penalties and calculate totals
            - Rank teams by average score after each round
            - Show live rankings on a projector screen
API:        REST
            GET  /matches?field={n}
            POST /matches/{id}/scores
            GET  /rankings
Storage:    PostgreSQL
Tech stack: Node.js, Express, Socket.IO, Svelte
```

---

## Example 22

**Intent:**
my grandmother lives alone and fell twice last year, nobody found her for hours. I want a small device she wears that detects a fall and calls me automatically

**Spec:**
```
Type:       IoT system (wearable fall detection)
Data model: Wearer(id, name, emergency_contacts)
            FallEvent(id, wearer_id -> Wearer, detected_at, cancelled, latitude, longitude)
            Heartbeat(id, wearer_id -> Wearer, battery_pct, seen_at)
Features:   - Detect falls from accelerometer impact followed by no movement
            - Give the wearer 30 seconds to cancel with a button
            - Call and text emergency contacts with the location
            - Send a daily check-in so family knows the device works
            - Warn family when the battery drops below 20 percent
Storage:    PostgreSQL (backend)
Tech stack: nRF52840 wearable, Zephyr RTOS, BLE to phone, Flutter companion app, Twilio
```

---

## Example 23

**Intent:**
Smart pill dispenser that drops the right pills at the right time and tells my son if I miss them

**Spec:**
```
Type:       IoT system (smart pill dispenser)
Data model: Medication(id, name, compartment)
            DoseSchedule(id, medication_id -> Medication, time, count)
            DoseEvent(id, schedule_id -> DoseSchedule, dispensed_at, taken_at, missed)
Features:   - Rotate the carousel to release the scheduled compartment
            - Beep and flash until the tray is lifted
            - Mark a dose as missed after 30 minutes
            - Notify a caregiver by app when a dose is missed
            - Let the caregiver edit the schedule remotely
API:        REST
            GET  /schedule
            PUT  /schedule
            GET  /doses?date={date}
Storage:    Firebase Firestore
Tech stack: ESP32, stepper motor, Arduino C++, Firebase, Flutter
```

---

## Example 24

**Intent:**
glove with flex sensors that translates sign language letters to speech

**Spec:**
```
Type:       IoT system (sign language glove)
Features:   - Read five flex sensors and an IMU on the glove
            - Classify hand shapes into fingerspelled letters with a small model
            - Join letters into words after a pause
            - Speak words through a phone app using text-to-speech
            - Let the user record new samples to retrain a letter
Tech stack: Arduino Nano 33 BLE Sense, TensorFlow Lite Micro, BLE, Android (Kotlin)
```

---

## Example 25

**Intent:**
assistive switch so my son who can only move his head can use the tablet

**Spec:**
```
Type:       IoT system (assistive switch interface)
Data model: SwitchProfile(id, name, scan_speed_ms, action_map)
Features:   - Read a large head-activated switch through a USB adapter
            - Present itself as a Bluetooth keyboard to the tablet
            - Map single and long presses to next and select
            - Adjust debounce and hold times for the user's motor control
            - Store several profiles for different apps
Storage:    Flash memory on the device
Tech stack: Adafruit Feather nRF52840, CircuitPython, BLE HID
```

---

## Example 26

**Intent:**
preflight checklist app for small plane pilots, works offline

**Spec:**
```
Type:       Mobile application (aviation checklist)
Data model: Aircraft(id, registration, type)
            Checklist(id, aircraft_id -> Aircraft, phase, title)
            ChecklistItem(id, checklist_id -> Checklist, position, challenge, response)
            Run(id, checklist_id -> Checklist, completed_at)
Features:   - Show checklists by phase such as preflight, before takeoff and landing
            - Tick items one at a time with large touch targets
            - Read items aloud with text-to-speech
            - Edit checklists per aircraft
            - Work fully offline and log completed runs
Storage:    Local SQLite on the device
Tech stack: Swift, SwiftUI, AVSpeechSynthesizer
```

---

## Example 27

**Intent:**
dispatch board for our volunteer fire brigade, who is available and which truck goes

**Spec:**
```
Type:       Web application (emergency dispatch board)
Data model: Volunteer(id, name, phone, qualifications)
            Availability(id, volunteer_id -> Volunteer, available, updated_at)
            Truck(id, call_sign, status)
            Incident(id, type, address, created_at)
            Response(id, incident_id -> Incident, volunteer_id -> Volunteer, eta_min)
Features:   - Page all available volunteers when an incident is created
            - Let volunteers reply attending or not with an ETA
            - Show who is coming and their qualifications on a station screen
            - Assign trucks and track their status
            - Keep an incident log for reports
API:        REST
            POST /incidents
            POST /incidents/{id}/responses
            GET  /availability
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire, Twilio
```

---

## Example 28

**Intent:**
intake form for our legal aid clinic so we can check if people qualify before an appointment

**Spec:**
```
Type:       Web application (legal aid intake)
Data model: Applicant(id, name, contact, household_size, monthly_income)
            Case(id, applicant_id -> Applicant, legal_area, summary, status)
            ConflictCheck(id, case_id -> Case, opposing_party, result)
Features:   - Collect applicant details and the legal problem in a guided form
            - Check income against the eligibility threshold by household size
            - Run a conflict check on the opposing party name
            - Route the case to the right legal area queue
            - Let staff book an appointment for eligible applicants
API:        REST
            POST /intake
            GET  /cases?status=new
            POST /cases/{id}/conflict-check
Storage:    PostgreSQL (encrypted at rest)
Tech stack: Python, Django, HTMX
```

---

## Example 29

**Intent:**
we help refugees and need to track which family got what help, and in Arabic and Ukrainian too

**Spec:**
```
Type:       Web application (refugee case management)
Data model: Household(id, head_name, size, origin_country, arrival_date)
            Member(id, household_id -> Household, name, birth_year)
            Service(id, name, category)
            ServiceRecord(id, household_id -> Household, service_id -> Service, given_at, caseworker_id)
Features:   - Register households and their members
            - Record services given such as housing, language classes and food
            - Show a timeline of support per household
            - Translate the interface into English, Arabic and Ukrainian with right-to-left support
            - Report numbers served per month for funders
API:        REST
            POST /households
            POST /households/{id}/services
            GET  /reports/monthly
Storage:    PostgreSQL
Tech stack: Next.js, Prisma, i18next
```

---

## Example 30

**Intent:**
prison visitation booking so families can book a slot online instead of calling

**Spec:**
```
Type:       Web application (visit booking)
Data model: Inmate(id, number, unit)
            Visitor(id, name, id_document_no, approved)
            VisitSlot(id, unit, starts_at, capacity)
            Booking(id, slot_id -> VisitSlot, inmate_id -> Inmate, visitor_id -> Visitor, status)
Features:   - Show available visit slots for the inmate's unit
            - Allow only visitors on the inmate's approved list to book
            - Limit the number of visits per inmate per week
            - Let staff confirm, cancel or move bookings
            - Send email confirmation and reminders
API:        REST
            GET  /slots?inmate={number}
            POST /bookings
            PATCH /bookings/{id}
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Thymeleaf
```

---

## Example 31

**Intent:**
Digitise our old cemetery burial records and plot map

**Spec:**
```
Type:       Web application (cemetery records)
Data model: Section(id, name)
            Plot(id, section_id -> Section, row, number, status, lat, lng)
            Burial(id, plot_id -> Plot, full_name, birth_date, death_date, burial_date)
            Photo(id, plot_id -> Plot, url)
Features:   - Enter burial records and link them to plots
            - Search burials by name or date
            - Show plots on an interactive map with available plots highlighted
            - Attach headstone photos to plots
            - Export records for genealogy researchers
API:        REST
            GET  /burials?name={q}
            GET  /plots?section={id}
            POST /plots/{id}/photos
Storage:    PostgreSQL with PostGIS, S3 (photos)
Tech stack: Python, Django, Leaflet.js
```

---

## Example 32

**Intent:**
grow tent humidity fan controller

**Spec:**
```
Type:       IoT system (grow tent climate)
Features:   - Read temperature and humidity in the tent
            - Speed up the exhaust fan when humidity is above target
            - Turn on a humidifier when humidity is too low
            - Show values on a small OLED screen
            - Keep the last 24 hours of readings in memory
Tech stack: ESP32, SHT31 sensor, PWM fan control, Arduino C++
```

---

## Example 33

**Intent:**
coffee roaster logger, plot bean temperature during roast

**Spec:**
```
Type:       Desktop application (roast logger)
Data model: Roast(id, bean_name, green_weight_g, roasted_weight_g, started_at)
            RoastPoint(id, roast_id -> Roast, seconds, bean_temp_c, env_temp_c)
            Event(id, roast_id -> Roast, name, seconds)
Features:   - Read bean and environment temperatures from thermocouples over USB
            - Plot a live temperature curve and rate of rise
            - Mark first crack, second crack and drop events
            - Overlay a previous roast as a reference profile
            - Calculate weight loss percentage
Storage:    SQLite
Tech stack: Python, PyQt6, pyqtgraph, MAX31855 thermocouple board
```

---

## Example 34

**Intent:**
alarm when the sump pump in my basement stops working

**Spec:**
```
Type:       IoT system (sump pump monitor)
Features:   - Measure the water level in the sump pit with a float sensor
            - Sense pump current with a clamp sensor
            - Alert when water rises but the pump does not start
            - Report pump run cycles per day
            - Send alerts by email and push notification
Storage:    SQLite
Tech stack: ESP32, SCT-013 current sensor, ESPHome, Home Assistant
```

---

## Example 35

**Intent:**
wine cellar temp humidity logger

**Spec:**
```
Type:       IoT system (cellar monitoring)
Data model: Reading(id, temp_c, humidity_pct, recorded_at)
Features:   - Record temperature and humidity every 10 minutes
            - Alert when temperature leaves 10 to 15 °C
            - Alert when humidity drops under 55 percent
            - Show monthly min, max and average values
Storage:    InfluxDB
Tech stack: Raspberry Pi Pico W, BME280, MicroPython, InfluxDB Cloud
```

---

## Example 36

**Intent:**
pls make sth to track fridge temps in our school canteen, inspector wants records twice a day

**Spec:**
```
Type:       Web application (food safety temperature log)
Data model: Appliance(id, name, type, min_c, max_c)
            TempCheck(id, appliance_id -> Appliance, temp_c, checked_by, checked_at, corrective_action)
Features:   - List fridges and freezers with their allowed ranges
            - Record a morning and afternoon temperature per appliance
            - Require a corrective action note when a reading is out of range
            - Remind staff when a check is overdue
            - Print a monthly log for the inspector
API:        REST
            GET  /appliances
            POST /checks
            GET  /checks/report?month={m}
Storage:    SQLite
Tech stack: PHP, Laravel, Blade
```

---

## Example 37

**Intent:**
Ice rink in our town, want to show the ice temperature and the zamboni schedule on a screen in the lobby

**Spec:**
```
Type:       Web application (rink information display)
Data model: IceReading(id, surface_temp_c, recorded_at)
            ResurfaceSlot(id, starts_at, ends_at)
            Session(id, name, starts_at, ends_at)
Features:   - Read the ice surface temperature from an infrared sensor
            - Show current ice temperature on a lobby screen
            - Show today's public sessions and resurfacing breaks
            - Let staff edit the schedule from a web form
            - Rotate announcements between schedule views
API:        REST
            GET  /display
            POST /sessions
            POST /resurface-slots
Storage:    SQLite
Tech stack: Raspberry Pi, MLX90614 IR sensor, Python, Flask, Chromium kiosk mode
```

---

## Example 38

**Intent:**
bike counter on our cycle path for the city council

**Spec:**
```
Type:       IoT system (bicycle counter)
Data model: Counter(id, location, installed_at)
            PassEvent(id, counter_id -> Counter, direction, passed_at)
            DailyCount(counter_id -> Counter, date, inbound, outbound)
Features:   - Detect bicycles with an inductive loop or radar sensor
            - Count passes by direction
            - Send daily counts over NB-IoT
            - Publish counts as open data
            - Show a public chart comparing weekdays and weekends
API:        REST
            GET  /counters
            GET  /counters/{id}/daily?from={date}&to={date}
Storage:    PostgreSQL
Tech stack: STM32, NB-IoT modem, Python, FastAPI, Chart.js
```

---

## Example 39

**Intent:**
horse stable water trough level sensor

**Spec:**
```
Type:       IoT system (trough level monitoring)
Features:   - Measure the water level in each trough with an ultrasonic sensor
            - Send levels over LoRa to a barn gateway
            - Alert the owner when a trough is below 20 percent
            - Detect a trough that empties unusually fast as a possible leak
            - Show all troughs on one phone screen
Storage:    SQLite on the gateway
Tech stack: Heltec LoRa32, JSN-SR04T sensor, Raspberry Pi gateway, Node-RED
```

---

## Example 40

**Intent:**
elevator downtime tracker for a building management company with 40 buildings

**Spec:**
```
Type:       Web application (elevator uptime)
Data model: Building(id, name, address)
            Elevator(id, building_id -> Building, code, installed_year)
            Outage(id, elevator_id -> Elevator, started_at, ended_at, cause)
            Inspection(id, elevator_id -> Elevator, date, result)
Features:   - Receive fault signals from elevator controllers
            - Open an outage automatically and notify the on-call technician
            - Close outages when the elevator reports normal again
            - Calculate uptime per elevator per month
            - Remind managers about upcoming legal inspections
API:        REST
            POST /elevators/{id}/faults
            GET  /outages?open=true
            GET  /reports/uptime?month={m}
Storage:    PostgreSQL
Tech stack: Go, Gin, React, MQTT
```

---

## Example 41

**Intent:**
Need a thing that logs when our generator runs and fuel level at the cell tower site

**Spec:**
```
Type:       IoT system (remote generator monitoring)
Data model: Site(id, name, lat, lng)
            GeneratorRun(id, site_id -> Site, started_at, stopped_at)
            FuelReading(id, site_id -> Site, level_pct, recorded_at)
Features:   - Detect generator start and stop from its output voltage
            - Measure fuel tank level with a pressure sensor
            - Send data over satellite or cellular when available
            - Estimate days of fuel left from recent consumption
            - Alert operations when fuel is below 25 percent
Storage:    PostgreSQL with TimescaleDB
Tech stack: Teltonika RUT router, Modbus RTU, Python, TimescaleDB, Grafana
```

---

## Example 42

**Intent:**
smoker bbq controller with meat probe and app

**Spec:**
```
Type:       IoT system (BBQ temperature controller)
Features:   - Read pit and meat probe temperatures
            - Control a blower fan with PID to hold pit temperature
            - Show temperatures and a live graph on a phone app over Wi-Fi
            - Alert when the meat reaches target temperature
            - Save cook logs with notes
Storage:    SPIFFS on the device
Tech stack: ESP32, MAX31865 RTD amplifier, Arduino C++, Blynk
```

---

## Example 43

**Intent:**
kombucha fermentation tracker for my small brewery, ph and temp per batch

**Spec:**
```
Type:       Web application (fermentation tracking)
Data model: Batch(id, tea_blend, volume_l, started_at, bottled_at)
            Measurement(id, batch_id -> Batch, ph, temp_c, brix, measured_at)
Features:   - Create batches with tea blend and volume
            - Log pH, temperature and sugar readings
            - Pull temperature automatically from a wireless probe
            - Mark a batch ready when pH reaches the target
            - Chart fermentation curves to compare batches
API:        REST
            POST /batches
            POST /batches/{id}/measurements
            GET  /batches/{id}/chart
Storage:    PostgreSQL
Tech stack: Python, Flask, Chart.js, Tilt hydrometer integration
```

---

## Example 44

**Intent:**
my clinic has a vaccine fridge and the power goes out sometimes. what i want is that it log the temperature and if power cut it send SMS to me and the nurse

**Spec:**
```
Type:       IoT system (vaccine fridge monitor)
Data model: Reading(id, temp_c, mains_power, recorded_at)
            Contact(id, name, phone)
Features:   - Read fridge temperature every minute
            - Detect mains power loss and run on a backup battery
            - Send SMS to all contacts on power cut or temperature out of 2 to 8 °C
            - Send a recovery SMS when power returns
            - Keep 12 months of readings for audits
Storage:    SD card and SQLite
Tech stack: Arduino Mega, SIM800L GSM module, DS18B20, Python sync script
```

---

## Example 45

**Intent:**
Office meeting room sensor that knows if a booked room is actually empty and releases it

**Spec:**
```
Type:       IoT system (room occupancy)
Data model: Room(id, name, capacity, calendar_id)
            OccupancyReading(id, room_id -> Room, occupied, recorded_at)
            Release(id, room_id -> Room, booking_id, released_at)
Features:   - Detect presence with a PIR or mmWave sensor in each room
            - Read room bookings from Microsoft 365 calendars
            - Release a booking if the room is empty 10 minutes after the start
            - Notify the organiser that the room was released
            - Report booked-but-unused hours per room
Storage:    PostgreSQL
Tech stack: ESP32, LD2410 mmWave sensor, Python, Microsoft Graph API
```

---

## Example 46

**Intent:**
data logger for a weather balloon launch with our physics class

**Spec:**
```
Type:       IoT system (high-altitude balloon logger)
Features:   - Log GPS position, altitude, temperature and pressure every 5 seconds
            - Save data to an SD card in CSV format
            - Transmit position over LoRa for tracking
            - Detect burst from a sudden altitude drop
            - Plot the flight path and altitude profile after recovery
Tech stack: Arduino, u-blox GPS, BMP388 sensor, LoRa RFM95, Python, matplotlib
```

---

## Example 47

**Intent:**
rfid tool crib checkout for the workshop so we know who took the drill

**Spec:**
```
Type:       IoT system (tool checkout)
Data model: Worker(id, name, badge_uid)
            Tool(id, name, tag_uid)
            Checkout(id, tool_id -> Tool, worker_id -> Worker, out_at, returned_at)
Features:   - Scan a worker badge and then the tool tag to check a tool out
            - Scan the tool again to return it
            - Show which tools are out and with whom
            - Flag tools out for more than 3 days
            - Show checkout history per tool
API:        REST
            POST /checkouts
            POST /returns
            GET  /tools?status=out
Storage:    SQLite
Tech stack: Raspberry Pi, RC522 RFID reader, Python, Flask
```

---

## Example 48

**Intent:**
Pond oxygen pump timer

**Spec:**
```
Type:       IoT system (pond aeration)
Features:   - Run the air pump on a daily schedule
            - Increase pump time on hot nights when dissolved oxygen drops
            - Read water temperature as a proxy for oxygen demand
            - Allow manual override from a button
            - Show the schedule and status on a small web page
Tech stack: ESP8266, Tasmota, DS18B20 sensor
```

---

## Example 49

**Intent:**
koi pond filter clog alert

**Spec:**
```
Type:       IoT system (pond filter monitoring)
Features:   - Measure the water level difference before and after the filter
            - Detect a clogged filter when the difference passes a threshold
            - Send a push notification to clean the filter
            - Log cleaning dates when the alert is acknowledged
Storage:    SQLite
Tech stack: ESP32, two pressure level sensors, Home Assistant
```

---

## Example 50

**Intent:**
track fuel usage of our fishing boats

**Spec:**
```
Type:       Web application (vessel fuel tracking)
Data model: Vessel(id, name, engine_type)
            Trip(id, vessel_id -> Vessel, departed_at, returned_at, catch_kg)
            FuelLog(id, trip_id -> Trip, litres, flow_meter_reading)
Features:   - Read engine fuel flow from an onboard NMEA 2000 gateway
            - Total fuel used per trip
            - Calculate litres per kg of catch
            - Compare vessels over a season
            - Export monthly fuel reports for tax claims
API:        REST
            POST /trips
            POST /trips/{id}/fuel
            GET  /vessels/{id}/efficiency
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Yacht Devices NMEA gateway, React
```

---

## Example 51

**Intent:**
Logbook for ham radio contests on raspberry pi, shared between 3 operators on a LAN

**Spec:**
```
Type:       Web application (contest logging)
Data model: Operator(id, callsign)
            QSO(id, operator_id -> Operator, callsign, band, mode, exchange, logged_at)
            Multiplier(id, type, value, first_qso_id -> QSO)
Features:   - Log contacts from several operator stations at the same time
            - Check for duplicates across all stations instantly
            - Track new multipliers and highlight them
            - Show a live score and rate per hour
            - Export the log in Cabrillo format
API:        REST
            POST /qsos
            GET  /qsos/dupe-check?call={c}&band={b}
            GET  /score
Storage:    SQLite on the Raspberry Pi
Tech stack: Raspberry Pi, Python, FastAPI, WebSockets, Vue.js
```

---

## Example 52

**Intent:**
APRS tracker for my car that shows on a map

**Spec:**
```
Type:       IoT system (APRS position tracking)
Features:   - Read GPS position every 30 seconds
            - Encode position as an APRS packet
            - Transmit over a 2 m radio with smart beaconing
            - Forward packets to APRS-IS when an internet gateway is in range
            - Display the track on a web map
Tech stack: Arduino, NEO-6M GPS, LibAPRS, Baofeng radio, aprs.fi
```

---

## Example 53

**Intent:**
satelite pass predictor for my antenna rotator

**Spec:**
```
Type:       Command-line tool (satellite tracking)
Features:   - Download current TLE data from CelesTrak
            - Predict upcoming passes with start, max elevation and end times
            - Point the antenna rotator in azimuth and elevation during a pass
            - Apply Doppler correction to the radio frequency
            - Print a table of passes for the next 24 hours
Tech stack: Python, Skyfield, Hamlib rotctld
```

---

## Example 54

**Intent:**
drone battery health tracker

**Spec:**
```
Type:       Mobile application (drone battery tracking)
Data model: Battery(id, label, capacity_mah, purchased_at)
            Cycle(id, battery_id -> Battery, start_pct, end_pct, cell_delta_mv, flown_at)
Features:   - Register batteries with a QR label
            - Log each flight's start and end charge
            - Record cell voltage difference after flight
            - Warn when a battery shows swelling or high cell imbalance
            - Sort batteries by health score
Storage:    Local SQLite on the device
Tech stack: Kotlin, Jetpack Compose, ML Kit barcode scanning
```

---

## Example 55

**Intent:**
preflight checks for our drone team, each pilot must complete before flying, office needs to see it

**Spec:**
```
Type:       Mobile application with backend (drone preflight checks)
Data model: Pilot(id, name)
            Checklist(id, name, version)
            CheckItem(id, checklist_id -> Checklist, text, required)
            Submission(id, pilot_id -> Pilot, checklist_id -> Checklist, site, lat, lng, submitted_at, all_passed)
Features:   - Complete a preflight checklist on the phone before each flight
            - Record the GPS location and site name
            - Block submission until required items are ticked
            - Attach airspace authorisation photos
            - Show all submissions to the office in a web view
API:        REST
            GET  /checklists
            POST /submissions
            GET  /submissions?date={d}
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Express
```

---

## Example 56

**Intent:**
FRC robot telemetry dashboard

**Spec:**
```
Type:       Desktop application (robot telemetry)
Features:   - Connect to the robot over NetworkTables
            - Plot motor currents, battery voltage and encoder values live
            - Record matches to a log file
            - Replay a recorded match with a timeline slider
            - Highlight brownout events
Storage:    Local log files (WPILOG)
Tech stack: Java, WPILib NetworkTables, JavaFX
```

---

## Example 57

**Intent:**
scouting app for robotics team, we collect data on other teams at events

**Spec:**
```
Type:       Mobile application with backend (robotics scouting)
Data model: Event(id, code, name)
            TeamProfile(id, number, name)
            MatchReport(id, event_id -> Event, team_id -> TeamProfile, match_no, auto_points, cycles, climbed, notes, scout_name)
Features:   - Fill a match scouting form per robot during matches
            - Work offline and sync when Wi-Fi is available
            - Pull the match schedule from The Blue Alliance API
            - Average stats per team
            - Build a ranked pick list for alliance selection
API:        REST
            POST /reports
            GET  /events/{code}/teams/{n}/stats
            GET  /events/{code}/picklist
Storage:    PostgreSQL, SQLite (offline on device)
Tech stack: Flutter, Python, FastAPI, The Blue Alliance API
```

---

## Example 58

**Intent:**
line follower robot for the school contest

**Spec:**
```
Type:       IoT system (line follower robot)
Features:   - Read an array of 8 infrared reflectance sensors
            - Compute the line position as a weighted average
            - Steer the two motors with a PID controller
            - Tune PID values over Bluetooth from a phone
            - Stop at the finish marker
Tech stack: Arduino Nano, QTR-8RC sensor array, TB6612FNG motor driver, HC-05 Bluetooth
```

---

## Example 59

**Intent:**
sumo robot

**Spec:**
```
Type:       IoT system (mini sumo robot)
Features:   - Wait 5 seconds after the start signal as the rules require
            - Find the opponent with infrared distance sensors
            - Detect the white ring edge with line sensors and back away
            - Push forward at full power when the opponent is in front
            - Switch between start strategies with a DIP switch
Tech stack: Arduino Pro Mini, Sharp GP2Y0A21 sensors, DRV8833 motor driver
```

---

## Example 60

**Intent:**
hospital wandering alert for dementia patients near the exit doors

**Spec:**
```
Type:       IoT system (patient wander alert)
Data model: Patient(id, name, ward, tag_id)
            Door(id, name, ward)
            Alert(id, patient_id -> Patient, door_id -> Door, raised_at, resolved_by, resolved_at)
Features:   - Detect a patient's BLE tag near a monitored exit door
            - Lock or hold the door for 15 seconds when an at-risk tag approaches
            - Send an alert to nurses' pagers and the ward screen
            - Let staff clear the alert with their badge
            - Log every alert for incident review
API:        REST
            GET  /alerts?open=true
            POST /alerts/{id}/resolve
Storage:    PostgreSQL
Tech stack: BLE tags, ESP32 door readers, MQTT, Node.js, React
```

---

## Example 61

**Intent:**
Bed exit sensor for my dad at night

**Spec:**
```
Type:       IoT system (bed exit alarm)
Features:   - Detect when weight leaves the bed with a pressure mat
            - Only alert between set night hours
            - Play a chime in my room and send a phone notification
            - Turn on a dim night light by the bed
            - Log the times he got up for the doctor
Storage:    SQLite
Tech stack: Raspberry Pi Zero, pressure mat sensor, Python, ntfy.sh
```

---

## Example 62

**Intent:**
medication fridge in pharmacy, need to log temps every 5 min and keep for 2 years, also need min max report daily

**Spec:**
```
Type:       IoT system (pharmacy fridge logging)
Data model: Fridge(id, name, location)
            Reading(id, fridge_id -> Fridge, temp_c, recorded_at)
            DailyReport(id, fridge_id -> Fridge, date, min_c, max_c, signed_by)
Features:   - Record temperature every 5 minutes for each fridge
            - Calculate daily minimum and maximum
            - Ask the pharmacist to sign off the daily report
            - Alert when a fridge is out of range for 15 minutes
            - Keep readings for two years and archive older data
Storage:    PostgreSQL
Tech stack: Python, Django, Wi-Fi temperature probes (SensorPush)
```

---

## Example 63

**Intent:**
hearing aid battery reminder

**Spec:**
```
Type:       Mobile application (battery reminder)
Data model: Device(id, side, battery_size, typical_days)
            BatteryChange(id, device_id -> Device, changed_at)
Features:   - Log each battery change for left and right hearing aids
            - Predict the next change from average life
            - Remind the user a day before
            - Show how many batteries are left in the current pack
Storage:    Local storage on the device
Tech stack: Flutter, local notifications plugin
```

---

## Example 64

**Intent:**
talking clock and calendar for a blind person, press one button

**Spec:**
```
Type:       IoT system (talking clock)
Features:   - Speak the time, date and weekday when the big button is pressed
            - Speak today's appointments from a shared Google Calendar
            - Hold the button to hear tomorrow's appointments
            - Adjust volume with a knob
            - Keep time with a battery-backed clock module
Tech stack: Raspberry Pi, Python, Google Calendar API, pyttsx3, DS3231 RTC
```

---

## Example 65

**Intent:**
Eye-gaze communication board for a child with cerebral palsy

**Spec:**
```
Type:       Desktop application (AAC communication board)
Data model: Board(id, name, rows, cols)
            Cell(id, board_id -> Board, position, label, image_path, phrase, link_board_id -> Board)
Features:   - Show a grid of picture symbols
            - Select a cell by looking at it for a set dwell time
            - Speak the phrase of the selected cell
            - Link cells to open sub-boards such as food or feelings
            - Let carers edit boards with their own photos
Storage:    Local SQLite
Tech stack: C#, WPF, Tobii eye tracker SDK, Windows text-to-speech
```

---

## Example 66

**Intent:**
Braille label maker for my pantry jars

**Spec:**
```
Type:       Desktop application (braille label maker)
Features:   - Type label text and preview it as Braille dots
            - Translate text to Grade 1 or Grade 2 Braille
            - Send the dots to an embosser
            - Save label templates for common items
            - Print a large-print version as well
Tech stack: Python, liblouis, Tkinter
```

---

## Example 67

**Intent:**
walkie talkie log for festival security radio channels

**Spec:**
```
Type:       Web application (radio incident log)
Data model: Channel(id, name)
            Callsign(id, name, team)
            LogEntry(id, channel_id -> Channel, callsign_id -> Callsign, message, priority, logged_at, closed_at)
Features:   - Log radio calls with time, callsign and channel
            - Mark entries as incidents with a priority
            - Track open incidents until closed
            - Search the log by callsign or keyword
            - Export the full log after the event
API:        REST
            POST /entries
            GET  /entries?open=true
            GET  /entries/export.csv
Storage:    PostgreSQL
Tech stack: Elixir, Phoenix LiveView
```

---

## Example 68

**Intent:**
cad system for small 911 center, take call, place incident on map, send units

**Spec:**
```
Type:       Web application (computer-aided dispatch)
Data model: Call(id, caller_phone, address, lat, lng, received_at)
            Incident(id, call_id -> Call, type, priority, status)
            Unit(id, call_sign, type, status, lat, lng)
            Assignment(id, incident_id -> Incident, unit_id -> Unit, dispatched_at, arrived_at)
Features:   - Create an incident from a call with geocoded address
            - Show incidents and unit positions on a live map
            - Suggest the nearest available unit by drive time
            - Track unit status from dispatched to on scene to clear
            - Record a timestamped audit log of all actions
API:        REST
            POST /incidents
            POST /incidents/{id}/assign
            PATCH /units/{id}/status
            GET  /map/state
Storage:    PostgreSQL with PostGIS
Tech stack: Java, Spring Boot, WebSockets, OpenLayers, OSRM
```

---

## Example 69

**Intent:**
lifeguard tower rotation and incident log for our beach

**Spec:**
```
Type:       Mobile application with backend (lifeguard operations)
Data model: Tower(id, name, beach_zone)
            Lifeguard(id, name, certs_expire_at)
            Rotation(id, tower_id -> Tower, lifeguard_id -> Lifeguard, starts_at, ends_at)
            Incident(id, tower_id -> Tower, type, description, occurred_at)
Features:   - Generate tower rotations every 30 minutes
            - Notify lifeguards of their next tower
            - Log rescues and first aid incidents with location
            - Record water and flag conditions each hour
            - Warn when a lifeguard's certification is expiring
API:        REST
            GET  /rotations/today
            POST /incidents
            POST /conditions
Storage:    PostgreSQL
Tech stack: React Native, Supabase
```

---

## Example 70

**Intent:**
search and rescue team callout and who is on which task

**Spec:**
```
Type:       Web application (search and rescue coordination)
Data model: Member(id, name, phone, skills)
            Mission(id, title, lat, lng, started_at)
            Team(id, mission_id -> Mission, name, leader_id -> Member)
            Task(id, team_id -> Team, area_geojson, status)
Features:   - Send a callout to all members and record their replies
            - Split responders into field teams
            - Draw search areas on a map and assign them to teams
            - Update task status and coverage from the field
            - Produce a mission summary with timings
API:        REST
            POST /missions
            POST /missions/{id}/callout
            POST /teams/{id}/tasks
Storage:    PostgreSQL with PostGIS
Tech stack: Python, Django, Leaflet, Twilio
```

---

## Example 71

**Intent:**
Avalanche transceiver practice timer

**Spec:**
```
Type:       Mobile application (avalanche drill timer)
Data model: Drill(id, scenario, burial_count, started_at)
            Find(id, drill_id -> Drill, beacon_no, found_seconds)
Features:   - Start a timer when the search begins
            - Record the time to each buried beacon
            - Compare drill times over the season
            - Share results with the club group
Storage:    Local storage on the device
Tech stack: Swift, SwiftUI
```

---

## Example 72

**Intent:**
marine VHF log book for our yacht club safety boat

**Spec:**
```
Type:       Mobile application (VHF radio log)
Data model: Entry(id, channel, station, message, logged_at, lat, lng)
Features:   - Log calls with channel, station and message
            - Add the GPS position automatically
            - Mark distress and urgency calls
            - Export the daily log as PDF
Storage:    Local SQLite
Tech stack: Flutter, geolocator plugin, pdf package
```

---

## Example 73

**Intent:**
Anchor drag alarm on my phone

**Spec:**
```
Type:       Mobile application (anchor alarm)
Features:   - Set the anchor position when the anchor is dropped
            - Set a swing radius in metres
            - Track the boat's GPS position in the background
            - Sound a loud alarm when the boat leaves the radius
            - Show the track around the anchor on a map
Tech stack: Kotlin, Android location services, Google Maps SDK
```

---

## Example 74

**Intent:**
marina berth booking system for visiting boats

**Spec:**
```
Type:       Web application (marina berth booking)
Data model: Pontoon(id, name)
            Berth(id, pontoon_id -> Pontoon, number, max_length_m, has_power)
            Boat(id, owner_id, name, length_m)
            Booking(id, berth_id -> Berth, boat_id -> Boat, arrives_on, departs_on, status)
Features:   - Show available berths that fit the boat length
            - Book and pay for nights online
            - Let harbour staff assign and change berths
            - Show arrivals and departures for today
            - Send arrival instructions by email
API:        REST
            GET  /berths/available?length={m}&from={d}&to={d}
            POST /bookings
            GET  /arrivals?date={d}
Storage:    PostgreSQL
Tech stack: PHP, Symfony, Stripe
```

---

## Example 75

**Intent:**
Want to track the tide gauge at our harbour and put the level online for fishermen

**Spec:**
```
Type:       IoT system (tide gauge)
Data model: Gauge(id, name, lat, lng)
            LevelReading(id, gauge_id -> Gauge, level_m, recorded_at)
Features:   - Measure water level with a radar sensor every minute
            - Average readings to remove wave noise
            - Upload levels to a server
            - Show the live level and the predicted tide curve on a web page
            - Alert subscribers when the level is above a storm threshold
API:        REST
            GET  /gauges/{id}/latest
            GET  /gauges/{id}/history?hours={n}
Storage:    PostgreSQL
Tech stack: Raspberry Pi, Maxbotix radar sensor, Python, FastAPI, Plotly
```

---

## Example 76

**Intent:**
airplane maintenance log for a flying club, track hours until next 100 hour inspection

**Spec:**
```
Type:       Web application (aircraft maintenance tracking)
Data model: Aircraft(id, registration, model, tach_hours)
            Flight(id, aircraft_id -> Aircraft, pilot_id, tach_start, tach_end, flown_on)
            Inspection(id, aircraft_id -> Aircraft, type, done_at_hours, done_on)
            Squawk(id, aircraft_id -> Aircraft, description, status)
Features:   - Log flights with tachometer start and end
            - Calculate hours left until the next 100-hour and annual inspection
            - Report squawks and track repairs
            - Ground an aircraft when an inspection is overdue
            - Email members when a plane is grounded or back in service
API:        REST
            POST /flights
            GET  /aircraft/{id}/due
            POST /squawks
Storage:    PostgreSQL
Tech stack: Ruby on Rails, PostgreSQL, Tailwind CSS
```

---

## Example 77

**Intent:**
weight and balance calculator for a Cessna 172

**Spec:**
```
Type:       Mobile application (weight and balance)
Data model: AircraftProfile(id, registration, empty_weight_kg, empty_arm_mm)
            Station(id, profile_id -> AircraftProfile, name, arm_mm, max_kg)
Features:   - Enter pilot, passenger, baggage and fuel weights
            - Calculate total weight and centre of gravity
            - Plot the result on the CG envelope
            - Warn when weight or CG is outside limits
            - Save profiles for several aircraft
Storage:    Local storage on the device
Tech stack: React Native, Victory charts
```

---

## Example 78

**Intent:**
glider club launch log at the airfield

**Spec:**
```
Type:       Mobile application with backend (glider launch log)
Data model: Glider(id, registration)
            Member(id, name)
            Launch(id, glider_id -> Glider, pilot_id -> Member, method, launched_at, landed_at, fee)
Features:   - Log each launch with glider, pilot and winch or tow
            - Record landing time to compute flight duration
            - Charge launch fees to member accounts
            - Show the day's launches on a board
            - Export to the club accounting system
API:        REST
            POST /launches
            PATCH /launches/{id}/land
            GET  /launches?date={d}
Storage:    PostgreSQL
Tech stack: Vue.js PWA, Python, FastAPI
```

---

## Example 79

**Intent:**
ship engine room checklist and rounds log

**Spec:**
```
Type:       Mobile application with backend (engine room rounds)
Data model: Vessel(id, name, imo)
            Round(id, vessel_id -> Vessel, engineer, started_at)
            RoundReading(id, round_id -> Round, point, value, unit, ok)
Features:   - Guide the engineer through each reading point in the engine room
            - Check readings against normal ranges
            - Work offline and sync when the ship has connectivity
            - Flag abnormal readings to the chief engineer
            - Keep the log for class society audits
API:        REST
            POST /rounds
            GET  /vessels/{id}/rounds?from={d}
Storage:    PostgreSQL, SQLite (on tablet)
Tech stack: Flutter, Django REST Framework
```

---

## Example 80

**Intent:**
library of ship stability calc

**Spec:**
```
Type:       Command-line tool (ship stability)
Features:   - Calculate displacement and draft from the loading condition
            - Calculate the metacentric height GM
            - Build a GZ righting arm curve
            - Check results against IMO intact stability criteria
            - Print a stability report
Tech stack: Python, NumPy, pandas, matplotlib
```

---

## Example 81

**Intent:**
lab glove box oxygen and moisture monitor

**Spec:**
```
Type:       IoT system (glove box monitoring)
Features:   - Read oxygen and moisture ppm from the glove box analyzer over RS-485
            - Log values every 30 seconds
            - Alert the lab group when oxygen rises above 1 ppm
            - Show a 24-hour trend on a wall screen
Storage:    InfluxDB
Tech stack: Raspberry Pi, Python, minimalmodbus, Grafana
```

---

## Example 82

**Intent:**
Kiln controller for pottery with firing schedules

**Spec:**
```
Type:       IoT system (kiln controller)
Data model: Schedule(id, name)
            Segment(id, schedule_id -> Schedule, position, rate_c_per_h, target_c, hold_min)
            Firing(id, schedule_id -> Schedule, started_at, ended_at, max_c)
Features:   - Read kiln temperature with a type K thermocouple
            - Follow firing schedule segments with ramp and hold
            - Control the elements through a solid state relay with PID
            - Show progress on a web page from the phone
            - Abort and alert if the kiln cannot keep up with the ramp
Storage:    SQLite
Tech stack: Raspberry Pi, MAX31856, Python, Flask
```

---

## Example 83

**Intent:**
can u make a sensor that tells me when the septic tank is getting full

**Spec:**
```
Type:       IoT system (septic tank level)
Features:   - Measure the tank level with an ultrasonic sensor through the lid
            - Send a reading every 6 hours over LoRaWAN
            - Estimate the date the tank will need pumping
            - Notify the owner when it reaches 80 percent
Tech stack: Dragino LDDS75 sensor, The Things Network, Node-RED
```

---

## Example 84

**Intent:**
rainwater tank level on my phone

**Spec:**
```
Type:       IoT system (rainwater tank level)
Features:   - Measure water depth with a submersible pressure sensor
            - Convert depth to litres using the tank shape
            - Send readings over Wi-Fi every 30 minutes
            - Show percentage full and daily usage on a phone dashboard
Tech stack: ESP32, ESPHome, Home Assistant mobile app
```

---

## Example 85

**Intent:**
Shed door left open alarm

**Spec:**
```
Type:       IoT system (door open alert)
Features:   - Detect the shed door state with a magnetic reed switch
            - Notify the phone if the door stays open more than 20 minutes
            - Notify again after dark
            - Run on a coin cell for a year
Tech stack: Zigbee door sensor, Zigbee2MQTT, Home Assistant
```

---

## Example 86

**Intent:**
lift station pump monitoring for our water utility, 25 remote sites

**Spec:**
```
Type:       IoT system (lift station SCADA)
Data model: Station(id, name, lat, lng)
            Pump(id, station_id -> Station, number)
            PumpRun(id, pump_id -> Pump, started_at, stopped_at, amps)
            WetWellLevel(id, station_id -> Station, level_m, recorded_at)
            Alarm(id, station_id -> Station, type, raised_at, acked_at)
Features:   - Poll PLCs at each station over cellular
            - Show wet well levels and pump states on an overview map
            - Raise high-level and pump-fail alarms
            - Call out the on-duty operator by phone until acknowledged
            - Report pump run hours for maintenance planning
API:        REST
            GET  /stations
            GET  /stations/{id}/trend
            POST /alarms/{id}/ack
Storage:    TimescaleDB
Tech stack: Python, Modbus TCP, FastAPI, React, Twilio Voice
```

---

## Example 87

**Intent:**
monitoring compressed air leaks in factory by measuring flow at night when machines off

**Spec:**
```
Type:       Data analysis script (compressed air leak analysis)
Features:   - Find periods when production is stopped
            - Calculate the base air flow during those periods as leakage
            - Estimate yearly energy cost of the leaks
            - Compare weeks to see if leak repairs helped
            - Produce a chart and summary table
Tech stack: Python, pandas, matplotlib
```

---

## Example 88

**Intent:**
injection molding cycle time monitor

**Spec:**
```
Type:       IoT system (molding cycle monitoring)
Data model: Press(id, name, target_cycle_s)
            Cycle(id, press_id -> Press, mold_id, duration_s, ended_at)
Features:   - Detect each mold open signal from the press
            - Record cycle duration per press
            - Alert when cycles are 10 percent slower than target
            - Count shots per mold for maintenance
            - Show presses on a shop-floor TV dashboard
Storage:    PostgreSQL
Tech stack: Siemens LOGO PLC, Node-RED, PostgreSQL, Grafana
```

---

## Example 89

**Intent:**
andon light system for our assembly line

**Spec:**
```
Type:       IoT system (andon system)
Data model: Station(id, name, line)
            AndonCall(id, station_id -> Station, type, called_at, responded_at, resolved_at)
Features:   - Let operators press buttons for material, quality or help
            - Light the station tower lamp in the matching colour
            - Show open calls on a large screen with waiting time
            - Notify the team leader's smartwatch
            - Report response times per shift
API:        REST
            POST /stations/{id}/calls
            PATCH /calls/{id}
            GET  /calls?open=true
Storage:    PostgreSQL
Tech stack: ESP32 button boxes, MQTT, Node.js, Vue.js
```

---

## Example 90

**Intent:**
morse code practice game

**Spec:**
```
Type:       Browser game (Morse code trainer)
Features:   - Play Morse characters as audio tones at an adjustable speed
            - Ask the player to type the character they heard
            - Add new characters as the player gets earlier ones right
            - Speed up when accuracy stays above 90 percent
            - Save progress and best speed between sessions
Storage:    Browser localStorage
Tech stack: TypeScript, Web Audio API, Vite
```

---

## Example 91

**Intent:**
telegram bot that tells me the battery state of my off grid cabin

**Spec:**
```
Type:       Bot (Telegram, off-grid cabin status)
Features:   - Read battery voltage and state of charge from the Victron charge controller
            - Reply to /status with battery, solar input and load
            - Send a warning when state of charge drops below 30 percent
            - Send a morning summary of yesterday's solar harvest
Storage:    SQLite
Tech stack: Python, python-telegram-bot, Victron VE.Direct, Raspberry Pi
```

---

## Example 92

**Intent:**
discord bot for our repeater club net check-ins

**Spec:**
```
Type:       Bot (Discord, radio net check-ins)
Data model: Net(id, name, started_at, net_control)
            CheckIn(id, net_id -> Net, callsign, location, checked_in_at)
Features:   - Start a net session with a command
            - Let members check in with their callsign
            - Post the running list of check-ins
            - Close the net and post a summary with the count
            - Show attendance statistics per member
Storage:    PostgreSQL
Tech stack: Python, discord.py, asyncpg
```

---

## Example 93

**Intent:**
power outage logger

**Spec:**
```
Type:       IoT system (power outage logging)
Data model: Outage(id, started_at, ended_at, duration_s)
Features:   - Detect mains power loss with a UPS-backed device
            - Record start and end time of each outage
            - Send a notification when power goes off and returns
            - Show outages per month in a chart
Storage:    SQLite
Tech stack: Raspberry Pi, NUT (Network UPS Tools), Python, Pushover
```

---

## Example 94

**Intent:**
Script that pulls my Tesla Powerwall stats into a spreadsheet every night

**Spec:**
```
Type:       Scheduled script (home battery export)
Features:   - Log in to the local Powerwall gateway API
            - Fetch yesterday's solar, battery, grid and home energy totals
            - Append a row to a Google Sheet
            - Retry when the gateway is unreachable
            - Email an error if three nights fail in a row
Tech stack: Python, requests, gspread, cron
```

---

## Example 95

**Intent:**
wind turbine data from our small community wind farm, show production vs wind speed

**Spec:**
```
Type:       Data dashboard (wind turbine performance)
Data model: Turbine(id, name, rated_kw)
            TurbineReading(id, turbine_id -> Turbine, wind_ms, power_kw, rotor_rpm, recorded_at)
Features:   - Import 10-minute SCADA data from each turbine
            - Plot the measured power curve against the manufacturer curve
            - Calculate monthly energy and capacity factor
            - Highlight periods of underperformance
            - Show each member's share of production
API:        REST
            GET  /turbines/{id}/power-curve
            GET  /production/monthly
Storage:    PostgreSQL
Tech stack: Python, Dash, Plotly, pandas
```

---

## Example 96

**Intent:**
bird feeder camera that identifies species

**Spec:**
```
Type:       IoT system (bird feeder camera)
Data model: Sighting(id, species, confidence, image_path, seen_at)
Features:   - Capture a photo when motion is detected at the feeder
            - Classify the bird species with an image model
            - Save sightings with photo and confidence
            - Show a daily list of visitors
            - Post rare species to a Mastodon account
Storage:    SQLite, local image folder
Tech stack: Raspberry Pi 5, Pi Camera Module 3, Python, TensorFlow Lite, BirdNET-style classifier
```

---

## Example 97

**Intent:**
Model that detects bearing faults from vibration recordings

**Spec:**
```
Type:       Machine learning model (bearing fault classification)
Features:   - Split recordings into fixed-length windows
            - Extract time-domain and FFT features
            - Train a gradient boosting classifier
            - Report accuracy and a confusion matrix per fault type
            - Export the model for use on an edge device
Tech stack: Python, scikit-learn, LightGBM, SciPy
```

---

## Example 98

**Intent:**
predict when our forklift batteries will need replacing

**Spec:**
```
Type:       Machine learning model (battery remaining life)
Features:   - Clean and join charger logs per battery
            - Engineer features such as capacity fade and depth of discharge
            - Train a regression model for remaining cycles
            - Rank batteries by predicted replacement date
            - Output a monthly replacement forecast
Tech stack: Python, pandas, XGBoost, Jupyter
```

---

## Example 99

**Intent:**
data pipeline from 200 cold-room sensors to our warehouse db

**Spec:**
```
Type:       Data pipeline (sensor ingestion)
Data model: SensorReading(sensor_id, site_id, temp_c, humidity_pct, recorded_at)
            HourlyAggregate(sensor_id, hour, min_c, max_c, avg_c)
Features:   - Subscribe to MQTT topics from all sensors
            - Validate and deduplicate readings
            - Write raw readings to a time-series table
            - Compute hourly aggregates every hour
            - Load aggregates into the company data warehouse nightly
Storage:    TimescaleDB, Snowflake
Tech stack: Python, paho-mqtt, Apache Airflow
```

---

## Example 100

**Intent:**
webhook that receives alerts from our server room temperature sensor and posts them to slack

**Spec:**
```
Type:       Webhook service (sensor alerts to Slack)
Features:   - Receive alert webhooks from the sensor cloud
            - Verify the shared secret on each request
            - Format the alert with room name, temperature and trend
            - Post it to the facilities Slack channel
            - Suppress duplicate alerts within 10 minutes
API:        REST
            POST /webhooks/sensor-alert
Storage:    Redis (deduplication)
Tech stack: Node.js, Express, Slack Incoming Webhooks
```

---

## Example 101

**Intent:**
Home Assistant plugin for my old heat pump that only has a serial port

**Spec:**
```
Type:       Plugin (Home Assistant integration)
Features:   - Talk to the heat pump over RS-232 through a USB adapter
            - Expose a climate entity with mode and target temperature
            - Expose sensors for outdoor temperature and compressor state
            - Poll the heat pump every 30 seconds
            - Configure the serial port from the UI
Tech stack: Python, Home Assistant custom component, pyserial
```

---

## Example 102

**Intent:**
OctoPrint style plugin but for my laser cutter, log job times

**Spec:**
```
Type:       Plugin (laser cutter job logging)
Data model: Job(id, filename, material, started_at, ended_at, power_pct)
Features:   - Hook into the job start and end events
            - Record job duration, material and power settings
            - Show total tube hours since the last tube change
            - Warn when the tube reaches its rated hours
Storage:    SQLite
Tech stack: Python, LightBurn log parsing, Flask
```

---

## Example 103

**Intent:**
Browser extension that shows the live price of electricity in the corner while I browse

**Spec:**
```
Type:       Browser extension (electricity price badge)
Features:   - Fetch the current hourly electricity price for the selected area
            - Show the price as a badge on the toolbar icon
            - Colour the badge green, amber or red by price level
            - Show the next 12 hours in the popup
            - Notify when the price drops below a set level
Tech stack: JavaScript, Chrome Extensions Manifest V3, ENTSO-E API
```

---

## Example 104

**Intent:**
cli to flash firmware to 50 esp32 boards at once

**Spec:**
```
Type:       Command-line tool (bulk firmware flashing)
Features:   - Detect all connected ESP32 boards
            - Flash firmware to several boards in parallel
            - Write a unique device ID to each board
            - Verify the flash and print a pass or fail table
            - Save a CSV of MAC addresses and device IDs
Tech stack: Python, esptool, concurrent.futures
```

---

## Example 105

**Intent:**
script that reads my car's OBD port and logs fuel economy

**Spec:**
```
Type:       Command-line script (OBD-II logger)
Features:   - Connect to the OBD-II adapter
            - Read speed, RPM and fuel rate every second
            - Calculate trip fuel economy
            - Save each trip to a CSV file
            - Print a summary when the engine stops
Tech stack: Python, python-OBD
```

---

## Example 106

**Intent:**
chatbot that answers questions about our ISO 9001 machine maintenance procedures

**Spec:**
```
Type:       Chatbot (maintenance procedures assistant)
Data model: Document(id, title, revision, uploaded_at)
            Chunk(id, document_id -> Document, text, embedding)
Features:   - Index maintenance procedures from PDF and Word files
            - Answer technician questions with the relevant procedure steps
            - Cite the document title and revision in every answer
            - Refuse to answer when no procedure matches
            - Re-index when a new revision is uploaded
API:        REST
            POST /chat
            POST /documents
Storage:    PostgreSQL with pgvector
Tech stack: Python, FastAPI, LangChain, OpenAI API
```

---

## Example 107

**Intent:**
sms chatbot for farmers to report dead livestock for collection

**Spec:**
```
Type:       Chatbot (SMS livestock collection)
Data model: Farm(id, phone, name, address)
            CollectionRequest(id, farm_id -> Farm, species, count, requested_at, collected_at)
Features:   - Guide the farmer through species, count and location by SMS
            - Create a collection request for the rendering company
            - Confirm the expected pickup day
            - Notify the farmer when the pickup is done
API:        REST
            POST /sms/incoming
            GET  /requests?status=open
Storage:    PostgreSQL
Tech stack: Python, Flask, Twilio Programmable SMS
```

---

## Example 108

**Intent:**
smart bin that tells the council when its full

**Spec:**
```
Type:       IoT system (waste bin fill level)
Data model: Bin(id, location, lat, lng, type)
            FillReading(id, bin_id -> Bin, fill_pct, recorded_at)
Features:   - Measure fill level with an ultrasonic sensor under the lid
            - Report fill level twice a day over NB-IoT
            - Show all bins on a map coloured by fill level
            - Plan a collection route for bins above 75 percent
            - Report fill trends per bin to resize collections
API:        REST
            GET  /bins?min_fill={n}
            GET  /routes/today
Storage:    PostgreSQL with PostGIS
Tech stack: NB-IoT sensor nodes, Python, FastAPI, Leaflet, OR-Tools
```

---

## Example 109

**Intent:**
Public toilet occupancy and cleaning tracker for a train station

**Spec:**
```
Type:       IoT system (restroom monitoring)
Data model: Restroom(id, name)
            Visit(id, restroom_id -> Restroom, counted_at)
            Cleaning(id, restroom_id -> Restroom, cleaner_id, cleaned_at)
Features:   - Count visitors with a door sensor
            - Request cleaning after a set number of visits
            - Let cleaners confirm with an NFC tag scan
            - Collect feedback with smiley buttons at the exit
            - Report cleaning frequency and feedback per restroom
Storage:    PostgreSQL
Tech stack: ESP32, NFC tags, MQTT, Django
```

---

## Example 110

**Intent:**
nfc patrol checkpoint app for security guards

**Spec:**
```
Type:       Mobile application with backend (guard patrol)
Data model: Site(id, name)
            Checkpoint(id, site_id -> Site, name, nfc_uid)
            Patrol(id, guard_id, site_id -> Site, started_at)
            Scan(id, patrol_id -> Patrol, checkpoint_id -> Checkpoint, scanned_at, note)
Features:   - Scan NFC checkpoints during a patrol
            - Attach notes and photos to a scan
            - Alert supervisors when a checkpoint is missed
            - Show patrol history per site
            - Export patrol reports for clients
API:        REST
            POST /patrols
            POST /patrols/{id}/scans
            GET  /sites/{id}/reports
Storage:    PostgreSQL
Tech stack: Kotlin, Android NFC, Spring Boot
```

---

## Example 111

**Intent:**
Track the temperature of our server closet and email IT if it gets hot

**Spec:**
```
Type:       Scheduled script (server room temperature)
Features:   - Read the temperature from a USB sensor every 5 minutes
            - Email IT when it passes 30 °C
            - Send a follow-up when it returns to normal
            - Append readings to a CSV log
Tech stack: Python, TEMPer USB sensor, smtplib, systemd timer
```

---

## Example 112

**Intent:**
Something for our carpenters shop: the dust collector should turn on by itself when any saw starts

**Spec:**
```
Type:       IoT system (dust collector automation)
Features:   - Sense current on each machine with a clamp sensor
            - Switch the dust collector on when any machine runs
            - Open the blast gate for the running machine
            - Keep the collector on for 10 seconds after the machine stops
            - Log machine run hours
Tech stack: Arduino Mega, ACS712 current sensors, servo blast gates, relay module
```

---

## Example 113

**Intent:**
freeze warning for my water pipes in the crawlspace

**Spec:**
```
Type:       IoT system (pipe freeze alert)
Features:   - Read the crawlspace temperature every 10 minutes
            - Turn on a heat tape relay below 2 °C
            - Send a phone alert below 0 °C
            - Show the minimum temperature of each night
Tech stack: Shelly Plus 1, Shelly H&T sensor, Shelly cloud scenes
```

---

## Example 114

**Intent:**
my fish tank at the office, need auto feeder that coworkers can trigger from teams

**Spec:**
```
Type:       IoT system (aquarium feeder)
Data model: Feeding(id, triggered_by, fed_at)
Features:   - Drop a portion of food with a servo-driven feeder
            - Trigger feeding from a Microsoft Teams command
            - Block extra feedings within 8 hours to avoid overfeeding
            - Post who fed the fish in the channel
Storage:    SQLite
Tech stack: ESP32, servo motor, Azure Bot Service, Node.js
```

---

## Example 115

**Intent:**
we run a vertical farm, need LED recipes per crop and to log yield per rack

**Spec:**
```
Type:       Web application (vertical farm management)
Data model: Crop(id, name, days_to_harvest)
            LightRecipe(id, crop_id -> Crop, photoperiod_h, red_pct, blue_pct, ppfd)
            Rack(id, code, tier_count)
            Planting(id, rack_id -> Rack, crop_id -> Crop, seeded_on, harvested_on, yield_g)
Features:   - Define light recipes per crop
            - Push the recipe to the rack LED drivers when a planting starts
            - Track plantings per rack from seeding to harvest
            - Record yield in grams per tray
            - Compare yield per kWh across recipes
API:        REST
            POST /plantings
            PUT  /racks/{id}/recipe
            GET  /reports/yield
Storage:    PostgreSQL
Tech stack: Python, Django, Modbus LED drivers, Chart.js
```

---

## Example 116

**Intent:**
mushroom grow room CO2 control

**Spec:**
```
Type:       IoT system (mushroom fruiting room)
Features:   - Read CO2, temperature and humidity in the fruiting room
            - Run the fresh air fan when CO2 goes over the setpoint
            - Run the ultrasonic fogger to keep humidity near 90 percent
            - Log values every minute
            - Alert if humidity stays low for an hour
Storage:    InfluxDB
Tech stack: ESP32, SCD30 sensor, ESPHome, Home Assistant
```

---

## Example 117

**Intent:**
maple syrup sap tank levels across the sugarbush

**Spec:**
```
Type:       IoT system (sap collection monitoring)
Data model: Tank(id, name, capacity_l)
            LevelReading(id, tank_id -> Tank, litres, recorded_at)
Features:   - Measure sap level in each collection tank
            - Send readings over LoRa to the sugarhouse
            - Estimate sap flow rate per tank
            - Notify when a tank is nearly full to send the truck
            - Track total sap collected per day
Storage:    SQLite
Tech stack: LoRa32 boards, ultrasonic sensors, Raspberry Pi gateway, Python, Grafana
```

---

## Example 118

**Intent:**
egg incubator with auto turning and humidity

**Spec:**
```
Type:       IoT system (egg incubator)
Features:   - Hold temperature at 37.5 °C with a PID-controlled heater
            - Turn the eggs every 3 hours with a motor
            - Stop turning 3 days before the hatch date
            - Keep humidity in range with a small fan and water tray
            - Show day count and readings on an LCD
Tech stack: Arduino Uno, DHT22 sensor, 16x2 LCD, Arduino C++
```

---

## Example 119

**Intent:**
goat milking parlor records each goat milk amount using ear tag

**Spec:**
```
Type:       IoT system (milking records)
Data model: Goat(id, name, rfid_tag, birth_date)
            Milking(id, goat_id -> Goat, litres, milked_at)
Features:   - Read the goat's RFID ear tag at the stall
            - Weigh the milk bucket before and after
            - Store the yield per goat per milking
            - Flag goats whose yield drops more than 20 percent
            - Export lactation curves per goat
Storage:    SQLite
Tech stack: Raspberry Pi, RDM6300 125 kHz reader, HX711 scale, Python
```

---

## Example 120

**Intent:**
track sheep on hill farm with gps collars

**Spec:**
```
Type:       IoT system (livestock GPS tracking)
Data model: Animal(id, tag, name, collar_id)
            Fix(id, animal_id -> Animal, lat, lng, recorded_at)
            Geofence(id, name, polygon)
Features:   - Report collar GPS positions every hour over LoRaWAN
            - Show the flock on a satellite map
            - Alert when an animal leaves the geofence
            - Alert when an animal has not moved for 6 hours
            - Show each animal's track for the last week
API:        REST
            GET  /animals
            GET  /animals/{id}/track?days=7
            POST /geofences
Storage:    PostgreSQL with PostGIS
Tech stack: LoRaWAN GPS collars, ChirpStack, Python, FastAPI, Mapbox GL JS
```

---

## Example 121

**Intent:**
smart dog door only for our dog not the neighbours cat

**Spec:**
```
Type:       IoT system (pet door)
Features:   - Read the dog's microchip or collar tag when it approaches
            - Unlock the flap only for registered pets
            - Lock at night on a curfew schedule
            - Log every entry and exit with time
            - Notify when the dog goes outside after curfew
Tech stack: ESP32, RFID reader, servo latch, Arduino C++, Blynk
```

---

## Example 122

**Intent:**
lost pet tracker tag

**Spec:**
```
Type:       Mobile application with backend (pet tracker)
Data model: Pet(id, owner_id, name, tag_id, photo_url)
            Location(id, pet_id -> Pet, lat, lng, recorded_at)
            SafeZone(id, pet_id -> Pet, lat, lng, radius_m)
Features:   - Pair a GPS tag with a pet profile
            - Show the pet's last location on a map
            - Alert the owner when the pet leaves a safe zone
            - Switch the tag to live tracking mode when lost
            - Share a lost pet page with neighbours
API:        REST
            POST /pets
            GET  /pets/{id}/location
            POST /pets/{id}/lost-mode
Storage:    PostgreSQL
Tech stack: Flutter, Go, LTE-M GPS tracker
```

---

## Example 123

**Intent:**
fridge door left open beeper for the lab

**Spec:**
```
Type:       IoT system (door alarm)
Features:   - Detect the fridge door open with a magnet switch
            - Beep after 60 seconds open
            - Flash an LED during the alarm
            - Count door openings per day
Tech stack: ATtiny85, reed switch, piezo buzzer, Arduino C++
```

---

## Example 124

**Intent:**
Detect when my washing machine is done and ping me

**Spec:**
```
Type:       IoT system (appliance cycle notifier)
Features:   - Measure power use with a smart plug
            - Detect the end of a cycle when power stays low for 3 minutes
            - Send a phone notification
            - Remind again after 30 minutes if the door was not opened
Tech stack: Shelly Plug S, Home Assistant automations
```

---

## Example 125

**Intent:**
solar powered irrigation pump in my field in Kenya, want to turn it on from phone via sms because no internet there

**Spec:**
```
Type:       IoT system (SMS pump control)
Data model: Command(id, from_phone, text, received_at)
            PumpRun(id, started_at, stopped_at)
Features:   - Receive SMS commands like ON 30 or STATUS
            - Accept commands only from registered phone numbers
            - Switch the pump relay on for the requested minutes
            - Reply with pump state and battery voltage
            - Stop the pump if the well level sensor reads dry
Tech stack: Arduino, SIM800L GSM module, relay, float switch
```

---

## Example 126

**Intent:**
EV charger sharing in our apartment garage, 2 chargers 12 cars

**Spec:**
```
Type:       Web application (shared EV charger booking)
Data model: Charger(id, name, power_kw)
            Resident(id, name, unit, plate)
            Slot(id, charger_id -> Charger, resident_id -> Resident, starts_at, ends_at)
            Session(id, slot_id -> Slot, kwh, cost)
Features:   - Book a charging slot on a charger
            - Limit each resident to a weekly number of hours
            - Read energy per session from the chargers over OCPP
            - Bill residents monthly for their kWh
            - Notify the next resident when the charger becomes free
API:        REST
            GET  /chargers/{id}/slots
            POST /slots
            GET  /residents/{id}/bills
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, OCPP 1.6J, React
```

---

## Example 127

**Intent:**
ev charge point map for our small town

**Spec:**
```
Type:       Web application (charge point map)
Data model: ChargePoint(id, name, lat, lng, connector_types, power_kw, status)
Features:   - Show charge points on a map
            - Filter by connector type and power
            - Show live status from the operator's OCPI feed
            - Let admins add and edit points
API:        REST
            GET  /charge-points?connector={type}
            POST /charge-points
Storage:    PostgreSQL
Tech stack: Next.js, Leaflet, OCPI 2.2
```

---

## Example 128

**Intent:**
Ebike battery charge cycle counter

**Spec:**
```
Type:       IoT system (e-bike battery logging)
Features:   - Measure charge current with a shunt on the charger lead
            - Count full equivalent charge cycles
            - Track energy put in per charge
            - Show cycles and estimated capacity on a BLE phone app
Tech stack: Arduino Nano 33 BLE, INA226 current sensor, MIT App Inventor
```

---

## Example 129

**Intent:**
race timing with rfid chips for our local 10k

**Spec:**
```
Type:       Web application (race timing)
Data model: Race(id, name, date, distance_km)
            Runner(id, race_id -> Race, bib, name, category, chip_uid)
            ChipRead(id, chip_uid, reader_point, read_at)
            Result(id, runner_id -> Runner, gun_time_s, chip_time_s, place)
Features:   - Import runners and chip assignments from a CSV
            - Receive chip reads from start and finish mats
            - Calculate gun time and chip time
            - Rank runners overall and by category
            - Publish live results on a public page
API:        REST
            POST /reads
            GET  /races/{id}/results?category={c}
Storage:    PostgreSQL
Tech stack: Impinj UHF RFID reader, Python, FastAPI, Svelte
```

---

## Example 130

**Intent:**
swimming pool chlorine and ph auto dosing for our hotel pool

**Spec:**
```
Type:       IoT system (pool chemistry control)
Data model: Reading(id, ph, orp_mv, free_chlorine_ppm, temp_c, recorded_at)
            Dose(id, chemical, ml, dosed_at)
Features:   - Measure pH and ORP continuously
            - Dose acid or chlorine with peristaltic pumps to hold setpoints
            - Stop dosing when the circulation pump is off
            - Log readings for the health department
            - Alert the maintenance team on out-of-range values
Storage:    SQLite
Tech stack: Raspberry Pi, Atlas Scientific EZO circuits, Python, Grafana
```

---

## Example 131

**Intent:**
Sauna heater remote start from phone

**Spec:**
```
Type:       IoT system (sauna remote control)
Features:   - Switch the heater contactor on from a phone app
            - Show current sauna temperature
            - Turn off automatically after 3 hours for safety
            - Refuse to start if the door sensor shows the door open
            - Notify when the sauna reaches target temperature
Tech stack: Shelly Pro 3, temperature probe, Home Assistant
```

---

## Example 132

**Intent:**
climbing gym route setter app, track which routes are up, grades and when to strip them

**Spec:**
```
Type:       Web application (climbing route management)
Data model: Wall(id, name, section)
            Route(id, wall_id -> Wall, grade, colour, setter, set_on, stripped_on)
            Rating(id, route_id -> Route, climber_grade, stars)
Features:   - Add routes to walls with grade, colour and setter
            - Show the current routes per wall
            - Let climbers suggest a grade and rate routes
            - Suggest routes to strip by age and rating
            - Show the grade distribution per wall
API:        REST
            GET  /walls/{id}/routes
            POST /routes
            POST /routes/{id}/ratings
Storage:    PostgreSQL
Tech stack: Python, Flask, SQLAlchemy, Alpine.js
```

---

## Example 133

**Intent:**
lap timer for rc cars on our backyard track

**Spec:**
```
Type:       IoT system (RC lap timer)
Data model: Car(id, name, transponder_id)
            Lap(id, car_id -> Car, lap_no, time_ms, crossed_at)
Features:   - Detect car transponders crossing the start line with an IR receiver
            - Record lap times per car
            - Announce lap times by voice
            - Show a live leaderboard on a laptop
            - Save the best lap per car
Storage:    SQLite
Tech stack: Arduino, IR transponders, Python, Pygame
```

---

## Example 134

**Intent:**
fpv drone race gates timing using rssi

**Spec:**
```
Type:       IoT system (FPV race timing)
Features:   - Measure video transmitter RSSI for each pilot frequency at the gate
            - Detect a gate pass at the RSSI peak
            - Calculate lap times per pilot
            - Run heats with a countdown and buzzer
            - Show results on a web page for spectators
Storage:    SQLite
Tech stack: RotorHazard, Raspberry Pi, RX5808 receiver modules
```

---

## Example 135

**Intent:**
model rocket altimeter that records max height

**Spec:**
```
Type:       IoT system (rocket flight computer)
Features:   - Record barometric altitude 50 times per second
            - Detect launch, apogee and landing
            - Store the flight to flash memory
            - Beep out the max altitude after landing
            - Download the flight log over USB as CSV
Tech stack: Arduino Nano, BMP390 sensor, SPI flash, Arduino C++
```

---

## Example 136

**Intent:**
ground station for our university cubesat

**Spec:**
```
Type:       Desktop application (satellite ground station)
Data model: Pass(id, aos_at, los_at, max_elevation)
            Packet(id, pass_id -> Pass, raw_hex, decoded_json, received_at)
            Command(id, name, sent_at, acked)
Features:   - Schedule passes and steer the antenna rotator
            - Demodulate downlink telemetry with an SDR
            - Decode telemetry packets into readable values
            - Send uplink commands and track acknowledgements
            - Plot battery and temperature telemetry over time
Storage:    SQLite
Tech stack: Python, GNU Radio, Hamlib, PyQt5, SatNOGS client
```

---

## Example 137

**Intent:**
diy seismometer network across our schools that sends quakes to a map

**Spec:**
```
Type:       IoT system (school seismometer network)
Data model: Station(id, school, lat, lng)
            Trigger(id, station_id -> Station, peak_accel_g, triggered_at)
            Event(id, detected_at, est_lat, est_lng, station_count)
Features:   - Record ground motion at 100 samples per second at each school
            - Detect a trigger with an STA/LTA algorithm
            - Group triggers from several stations into one event
            - Show events on a public map
            - Let students download the waveform data
API:        REST
            GET  /events
            GET  /stations/{id}/waveforms?from={t}&to={t}
Storage:    PostgreSQL, MinIO (waveforms)
Tech stack: Raspberry Shake, ObsPy, Python, FastAPI, Leaflet
```

---

## Example 138

**Intent:**
geiger counter that uploads radiation readings

**Spec:**
```
Type:       IoT system (radiation monitoring)
Features:   - Count Geiger tube pulses per minute
            - Convert counts to microsieverts per hour
            - Upload readings to a public map every 5 minutes
            - Alert when the level is three times the local average
Tech stack: ESP32, GMC tube module, Arduino C++, Safecast API
```

---

## Example 139

**Intent:**
wildlife camera trap photo sorter

**Spec:**
```
Type:       Data analysis script (camera trap sorting)
Features:   - Detect animals, people and empty frames with MegaDetector
            - Move empty frames to a separate folder
            - Group images into events by time
            - Write a CSV of species detections per camera
            - Summarise detections by hour of day
Tech stack: Python, MegaDetector, PyTorch, pandas
```

---

## Example 140

**Intent:**
bat detector that records the ultrasonic calls at night

**Spec:**
```
Type:       IoT system (bat acoustic monitoring)
Features:   - Record ultrasound at 384 kHz from dusk to dawn
            - Save only clips that contain bat call energy
            - Timestamp clips with GPS time
            - Run a species classifier on the clips
            - Summarise passes per night and species
Storage:    SD card (WAV files)
Tech stack: AudioMoth, Python, BatDetect2
```

---

## Example 141

**Intent:**
river level gauge for our village flood warning

**Spec:**
```
Type:       IoT system (flood warning)
Data model: Gauge(id, river, lat, lng, warning_m, danger_m)
            Level(id, gauge_id -> Gauge, level_m, recorded_at)
            Subscriber(id, phone, gauge_id -> Gauge)
Features:   - Measure river level every 5 minutes with a radar sensor
            - Calculate the rate of rise
            - Send SMS warnings to subscribers at warning and danger levels
            - Show the level and trend on a public web page
            - Keep working on solar and battery during storms
API:        REST
            GET  /gauges/{id}/levels
            POST /subscribers
Storage:    PostgreSQL
Tech stack: Arduino MKR NB 1500, radar level sensor, Python, Django, Twilio
```

---

## Example 142

**Intent:**
grain bin temperature cables, warn if grain starts heating

**Spec:**
```
Type:       IoT system (grain bin monitoring)
Data model: Bin(id, name, crop, capacity_t)
            Cable(id, bin_id -> Bin, position)
            SensorPoint(id, cable_id -> Cable, depth_m)
            Reading(id, point_id -> SensorPoint, temp_c, recorded_at)
Features:   - Read temperature at each depth on every cable
            - Detect hot spots that rise more than 3 °C in a week
            - Turn on aeration fans when outside air is cool and dry
            - Alert the farmer with the bin and depth
            - Show a heat map per bin
Storage:    InfluxDB
Tech stack: DS18B20 sensor chains, ESP32, MQTT, Grafana
```

---

## Example 143

**Intent:**
cheese aging cave humidity and wheel tracking

**Spec:**
```
Type:       Web application (cheese aging)
Data model: Wheel(id, batch, type, made_on, weight_kg)
            Shelf(id, code)
            Placement(id, wheel_id -> Wheel, shelf_id -> Shelf, placed_on)
            Task(id, wheel_id -> Wheel, type, due_on, done_on)
            CaveReading(id, temp_c, humidity_pct, recorded_at)
Features:   - Label wheels with QR codes and track their shelf
            - Schedule turning, brushing and washing tasks
            - Record cave temperature and humidity from a sensor
            - Weigh wheels to follow moisture loss
            - Mark wheels ready by age
API:        REST
            GET  /tasks/today
            POST /wheels/{id}/tasks/{task}/done
            GET  /cave/readings
Storage:    PostgreSQL
Tech stack: Python, Django, ESP32 sensor, QR labels
```

---

## Example 144

**Intent:**
brewery fermenter dashboard, we have 8 tanks with glycol cooling

**Spec:**
```
Type:       IoT system (fermenter control)
Data model: Tank(id, name, volume_hl)
            Brew(id, tank_id -> Tank, recipe, brewed_on)
            Setpoint(id, brew_id -> Brew, temp_c, from_day)
            Reading(id, tank_id -> Tank, temp_c, gravity, recorded_at)
Features:   - Read tank temperatures and open the glycol valve to hold setpoints
            - Follow a temperature profile per brew such as diacetyl rest
            - Log gravity from a floating hydrometer
            - Show all tanks on one dashboard
            - Alert when a tank cannot reach its setpoint
API:        REST
            GET  /tanks
            PUT  /brews/{id}/profile
Storage:    PostgreSQL
Tech stack: Raspberry Pi, CraftBeerPi, Python, iSpindel
```

---

## Example 145

**Intent:**
bakery proofing cabinet control

**Spec:**
```
Type:       IoT system (dough proofer)
Features:   - Hold proofing temperature and humidity at setpoints
            - Run overnight retard programs that warm up before morning
            - Show the time remaining on a display
            - Notify the baker when dough is ready
Tech stack: ESP32, SHT40 sensor, Arduino C++, ntfy
```

---

## Example 146

**Intent:**
pizza oven thermometer app

**Spec:**
```
Type:       Mobile application (oven thermometer)
Features:   - Connect to an infrared or probe thermometer over Bluetooth
            - Show floor and dome temperature live
            - Alert when the oven reaches baking temperature
            - Track bake timers per pizza
Tech stack: Swift, Core Bluetooth, SwiftUI
```

---

## Example 147

**Intent:**
office coffee machine tells slack when fresh pot is ready

**Spec:**
```
Type:       IoT system (coffee pot notifier)
Features:   - Detect brewing by power draw on a smart plug
            - Post a message to Slack when brewing finishes
            - Post a warning when the pot has been sitting for 2 hours
            - Count pots brewed per week
Tech stack: TP-Link Kasa smart plug, Python, python-kasa, Slack API
```

---

## Example 148

**Intent:**
vending machine stock levels and sales sent to me, I own 15 machines

**Spec:**
```
Type:       IoT system (vending telemetry)
Data model: Machine(id, location, model)
            Slot(id, machine_id -> Machine, code, product, capacity, stock)
            Sale(id, slot_id -> Slot, price, sold_at)
Features:   - Read sales from each machine via the MDB/DEX interface
            - Update stock per slot after each sale
            - Show machines that need a refill on a dashboard
            - Generate a picking list for the refill route
            - Report revenue per machine and product
API:        REST
            GET  /machines
            GET  /refill-list
            GET  /reports/sales?month={m}
Storage:    PostgreSQL
Tech stack: Cellular DEX reader, Python, FastAPI, React
```

---

## Example 149

**Intent:**
laundromat app shows which washers are free

**Spec:**
```
Type:       Web application (laundromat machine status)
Data model: Machine(id, number, type, status, cycle_ends_at)
Features:   - Detect machine status with current sensors
            - Show free and busy washers and dryers
            - Show minutes remaining on each busy machine
            - Let customers subscribe to a notification when a machine frees up
API:        REST
            GET  /machines
            POST /machines/{id}/notify
Storage:    Redis
Tech stack: ESP32 current sensors, MQTT, Node.js, Web Push
```

---

## Example 150

**Intent:**
car wash bay usage and coin box counts

**Spec:**
```
Type:       IoT system (car wash monitoring)
Data model: Bay(id, number)
            WashSession(id, bay_id -> Bay, program, minutes, paid, started_at)
            CoinCount(id, bay_id -> Bay, total, counted_at)
Features:   - Log each wash session with program and minutes
            - Count coins and card payments per bay
            - Detect a bay out of order when no sessions happen in a busy hour
            - Show revenue per bay per day
            - Alert when soap or wax tanks are low
Storage:    PostgreSQL
Tech stack: PLC with Modbus TCP, Python, Grafana
```

---

## Example 151

**Intent:**
Model train layout controller from my laptop

**Spec:**
```
Type:       Desktop application (model railway control)
Data model: Loco(id, name, dcc_address)
            Turnout(id, name, address, state)
            Route(id, name, turnout_states)
Features:   - Control locomotive speed and direction over DCC
            - Switch turnouts by clicking a track diagram
            - Set whole routes with one click
            - Detect occupied blocks and show them on the diagram
            - Run simple automatic shuttle trains
Storage:    JSON configuration files
Tech stack: Python, DCC++ EX command station, PySide6
```

---

## Example 152

**Intent:**
escape room puzzle controller with locks sensors and a game master screen

**Spec:**
```
Type:       IoT system (escape room control)
Data model: Room(id, name)
            Puzzle(id, room_id -> Room, name, order)
            Game(id, room_id -> Room, team_name, started_at, ended_at)
            PuzzleSolve(id, game_id -> Game, puzzle_id -> Puzzle, solved_at)
Features:   - Read puzzle sensors such as RFID props and switches
            - Open maglocks when a puzzle is solved
            - Show puzzle progress and the game clock to the game master
            - Let the game master send hints to a room screen
            - Override and reset props between games
API:        REST
            POST /games
            POST /puzzles/{id}/solve
            POST /rooms/{id}/hint
Storage:    SQLite
Tech stack: ESP32 props, MQTT, Node-RED, Raspberry Pi
```

---

## Example 153

**Intent:**
theatre cue light system for stage manager

**Spec:**
```
Type:       IoT system (stage cue lights)
Features:   - Let the stage manager set standby and go on each cue station
            - Light a cue lamp at each operator position
            - Let operators acknowledge standby with a button
            - Show acknowledgement status on the stage manager panel
Tech stack: Arduino, RS-485 bus, Arduino C++
```

---

## Example 154

**Intent:**
church bell ringing schedule

**Spec:**
```
Type:       IoT system (bell ringing controller)
Data model: RingPattern(id, name, sequence)
            Schedule(id, pattern_id -> RingPattern, weekday, time)
            SpecialDate(date, pattern_id -> RingPattern)
Features:   - Ring bells on a weekly schedule
            - Use different patterns for Sunday service, weddings and funerals
            - Mute at night
            - Allow the sexton to ring manually from a phone
            - Keep time from GPS
Tech stack: Raspberry Pi, relays, Python, Flask
```

---

## Example 155

**Intent:**
observatory dome that rotates with the telescope

**Spec:**
```
Type:       IoT system (observatory dome control)
Features:   - Read the telescope pointing from the mount over ASCOM
            - Rotate the dome to keep the slit aligned
            - Open and close the shutter
            - Close the shutter when the rain sensor triggers
            - Expose the dome as an ASCOM device for imaging software
Tech stack: Arduino, stepper motor, ASCOM Alpaca, C#
```

---

## Example 156

**Intent:**
telescope astrophotography session logger

**Spec:**
```
Type:       Desktop application (imaging log)
Data model: Target(id, name, ra, dec)
            Session(id, date, location, seeing)
            Sub(id, session_id -> Session, target_id -> Target, filter, exposure_s, hfr, accepted)
Features:   - Read FITS headers from a night's images
            - Group subs by target and filter
            - Reject subs with high star size (HFR)
            - Total integration time per target
            - Export a list of accepted files for stacking
Storage:    SQLite
Tech stack: Python, Astropy, Tkinter
```

---

## Example 157

**Intent:**
hey i need a bot which give me alert when aurora is maybe visible on my place

**Spec:**
```
Type:       Bot (aurora alert)
Features:   - Fetch the Kp index forecast every 30 minutes
            - Check the local cloud forecast for the user location
            - Send a Telegram alert when Kp is high and skies are clear
            - Avoid sending more than one alert per night
Storage:    SQLite
Tech stack: Python, NOAA SWPC API, Open-Meteo API, python-telegram-bot
```

---

## Example 158

**Intent:**
ski lift queue camera estimates wait time

**Spec:**
```
Type:       IoT system (lift queue estimation)
Data model: Lift(id, name, capacity_per_hour)
            QueueEstimate(id, lift_id -> Lift, people, wait_min, estimated_at)
Features:   - Count people in the queue area from a camera image
            - Estimate wait time from queue size and lift capacity
            - Update estimates every minute
            - Show wait times on the resort app and screens
API:        REST
            GET  /lifts/wait-times
Storage:    Redis
Tech stack: NVIDIA Jetson Nano, YOLOv8, Python, FastAPI
```

---

## Example 159

**Intent:**
Snow depth sensor for our mountain hut

**Spec:**
```
Type:       IoT system (snow depth station)
Features:   - Measure snow depth with an ultrasonic sensor on a mast
            - Correct for air temperature
            - Send readings once an hour by satellite
            - Show a season chart on a website
Tech stack: Arduino, MaxBotix MB7374, RockBLOCK Iridium modem, Python
```

---

## Example 160

**Intent:**
ocean buoy temperature wave data

**Spec:**
```
Type:       IoT system (data buoy)
Data model: Buoy(id, name, lat, lng)
            Observation(id, buoy_id -> Buoy, water_temp_c, wave_height_m, wave_period_s, recorded_at)
Features:   - Measure sea surface temperature and wave motion with an IMU
            - Calculate significant wave height every 30 minutes
            - Send observations over Iridium satellite
            - Report buoy GPS position to detect drifting
            - Publish observations on a web page for surfers
API:        REST
            GET  /buoys/{id}/observations
Storage:    PostgreSQL
Tech stack: Teensy 4.1, BNO085 IMU, RockBLOCK, Python, FastAPI
```

---

## Example 161

**Intent:**
fish counter at the fish ladder

**Spec:**
```
Type:       IoT system (fish passage counter)
Data model: Passage(id, direction, length_cm, species, passed_at, image_path)
Features:   - Capture images when a fish passes the viewing window
            - Estimate fish length from the image
            - Classify species with a trained model
            - Count upstream and downstream passages
            - Report daily counts to the river trust
Storage:    PostgreSQL, image storage
Tech stack: Raspberry Pi 5, camera, Python, PyTorch
```

---

## Example 162

**Intent:**
mouse trap that tells me when it caught something

**Spec:**
```
Type:       IoT system (trap notification)
Data model: Trap(id, location, battery_pct)
            TrapEvent(id, trap_id -> Trap, triggered_at, cleared_at)
Features:   - Detect the trap triggering with a switch
            - Send a notification naming the trap location
            - Remind every 12 hours until the trap is cleared
            - Report battery level daily
Tech stack: ESP8266, deep sleep, MQTT, Home Assistant
```

---

## Example 163

**Intent:**
pest control company bait station inspections with barcode

**Spec:**
```
Type:       Mobile application with backend (pest control inspections)
Data model: Client(id, name, address)
            Station(id, client_id -> Client, barcode, type, location_note)
            Inspection(id, station_id -> Station, activity_level, bait_replaced, photo_url, inspected_at)
Features:   - Scan each bait station barcode on site
            - Record activity level and bait replacement
            - Add photos to inspections
            - Generate a service report for the client
            - Show trends of rodent activity per site
API:        REST
            POST /inspections
            GET  /clients/{id}/report?visit={id}
Storage:    PostgreSQL
Tech stack: Flutter, mobile_scanner, Node.js, PostgreSQL
```

---

## Example 164

**Intent:**
I want bot that say me when my balcony solar is make more than 600 watt, the inverter have local api

**Spec:**
```
Type:       Bot (balcony solar alerts)
Features:   - Poll the micro-inverter's local API every minute
            - Detect output above 600 watts
            - Send a Telegram message with the current power
            - Send a daily summary of produced kWh
Tech stack: Python, requests, python-telegram-bot, OpenDTU API
```

---

## Example 165

**Intent:**
court hearing reminders by text

**Spec:**
```
Type:       Scheduled script (court date reminders)
Data model: Defendant(id, name, phone, language)
            Hearing(id, defendant_id -> Defendant, case_no, courtroom, starts_at)
            Reminder(id, hearing_id -> Hearing, sent_at, kind)
Features:   - Import upcoming hearings from the court's daily CSV export
            - Send SMS reminders 7 days, 1 day and 2 hours before
            - Send messages in the defendant's preferred language
            - Include the courtroom, address and a map link
            - Log delivery status for each reminder
Storage:    PostgreSQL
Tech stack: Python, Twilio, cron
```

---

## Example 166

**Intent:**
book court interpreters for hearings

**Spec:**
```
Type:       Web application (interpreter scheduling)
Data model: Interpreter(id, name, languages, certified)
            Hearing(id, case_no, courtroom, starts_at, language)
            Assignment(id, hearing_id -> Hearing, interpreter_id -> Interpreter, status)
Features:   - Request an interpreter for a hearing by language
            - Offer the job to certified interpreters first
            - Let interpreters accept or decline from email
            - Prevent double booking across courthouses
            - Track hours for interpreter payments
API:        REST
            POST /hearings/{id}/requests
            POST /assignments/{id}/accept
            GET  /interpreters/{id}/hours
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Blazor
```

---

## Example 167

**Intent:**
probation officers need check-in kiosk where clients scan face or id and answer questions

**Spec:**
```
Type:       Web application (probation check-in)
Data model: Client(id, name, id_no, officer_id)
            CheckIn(id, client_id -> Client, answers_json, address_changed, checked_in_at)
            Flag(id, checkin_id -> CheckIn, reason)
Features:   - Identify the client by scanning an ID card
            - Ask the standard check-in questions on a touchscreen
            - Flag answers like a new arrest or address change
            - Notify the officer of flagged check-ins
            - Show each client's check-in history
API:        REST
            POST /checkins
            GET  /officers/{id}/flags
Storage:    PostgreSQL
Tech stack: React, Node.js, NestJS
```

---

## Example 168

**Intent:**
tenant hotline log for our housing rights group, volunteers answer calls

**Spec:**
```
Type:       Web application (hotline call log)
Data model: Call(id, volunteer_id, caller_area, issue_type, summary, needs_followup, called_at)
            Followup(id, call_id -> Call, assigned_to, done_at)
Features:   - Log calls with issue type such as eviction, repairs or deposit
            - Mark calls that need a follow-up and assign them
            - Search past calls by address or landlord
            - Show monthly counts per issue type for campaigns
            - Protect caller details with limited access
API:        REST
            POST /calls
            GET  /followups?mine=true
            GET  /stats/issues
Storage:    PostgreSQL
Tech stack: Python, Flask, Bootstrap
```

---

## Example 169

**Intent:**
Eviction notice answer form generator

**Spec:**
```
Type:       Web application (court form assistant)
Data model: Session(id, answers_json, created_at)
            GeneratedForm(id, session_id -> Session, form_code, pdf_path)
Features:   - Ask tenants plain-language questions about their notice
            - Choose the right answer form for the state
            - Fill the official PDF form with their answers
            - Explain filing deadlines and where to file
            - Let them download or email the filled form
API:        REST
            POST /sessions
            POST /sessions/{id}/generate
Storage:    SQLite, file storage for PDFs
Tech stack: Docassemble, Python
```

---

## Example 170

**Intent:**
Small claims tracker for my cases as self rep

**Spec:**
```
Type:       Mobile application (small claims tracker)
Data model: Case(id, court, case_no, defendant, amount, status)
            Deadline(id, case_id -> Case, title, due_on)
            Document(id, case_id -> Case, name, file_path)
Features:   - Track each case and its status
            - Add deadlines and get reminders
            - Store photos of receipts and letters
            - Show a timeline of each case
Storage:    Local storage on the device
Tech stack: React Native, Expo, expo-notifications
```

---

## Example 171

**Intent:**
notary appointment booking

**Spec:**
```
Type:       Web application (notary booking)
Data model: Service(id, name, duration_min, fee)
            Appointment(id, service_id -> Service, customer_name, email, starts_at, id_type, status)
Features:   - Show available time slots per service
            - Book and pay a deposit online
            - Ask what ID the customer will bring
            - Send reminders with the documents to bring
            - Let the notary block holidays
API:        REST
            GET  /slots?service={id}&date={d}
            POST /appointments
Storage:    MySQL
Tech stack: PHP, Laravel, Stripe
```

---

## Example 172

**Intent:**
Funeral home arrangements tracker

**Spec:**
```
Type:       Web application (funeral arrangements)
Data model: Deceased(id, full_name, date_of_death)
            Arrangement(id, deceased_id -> Deceased, service_type, service_at, venue, status)
            Task(id, arrangement_id -> Arrangement, title, due_at, done)
            FamilyContact(id, deceased_id -> Deceased, name, phone, relation)
Features:   - Create an arrangement with the service type and date
            - Generate a task checklist such as permits, flowers and obituary
            - Track payments and options chosen
            - Share a private page with the family
            - Show the week's services on a calendar
API:        REST
            POST /arrangements
            GET  /arrangements/{id}/tasks
            GET  /calendar?week={w}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stimulus
```

---

## Example 173

**Intent:**
grave photo app volunteers walk the cemetery and photograph headstones, gps auto

**Spec:**
```
Type:       Mobile application with backend (headstone photo survey)
Data model: Cemetery(id, name, lat, lng)
            Headstone(id, cemetery_id -> Cemetery, lat, lng, photo_url, transcribed_text, volunteer_id)
Features:   - Take headstone photos with automatic GPS position
            - Upload photos when back on Wi-Fi
            - Run OCR to suggest the transcription
            - Let volunteers correct names and dates
            - Show surveyed and unsurveyed areas on a map
API:        REST
            POST /headstones
            PATCH /headstones/{id}
            GET  /cemeteries/{id}/coverage
Storage:    PostgreSQL, S3
Tech stack: Flutter, Google ML Kit text recognition, Django
```

---

## Example 174

**Intent:**
cemetery groundskeeping work orders

**Spec:**
```
Type:       Web application (cemetery maintenance)
Data model: Plot(id, section, row, number)
            WorkOrder(id, plot_id -> Plot, type, requested_by, status, due_on)
            Crew(id, name)
Features:   - Create work orders for mowing, leveling and headstone repair
            - Link orders to plots on the cemetery map
            - Assign orders to crews
            - Mark work done with a photo
            - Notify families who requested the work
API:        REST
            POST /work-orders
            PATCH /work-orders/{id}
            GET  /crews/{id}/orders
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Vue.js, Leaflet
```

---

## Example 175

**Intent:**
blood donation van schedule and donor reminders

**Spec:**
```
Type:       Web application (blood drive scheduling)
Data model: Drive(id, location, date, capacity)
            Donor(id, name, blood_type, last_donation_on)
            Appointment(id, drive_id -> Drive, donor_id -> Donor, time)
Features:   - Publish upcoming blood drives by location
            - Let donors book a time slot
            - Block donors whose last donation was too recent
            - Send reminders and post-donation thank-you messages
            - Alert donors of a blood type in short supply
API:        REST
            GET  /drives?near={zip}
            POST /appointments
            POST /campaigns/shortage
Storage:    PostgreSQL
Tech stack: Node.js, Express, React, SendGrid
```

---

## Example 176

**Intent:**
AED locator for our town with weekly battery and pad checks

**Spec:**
```
Type:       Mobile application with backend (AED registry)
Data model: Aed(id, location_name, lat, lng, access_hours, pad_expiry, battery_expiry)
            Check(id, aed_id -> Aed, status_ok, checked_by, checked_at)
Features:   - Show the nearest public AEDs on a map
            - Show opening hours and access notes
            - Remind guardians to do weekly checks
            - Warn before pads and batteries expire
            - Mark AEDs as out of service
API:        REST
            GET  /aeds?lat={lat}&lng={lng}
            POST /aeds/{id}/checks
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Supabase
```

---

## Example 177

**Intent:**
fire extinguisher inspection with qr tags

**Spec:**
```
Type:       Mobile application with backend (extinguisher inspections)
Data model: Building(id, name, address)
            Extinguisher(id, building_id -> Building, qr_code, type, location, next_service_on)
            Inspection(id, extinguisher_id -> Extinguisher, pressure_ok, seal_ok, notes, inspected_at)
Features:   - Scan the QR tag on each extinguisher
            - Complete the monthly inspection checklist
            - Flag units that need service or replacement
            - Show units overdue for inspection per building
            - Export an inspection report for the fire marshal
API:        REST
            POST /inspections
            GET  /buildings/{id}/overdue
Storage:    PostgreSQL
Tech stack: React Native, Expo Camera, Laravel
```

---

## Example 178

**Intent:**
fire hydrant flushing records for water department

**Spec:**
```
Type:       Web application (hydrant maintenance)
Data model: Hydrant(id, asset_no, lat, lng, flow_class)
            Flush(id, hydrant_id -> Hydrant, static_psi, residual_psi, flow_gpm, flushed_at, crew)
Features:   - Show hydrants on a map coloured by last flush date
            - Record pressure and flow test results
            - Calculate the flow class from the test
            - Plan the flushing program by zone
            - Export records to the GIS system
API:        REST
            GET  /hydrants?zone={z}
            POST /hydrants/{id}/flushes
Storage:    PostgreSQL with PostGIS
Tech stack: Python, Django, ArcGIS API for JavaScript
```

---

## Example 179

**Intent:**
monthly generator test log for hospital

**Spec:**
```
Type:       Web application (generator test log)
Data model: Generator(id, name, kw_rating)
            Test(id, generator_id -> Generator, run_minutes, load_pct, transfer_seconds, passed, tested_at)
Features:   - Record monthly load tests with run time and load
            - Record transfer switch timing
            - Flag tests that fail code requirements
            - Remind engineers when a test is due
            - Produce an annual report for accreditation
API:        REST
            POST /generators/{id}/tests
            GET  /reports/annual?year={y}
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, Thymeleaf
```

---

## Example 180

**Intent:**
Tornado siren test and status

**Spec:**
```
Type:       IoT system (outdoor warning sirens)
Data model: Siren(id, name, lat, lng)
            StatusReport(id, siren_id -> Siren, battery_v, ac_power, rotation_ok, reported_at)
            Activation(id, type, started_at, operator)
Features:   - Activate all or selected sirens from the emergency office
            - Run the monthly silent test and collect status
            - Show siren status on a map
            - Alert when a siren fails a test or loses power
            - Log every activation
API:        REST
            POST /activations
            GET  /sirens/status
Storage:    PostgreSQL
Tech stack: Radio telemetry controllers, Python, FastAPI, React
```

---

## Example 181

**Intent:**
ambulance daily equipment check

**Spec:**
```
Type:       Mobile application with backend (ambulance checks)
Data model: Vehicle(id, call_sign)
            CheckTemplate(id, item, expected_qty)
            DailyCheck(id, vehicle_id -> Vehicle, crew, done_at)
            CheckLine(id, check_id -> DailyCheck, item, qty, expiry_on, ok)
Features:   - Walk the crew through the equipment list per vehicle
            - Record quantities and expiry dates of drugs
            - Flag missing or expired items to the supervisor
            - Lock the vehicle as not ready until critical items are fixed
            - Show check history per vehicle
API:        REST
            POST /vehicles/{id}/checks
            GET  /vehicles/{id}/status
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI
```

---

## Example 182

**Intent:**
evidence locker chain of custody for police

**Spec:**
```
Type:       Web application (evidence management)
Data model: Case(id, case_no)
            Item(id, case_id -> Case, barcode, description, locker)
            CustodyEvent(id, item_id -> Item, from_person, to_person, action, reason, happened_at)
Features:   - Register evidence items with barcode labels
            - Record every transfer of custody with signature
            - Assign items to locker locations
            - Show the full chain of custody per item
            - Flag items eligible for disposal after the case closes
API:        REST
            POST /items
            POST /items/{id}/custody
            GET  /items/{id}/chain
Storage:    PostgreSQL with append-only audit table
Tech stack: C#, ASP.NET Core, Angular
```

---

## Example 183

**Intent:**
wildfire lookout camera smoke detection

**Spec:**
```
Type:       Machine learning model (smoke detection)
Features:   - Detect smoke plumes in camera images
            - Compare with previous frames to reduce false alarms from clouds
            - Estimate the bearing from the camera
            - Send detections with images to the fire office
            - Triangulate location when two towers see the same smoke
Tech stack: Python, PyTorch, YOLOv8, OpenCV
```

---

## Example 184

**Intent:**
we are refugee welcome center, we need app where new arrived people can see the services, the address, and it must work in Dari and Pashto and Tigrinya

**Spec:**
```
Type:       Mobile application (refugee services directory)
Data model: Service(id, category, name, address, lat, lng, hours)
            Translation(service_id -> Service, language, name, description)
Features:   - List services by category such as health, legal and food
            - Show each service on a map with directions
            - Show content in Dari, Pashto, Tigrinya and English
            - Work offline after the first download
            - Read text aloud for low-literacy users
Storage:    Local SQLite synced from a JSON file
Tech stack: Flutter, flutter_map, flutter_tts
```

---

## Example 185

**Intent:**
Asylum case document checklist

**Spec:**
```
Type:       Web application (asylum document tracker)
Data model: Client(id, name, language)
            DocumentType(id, name, required)
            ClientDocument(id, client_id -> Client, type_id -> DocumentType, status, file_path, uploaded_at)
Features:   - Show each client which documents they still need
            - Let clients upload photos of documents from the phone
            - Let caseworkers approve or reject uploads
            - Remind clients about missing documents before deadlines
            - Store files encrypted
API:        REST
            GET  /clients/{id}/checklist
            POST /clients/{id}/documents
Storage:    PostgreSQL, encrypted S3 bucket
Tech stack: Python, Django, Django REST Framework
```

---

## Example 186

**Intent:**
Language class attendance for our refugee center

**Spec:**
```
Type:       Web application (class attendance)
Data model: Class(id, level, teacher)
            Learner(id, name, phone)
            Enrollment(id, class_id -> Class, learner_id -> Learner)
            Attendance(id, enrollment_id -> Enrollment, date, present)
Features:   - Take attendance on a phone during class
            - Show attendance rates per learner
            - Send a WhatsApp reminder to learners who miss two classes
            - Export attendance for funder reports
API:        REST
            POST /classes/{id}/attendance
            GET  /reports/attendance
Storage:    SQLite
Tech stack: Python, Flask, WhatsApp Cloud API
```

---

## Example 187

**Intent:**
Mediation session scheduler

**Spec:**
```
Type:       Web application (mediation scheduling)
Data model: Case(id, reference, dispute_type)
            Party(id, case_id -> Case, name, email)
            Session(id, case_id -> Case, mediator_id, starts_at, room)
            Availability(id, party_id -> Party, slot_at)
Features:   - Collect availability from each party by email link
            - Find slots that suit all parties and the mediator
            - Book a room or video link
            - Send confidential reminders
            - Record the outcome of each session
API:        REST
            POST /cases/{id}/availability
            POST /cases/{id}/sessions
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma
```

---

## Example 188

**Intent:**
jail commissary orders

**Spec:**
```
Type:       Web application (commissary ordering)
Data model: Inmate(id, number, unit, balance)
            Product(id, name, price, restricted)
            Order(id, inmate_id -> Inmate, status, created_at)
            OrderLine(id, order_id -> Order, product_id -> Product, qty)
Features:   - Let inmates order items at a unit kiosk
            - Check the account balance and weekly spending limit
            - Block restricted items per inmate
            - Print packing lists per unit for delivery
            - Deduct the balance when delivered
API:        REST
            POST /orders
            GET  /units/{id}/packing-list
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, React
```

---

## Example 189

**Intent:**
inmate tablet messaging with family, every msg checked by staff

**Spec:**
```
Type:       Web application (monitored messaging)
Data model: Contact(id, inmate_id, family_member_id, approved)
            Message(id, contact_id -> Contact, direction, body, status, sent_at)
            Review(id, message_id -> Message, reviewer, decision)
Features:   - Let approved family members send messages
            - Queue every message for staff review
            - Scan messages for flagged keywords
            - Deliver approved messages to the inmate tablet
            - Keep a full audit log
API:        REST
            POST /messages
            GET  /review-queue
            POST /messages/{id}/review
Storage:    PostgreSQL
Tech stack: Python, Django, React
```

---

## Example 190

**Intent:**
hospice volunteer visits scheduling

**Spec:**
```
Type:       Web application (volunteer visit scheduling)
Data model: Volunteer(id, name, skills, area)
            Patient(id, name, area, preferences)
            Visit(id, volunteer_id -> Volunteer, patient_id -> Patient, scheduled_at, notes)
Features:   - Match volunteers to patients by area and preferences
            - Let volunteers book visits
            - Collect short visit notes
            - Remind volunteers of their visits
            - Report volunteer hours per month
API:        REST
            GET  /patients/{id}/matches
            POST /visits
Storage:    PostgreSQL
Tech stack: Node.js, Express, Vue.js
```

---

## Example 191

**Intent:**
track who has the keys to the community hall

**Spec:**
```
Type:       Web application (key register)
Data model: Key(id, label, door)
            Holder(id, name, phone)
            Loan(id, key_id -> Key, holder_id -> Holder, out_on, back_on)
Features:   - Record who borrowed which key
            - Show keys currently out
            - Remind holders to return keys
            - Show history per key
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 192

**Intent:**
smart lock access codes for our vacation rentals that change every guest

**Spec:**
```
Type:       Webhook service (rental lock codes)
Data model: Property(id, name, lock_id)
            Reservation(id, property_id -> Property, guest_name, check_in, check_out)
            AccessCode(id, reservation_id -> Reservation, code, valid_from, valid_to)
Features:   - Receive new reservations from the booking platform webhook
            - Generate a unique code valid only for the stay
            - Program the code into the smart lock
            - Send the code to the guest the day before check-in
            - Delete the code after checkout
API:        REST
            POST /webhooks/reservation
Storage:    PostgreSQL
Tech stack: Node.js, Fastify, Seam API
```

---

## Example 193

**Intent:**
cabin occupancy for our hiking huts so hikers know if there are beds

**Spec:**
```
Type:       Web application (hut occupancy)
Data model: Hut(id, name, beds, lat, lng)
            Occupancy(id, hut_id -> Hut, date, beds_taken, updated_at)
Features:   - Let hut keepers update beds taken for each night
            - Show free beds per hut on a map
            - Show a 7-day availability calendar
            - Work on slow mobile connections
API:        REST
            GET  /huts
            PUT  /huts/{id}/occupancy/{date}
Storage:    PostgreSQL
Tech stack: SvelteKit, Leaflet
```

---

## Example 194

**Intent:**
trailhead people counter in national park

**Spec:**
```
Type:       IoT system (trail counter)
Data model: Trailhead(id, name)
            Count(id, trailhead_id -> Trailhead, hour, inbound, outbound)
Features:   - Count hikers with a passive infrared sensor
            - Store hourly counts on the device
            - Upload counts weekly over LoRaWAN
            - Show visitor trends per trailhead
Tech stack: PIR sensor, Arduino MKR WAN 1310, The Things Stack, Python
```

---

## Example 195

**Intent:**
boat ramp camera tells fishermen if the parking is full

**Spec:**
```
Type:       IoT system (parking lot fill)
Features:   - Take a picture of the boat ramp parking every 5 minutes
            - Count trailers parked with an object detection model
            - Publish free spaces on a web page
            - Keep a history of busy times
Tech stack: Raspberry Pi, camera, Python, YOLO, Flask
```

---

## Example 196

**Intent:**
Dive log app that imports from my dive computer

**Spec:**
```
Type:       Mobile application (dive log)
Data model: Dive(id, site, max_depth_m, duration_min, water_temp_c, dived_at)
            ProfilePoint(id, dive_id -> Dive, seconds, depth_m)
            Gear(id, name)
Features:   - Download dives from the dive computer over Bluetooth
            - Show each dive's depth profile
            - Add site, buddy and gear
            - Show total dives and bottom time
            - Export logs to UDDF
Storage:    Local SQLite
Tech stack: Kotlin, libdivecomputer, Jetpack Compose
```

---

## Example 197

**Intent:**
track scuba tank hydro test dates for our dive shop

**Spec:**
```
Type:       Web application (cylinder tracking)
Data model: Cylinder(id, serial, size_l, owner, hydro_due_on, visual_due_on)
            Fill(id, cylinder_id -> Cylinder, gas, filled_at)
Features:   - Register customer and rental cylinders
            - Refuse fills for cylinders out of test
            - Warn about tests due in the next 30 days
            - Log every fill with gas mix
            - Print a list of cylinders to send for testing
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 198

**Intent:**
tank level for diesel at our farm

**Spec:**
```
Type:       IoT system (fuel tank level)
Features:   - Measure diesel level with a pressure sensor at the tank bottom
            - Convert level to litres
            - Log fills and draws by detecting jumps
            - Alert when below 300 litres
            - Show level on a phone dashboard
Tech stack: ESP32, 4-20 mA pressure sensor, ESPHome, Home Assistant
```

---

## Example 199

**Intent:**
propane tank gauge reader

**Spec:**
```
Type:       IoT system (propane level reading)
Features:   - Read the existing float gauge dial with a hall effect sensor
            - Report the percent full every 12 hours
            - Notify when the tank is at 25 percent
            - Email the gas supplier automatically for refill
Tech stack: ESP32, hall effect sensor, Arduino C++, SendGrid
```

---

## Example 200

**Intent:**
compost pile thermometer wifi

**Spec:**
```
Type:       IoT system (compost temperature)
Features:   - Read compost core temperature with a long probe
            - Send the reading every hour
            - Remind to turn the pile when temperature drops after a peak
            - Chart temperature per pile
Tech stack: ESP8266, DS18B20 probe, ThingSpeak
```

---

## Example 201

**Intent:**
worm farm moisture

**Spec:**
```
Type:       IoT system (worm bin moisture)
Features:   - Measure bedding moisture with a capacitive sensor
            - Show moisture on a small display
            - Alert when the bin is too dry or too wet
Tech stack: Arduino Nano, capacitive moisture sensor, OLED display
```

---

## Example 202

**Intent:**
cricket farm climate

**Spec:**
```
Type:       IoT system (insect farm climate)
Features:   - Hold bin temperature near 30 °C with heat mats
            - Track humidity in each breeding bin
            - Log daily feed and water given
            - Alert on heater failure
Storage:    SQLite
Tech stack: Raspberry Pi, DHT22 sensors, Python, Flask
```

---

## Example 203

**Intent:**
reptile terrarium heat lamp + uv timer

**Spec:**
```
Type:       IoT system (terrarium controller)
Features:   - Read warm side and cool side temperatures
            - Switch the heat lamp to keep the basking spot at target
            - Run the UVB lamp on a day schedule
            - Drop to a night temperature after lights out
            - Alert when the cool side gets too hot
Tech stack: ESP32, DS18B20 sensors, relay board, ESPHome
```

---

## Example 204

**Intent:**
shrimp farm pond oxygen monitoring, aerators turn on when DO low

**Spec:**
```
Type:       IoT system (aquaculture aeration)
Data model: Pond(id, name, area_m2)
            DoReading(id, pond_id -> Pond, do_mg_l, temp_c, recorded_at)
            AeratorRun(id, pond_id -> Pond, started_at, stopped_at)
Features:   - Measure dissolved oxygen in each pond every 5 minutes
            - Start paddle aerators when oxygen falls below 4 mg/L
            - Stop aerators when oxygen recovers to save power
            - Alert the farm manager at night on critical levels
            - Chart oxygen per pond by night
Storage:    InfluxDB
Tech stack: Optical DO probes, Modbus RTU, Raspberry Pi, Node-RED
```

---

## Example 205

**Intent:**
aquaponics fish feed + water quality log

**Spec:**
```
Type:       Web application (aquaponics log)
Data model: System(id, name)
            WaterTest(id, system_id -> System, ammonia, nitrite, nitrate, ph, tested_at)
            Feeding(id, system_id -> System, grams, fed_at)
            Harvest(id, system_id -> System, crop, kg, harvested_on)
Features:   - Log water tests and feedings
            - Show ammonia and nitrite trends with safe ranges
            - Track plant harvests per system
            - Calculate feed conversion ratio
            - Remind me to test water weekly
API:        REST
            POST /systems/{id}/tests
            POST /systems/{id}/feedings
            GET  /systems/{id}/trends
Storage:    SQLite
Tech stack: Python, FastAPI, HTMX
```

---

## Example 206

**Intent:**
auto top off for aquarium evaporation

**Spec:**
```
Type:       IoT system (aquarium auto top-off)
Features:   - Detect low water with an optical level sensor
            - Pump fresh water from a reservoir until level is restored
            - Stop after a maximum pump time to prevent flooding
            - Alert when the reservoir is empty
Tech stack: Arduino Nano, optical level sensors, 12V pump, Arduino C++
```

---

## Example 207

**Intent:**
ph meter calibration log for the water plant lab

**Spec:**
```
Type:       Web application (calibration log)
Data model: Instrument(id, name, serial, location)
            Calibration(id, instrument_id -> Instrument, buffer_values, slope_pct, offset_mv, passed, done_by, done_at)
Features:   - Record pH meter calibrations with buffer readings
            - Check slope and offset against limits
            - Block instruments that fail calibration
            - Remind staff of daily calibration
            - Export records for audits
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core MVC
```

---

## Example 208

**Intent:**
hey i wanna know when my 3 beehives are being robbed, like heavy traffic at entrance

**Spec:**
```
Type:       IoT system (hive entrance traffic)
Features:   - Count bees passing the entrance with infrared gates
            - Separate incoming and outgoing traffic
            - Detect unusual traffic spikes that suggest robbing
            - Send a phone alert with the hive name
            - Chart daily foraging activity
Storage:    InfluxDB
Tech stack: ESP32, IR gate sensor array, MQTT, Grafana
```

---

## Example 209

**Intent:**
beehive acoustic queenless detector

**Spec:**
```
Type:       Machine learning model (hive sound classification)
Features:   - Convert audio to mel spectrograms
            - Train a small CNN to classify hive state
            - Evaluate accuracy per hive
            - Quantise the model to run on a microcontroller
            - Output a daily hive state report
Tech stack: Python, librosa, TensorFlow, TensorFlow Lite Micro
```

---

## Example 210

**Intent:**
honey extraction batch records and jar labels

**Spec:**
```
Type:       Web application (honey batch tracking)
Data model: Apiary(id, name, location)
            Harvest(id, apiary_id -> Apiary, supers, harvested_on)
            Batch(id, harvest_id -> Harvest, kg, moisture_pct, lot_code)
            JarRun(id, batch_id -> Batch, jar_size_g, count, best_before)
Features:   - Record harvests per apiary
            - Create batches with moisture readings
            - Generate lot codes for traceability
            - Print jar labels with lot and best-before date
            - Trace a jar back to its apiary
API:        REST
            POST /harvests
            POST /batches
            GET  /batches/{lot}/trace
Storage:    SQLite
Tech stack: Python, Django, ReportLab
```

---

## Example 211

**Intent:**
Track my chickens egg laying, which hen lays

**Spec:**
```
Type:       IoT system (nest box tracking)
Data model: Hen(id, name, leg_band_uid)
            NestVisit(id, hen_id -> Hen, box, entered_at, left_at, egg_laid)
Features:   - Read the hen's RFID leg band in each nest box
            - Detect an egg with a weight sensor under the nest
            - Credit the egg to the hen who just left
            - Show eggs per hen per week
            - Flag hens that stopped laying
Storage:    SQLite
Tech stack: ESP32, RFID antennas, load cell, MQTT, Python
```

---

## Example 212

**Intent:**
chicken coop heater and water thaw

**Spec:**
```
Type:       IoT system (coop winter control)
Features:   - Read coop temperature
            - Turn on a heated waterer below freezing
            - Turn on a small heat lamp only below -10 °C
            - Show status in the phone app
Tech stack: Shelly Plus 2PM, temperature add-on, Shelly app
```

---

## Example 213

**Intent:**
Duck pond pump timer w/ solar

**Spec:**
```
Type:       IoT system (solar pond pump)
Features:   - Run the pump when solar battery voltage is high enough
            - Run on a schedule during daylight
            - Stop the pump if the water level is too low
            - Report battery voltage over Wi-Fi
Tech stack: ESP32, INA219 sensor, MOSFET switch, ESPHome
```

---

## Example 214

**Intent:**
freezer at church food pantry, need someone gets text if it fails, we have no money so cheap please

**Spec:**
```
Type:       IoT system (low-cost freezer alarm)
Features:   - Read freezer temperature with a cheap waterproof probe
            - Send a text through a free email-to-SMS gateway
            - Alert when the freezer is above -12 °C for 20 minutes
            - Send a weekly I'm-alive message
Tech stack: ESP8266 (Wemos D1 mini), DS18B20, Arduino C++, Gmail SMTP
```

---

## Example 215

**Intent:**
walk-in cooler door alarm restaurant

**Spec:**
```
Type:       IoT system (cooler door alarm)
Features:   - Detect the cooler door open with a magnetic switch
            - Buzz after 2 minutes open
            - Text the manager after 10 minutes open
            - Log door-open minutes per day
Tech stack: Arduino, reed switch, SIM800L module
```

---

## Example 216

**Intent:**
ice cream shop freezer temps log + daily haccp report

**Spec:**
```
Type:       IoT system (HACCP temperature logging)
Data model: Unit(id, name, type)
            Reading(id, unit_id -> Unit, temp_c, recorded_at)
            CorrectiveAction(id, unit_id -> Unit, note, by, at)
Features:   - Read all display and storage freezers every 5 minutes
            - Show current temperatures on a tablet in the kitchen
            - Require a corrective action entry when a unit is out of range
            - Generate a daily HACCP sheet as PDF
Storage:    PostgreSQL
Tech stack: Zigbee temperature sensors, Raspberry Pi, Python, Django
```

---

## Example 217

**Intent:**
sous vide cooker app

**Spec:**
```
Type:       IoT system (sous vide controller)
Features:   - Hold water bath temperature within 0.1 °C using PID
            - Set temperature and time from a phone
            - Notify when the bath reaches temperature and when cooking ends
            - Offer presets for common foods
Tech stack: ESP32, PT100 sensor, MAX31865, Blynk
```

---

## Example 218

**Intent:**
wine fermentation temp control in garage

**Spec:**
```
Type:       IoT system (fermentation chamber)
Features:   - Read the carboy temperature with a probe in a thermowell
            - Switch a fridge or a heat belt to hold the target
            - Follow a schedule that raises temperature at the end
            - Log temperatures to the cloud
Tech stack: Raspberry Pi, BrewPi-style controller, Python
```

---

## Example 219

**Intent:**
Distillery still temperature logging for compliance

**Spec:**
```
Type:       IoT system (still monitoring)
Data model: Run(id, still, wash_l, started_at, ended_at)
            TempPoint(id, run_id -> Run, pot_c, column_c, recorded_at)
            Cut(id, run_id -> Run, type, abv, litres, at)
Features:   - Log pot and column temperatures during a run
            - Record heads, hearts and tails cuts with volumes and ABV
            - Calculate proof gallons for tax reports
            - Alert on column temperature spikes
            - Export run records
Storage:    PostgreSQL
Tech stack: Raspberry Pi, PT100 probes, Python, Flask
```

---

## Example 220

**Intent:**
milk tank cooling monitor dairy

**Spec:**
```
Type:       IoT system (bulk milk tank monitoring)
Features:   - Read milk temperature in the bulk tank every minute
            - Check that milk is cooled to 4 °C within 2 hours of milking
            - Detect wash cycles and their temperatures
            - Alert the farmer if cooling fails
            - Keep records for the milk buyer
Storage:    TimescaleDB
Tech stack: Teltonika TRB140, PT100 probe, Python, Grafana
```

---

## Example 221

**Intent:**
hay bale moisture probe readings to spreadsheet

**Spec:**
```
Type:       Mobile application (hay moisture log)
Data model: Bale(id, field, cut_date, moisture_pct, lat, lng, measured_at)
Features:   - Read moisture from a Bluetooth hay probe
            - Tag readings with field and GPS
            - Warn when moisture is above 18 percent
            - Export readings to Google Sheets
Tech stack: Flutter, flutter_blue_plus, googleapis
```

---

## Example 222

**Intent:**
silo feed level so feed truck knows when to come

**Spec:**
```
Type:       IoT system (feed silo level)
Data model: Farm(id, name)
            Silo(id, farm_id -> Farm, feed_type, capacity_t)
            LevelReading(id, silo_id -> Silo, tonnes, recorded_at)
Features:   - Measure silo contents with a 3D radar sensor
            - Report levels daily over cellular
            - Predict the empty date from consumption
            - Show silos for all farms to the feed mill
            - Create a delivery order when below 3 days of feed
API:        REST
            GET  /silos?days_left_lt={n}
            POST /orders
Storage:    PostgreSQL
Tech stack: Radar level sensors, LTE-M, Python, FastAPI, React
```

---

## Example 223

**Intent:**
irrigation canal gate open and close remotely

**Spec:**
```
Type:       IoT system (canal gate control)
Features:   - Drive a gate actuator to a target opening
            - Read upstream and downstream water levels
            - Calculate flow through the gate
            - Allow remote control from the water board office
            - Report gate position and battery over LoRaWAN
Tech stack: Arduino MKR WAN 1310, linear actuator, ultrasonic level sensors, ChirpStack
```

---

## Example 224

**Intent:**
borehole pump hours counter for village water committee

**Spec:**
```
Type:       IoT system (borehole pump monitoring)
Features:   - Count pump run hours and litres pumped with a flow meter
            - Send daily totals over SMS
            - Detect a pump breakdown when no water flows for a day
            - Show monthly water supplied on a simple web page
Tech stack: Arduino, pulse flow meter, SIM800L, PHP
```

---

## Example 225

**Intent:**
water meter reading with camera

**Spec:**
```
Type:       IoT system (meter reading by camera)
Features:   - Take a photo of the analog water meter every hour
            - Read digits with an on-device neural network
            - Reject readings that go backwards
            - Send readings to Home Assistant
            - Show daily water use
Tech stack: ESP32-CAM, AI-on-the-edge-device firmware, MQTT, Home Assistant
```

---

## Example 226

**Intent:**
smart gas meter pulse reader

**Spec:**
```
Type:       IoT system (gas meter pulse counter)
Features:   - Count magnetic pulses from the gas meter
            - Convert pulses to cubic metres and kWh
            - Report hourly usage
            - Alert on continuous flow at night as a possible leak
Tech stack: ESP8266, reed switch, ESPHome, InfluxDB
```

---

## Example 227

**Intent:**
heat pump efficiency calculator from my sensors

**Spec:**
```
Type:       Data analysis script (heat pump COP)
Features:   - Calculate heat output from flow and temperature difference
            - Calculate COP per hour and per day
            - Plot COP against outdoor temperature
            - Report seasonal performance factor
Tech stack: Python, pandas, matplotlib
```

---

## Example 228

**Intent:**
boiler room monitoring for our school district, 30 schools

**Spec:**
```
Type:       IoT system (boiler monitoring)
Data model: School(id, name)
            Boiler(id, school_id -> School, model)
            BoilerReading(id, boiler_id -> Boiler, flow_c, return_c, pressure_bar, fault_code, recorded_at)
Features:   - Read boiler data over BACnet at each school
            - Show all boilers with their status on one dashboard
            - Alert on fault codes and low pressure
            - Compare gas use per school per degree day
            - Schedule heating around school holidays
API:        REST
            GET  /schools/{id}/boilers
            GET  /alerts
Storage:    TimescaleDB
Tech stack: BACnet gateways, Python, BAC0, Grafana
```

---

## Example 229

**Intent:**
classroom co2 light that tells teacher to open window

**Spec:**
```
Type:       IoT system (classroom ventilation indicator)
Features:   - Measure CO2 in the classroom
            - Show green under 1000 ppm, yellow up to 1400 and red above
            - Beep softly when red for 10 minutes
            - Log values for the school
Tech stack: Arduino, Sensirion SCD41, LED traffic light, SD card
```

---

## Example 230

**Intent:**
school locker with pin code

**Spec:**
```
Type:       IoT system (electronic locker)
Data model: Locker(id, number)
            Assignment(id, locker_id -> Locker, student_id, pin_hash, valid_until)
Features:   - Unlock a locker with the student's PIN on a keypad
            - Let the office reset a PIN
            - Lock out after 5 wrong tries
            - Log openings per locker
Tech stack: Arduino Mega, keypad, solenoid locks, Arduino C++
```

---

## Example 231

**Intent:**
student hall pass digital, teachers see who is out of class

**Spec:**
```
Type:       Web application (digital hall pass)
Data model: Student(id, name, grade)
            Pass(id, student_id -> Student, teacher_id, destination, out_at, back_at)
Features:   - Let students request a pass from a Chromebook
            - Let teachers approve with one click
            - Show all students currently out of class
            - Limit passes per student per day
            - Flag passes longer than 15 minutes
API:        REST
            POST /passes
            PATCH /passes/{id}
            GET  /passes/active
Storage:    Firebase Firestore
Tech stack: React, Firebase
```

---

## Example 232

**Intent:**
Bus arrival tracker for our school buses so parents see where the bus is

**Spec:**
```
Type:       Mobile application with backend (school bus tracking)
Data model: Bus(id, number, driver)
            Route(id, bus_id -> Bus, name)
            Stop(id, route_id -> Route, name, lat, lng, order)
            Position(id, bus_id -> Bus, lat, lng, recorded_at)
            Child(id, parent_id, stop_id -> Stop)
Features:   - Send bus GPS from a tracker every 15 seconds
            - Show the bus on a map for parents
            - Estimate arrival time at the child's stop
            - Notify parents when the bus is 5 minutes away
            - Notify when the bus is late
API:        REST
            GET  /buses/{id}/position
            GET  /stops/{id}/eta
Storage:    PostgreSQL, Redis
Tech stack: Flutter, Go, GPS trackers
```

---

## Example 233

**Intent:**
student RFID attendance at school gate

**Spec:**
```
Type:       IoT system (gate attendance)
Data model: Student(id, name, class, card_uid)
            GateEvent(id, student_id -> Student, direction, at)
Features:   - Read student RFID cards at the gate
            - Mark students present in the morning
            - Send parents an SMS when their child arrives
            - Show late arrivals to the office
            - Export attendance per class
Storage:    MySQL
Tech stack: Raspberry Pi, MFRC522, Python, Africa's Talking SMS API
```

---

## Example 234

**Intent:**
science fair plant growth experiment logger for kids

**Spec:**
```
Type:       IoT system (plant experiment logger)
Features:   - Take a photo of the plants every hour
            - Log light, temperature and soil moisture
            - Make a time-lapse video at the end
            - Plot sensor data in a chart for the poster
Tech stack: Raspberry Pi, camera, BH1750 light sensor, Python, ffmpeg
```

---

## Example 235

**Intent:**
classroom quiet game, if class quiet for 5 min they get a star

**Spec:**
```
Type:       Desktop application (classroom quiet game)
Features:   - Listen to the classroom microphone level
            - Fill a progress bar while the room stays quiet
            - Award a star after 5 quiet minutes
            - Reset the bar on loud noise
            - Keep a star total per class for the week
Storage:    Local JSON file
Tech stack: Python, PyAudio, Pygame
```

---

## Example 236

**Intent:**
gym members check in with QR at the door and the door unlocks

**Spec:**
```
Type:       IoT system (gym access control)
Data model: Member(id, name, plan, valid_until, qr_token)
            Entry(id, member_id -> Member, entered_at, granted)
Features:   - Scan a member QR code at the door
            - Unlock the door only for active memberships
            - Allow 24/7 access only for premium plans
            - Log every entry attempt
            - Show live member count in the gym
API:        REST
            POST /entries/verify
            GET  /occupancy
Storage:    PostgreSQL
Tech stack: Raspberry Pi, QR scanner, electric strike, Python, FastAPI
```

---

## Example 237

**Intent:**
rowing machine stroke data to app

**Spec:**
```
Type:       Mobile application (rowing workout tracker)
Data model: Workout(id, started_at, distance_m, duration_s)
            Split(id, workout_id -> Workout, split_no, pace_s_500m, stroke_rate)
Features:   - Connect to the rowing machine over Bluetooth FTMS
            - Show pace, stroke rate and distance live
            - Save workouts with 500 m splits
            - Show progress over weeks
Storage:    Local SQLite
Tech stack: Kotlin, Android BLE, Jetpack Compose
```

---

## Example 238

**Intent:**
smart punching bag that counts punches and force

**Spec:**
```
Type:       IoT system (punching bag sensor)
Features:   - Measure bag acceleration with an IMU
            - Detect individual punches
            - Estimate punch force from peak acceleration
            - Show punches per minute on a phone
            - Save training rounds
Tech stack: ESP32, MPU-6050, BLE, Flutter
```

---

## Example 239

**Intent:**
Weights rack tracking which plates are missing

**Spec:**
```
Type:       IoT system (plate rack monitoring)
Features:   - Detect plates on each rack peg with weight sensors
            - Show missing plates on a screen near the rack
            - Remind members to re-rack at closing time
            - Report how often plates are left out
Tech stack: ESP32, load cells, HX711, MQTT, Node-RED
```

---

## Example 240

**Intent:**
cycling power meter data to my training log

**Spec:**
```
Type:       Data pipeline (training data import)
Data model: Ride(id, started_at, duration_s, avg_power_w, normalized_power_w, tss)
            Sample(id, ride_id -> Ride, second, power_w, heart_rate, cadence)
Features:   - Pick up new FIT files from my bike computer's cloud folder
            - Parse power, heart rate and cadence samples
            - Calculate normalized power and training stress score
            - Load rides into my training database
            - Update weekly training load totals
Storage:    PostgreSQL
Tech stack: Python, fitparse, Dropbox API, cron
```

---

## Example 241

**Intent:**
trampoline park jump zone capacity limiter

**Spec:**
```
Type:       IoT system (zone capacity control)
Features:   - Count guests entering and leaving each zone
            - Show a red light when a zone is full
            - Show zone counts to staff on a tablet
            - Log peak counts for safety reports
Tech stack: ESP32, ToF people sensors, MQTT, Vue.js
```

---

## Example 242

**Intent:**
bowling alley lane status board

**Spec:**
```
Type:       Web application (lane status board)
Data model: Lane(id, number, status)
            Booking(id, lane_id -> Lane, party_name, players, starts_at, ends_at)
Features:   - Show each lane as free, playing or reserved
            - Book lanes for groups
            - Show time remaining per lane
            - Display the waiting list on a lobby screen
API:        REST
            GET  /lanes
            POST /bookings
Storage:    SQLite
Tech stack: Node.js, Express, Socket.IO, React
```

---

## Example 243

**Intent:**
pinball machine score tracker with leaderboard

**Spec:**
```
Type:       Web application (pinball leaderboard)
Data model: Machine(id, name)
            Player(id, initials, name)
            Score(id, machine_id -> Machine, player_id -> Player, points, photo_url, posted_at)
Features:   - Let players post scores with a photo of the display
            - Show a leaderboard per machine
            - Let staff verify scores
            - Show weekly champions
API:        REST
            GET  /machines/{id}/scores
            POST /scores
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 244

**Intent:**
arcade token machine counts

**Spec:**
```
Type:       IoT system (arcade revenue counting)
Data model: Cabinet(id, name)
            CoinEvent(id, cabinet_id -> Cabinet, at)
Features:   - Count coins from each cabinet's coin mech signal
            - Send counts to a central server
            - Show plays per cabinet per day
            - Rank cabinets by revenue
Storage:    SQLite
Tech stack: ESP8266, optocoupler input, MQTT, Python
```

---

## Example 245

**Intent:**
concrete curing sensors in the slab so we know when to strip forms

**Spec:**
```
Type:       IoT system (concrete maturity monitoring)
Data model: Pour(id, site, element, mix_design, poured_at)
            Sensor(id, pour_id -> Pour, position)
            TempReading(id, sensor_id -> Sensor, temp_c, recorded_at)
            StrengthEstimate(id, pour_id -> Pour, mpa, estimated_at)
Features:   - Log concrete temperature from embedded wireless sensors
            - Calculate maturity with the Nurse-Saul method
            - Estimate in-place strength from the mix calibration curve
            - Notify the engineer when target strength for stripping is reached
            - Produce a pour report for the client
API:        REST
            POST /pours
            GET  /pours/{id}/strength
Storage:    PostgreSQL
Tech stack: LoRaWAN temperature loggers, Python, FastAPI, React
```

---

## Example 246

**Intent:**
tower crane wind speed alarm

**Spec:**
```
Type:       IoT system (crane wind monitoring)
Features:   - Measure wind speed at the jib with an anemometer
            - Warn the operator in the cab at 15 m/s
            - Signal a stop at 20 m/s with a horn and light
            - Log gusts and stop events
            - Send alerts to the site manager phone
Tech stack: Arduino, ultrasonic anemometer, LoRa radio, Node-RED
```

---

## Example 247

**Intent:**
gas detection in underground mine, workers wear detectors and surface sees all

**Spec:**
```
Type:       IoT system (mine gas monitoring)
Data model: Worker(id, name, lamp_id)
            Detector(id, worker_id -> Worker, serial)
            GasReading(id, detector_id -> Detector, ch4_pct, co_ppm, o2_pct, zone, recorded_at)
            Alarm(id, detector_id -> Detector, gas, level, raised_at)
Features:   - Collect gas readings from worn detectors over an underground mesh network
            - Show each worker's zone and gas levels in the control room
            - Raise alarms on methane, CO or low oxygen
            - Send evacuation messages back to the detectors
            - Keep a full shift record for safety audits
API:        REST
            GET  /workers/positions
            GET  /alarms?open=true
            POST /zones/{id}/evacuate
Storage:    PostgreSQL
Tech stack: Mesh radio detectors, C#, .NET, SignalR, Blazor
```

---

## Example 248

**Intent:**
railway point heater control that turns on only when snow likely

**Spec:**
```
Type:       IoT system (point heater control)
Data model: Switch(id, location, heater_kw)
            RailReading(id, switch_id -> Switch, rail_temp_c, recorded_at)
            HeaterRun(id, switch_id -> Switch, started_at, stopped_at)
Features:   - Measure rail temperature at each switch
            - Fetch the snow and frost forecast
            - Turn heaters on only when frost or snow is expected
            - Report heater energy use per season
            - Alert maintenance when a heater fails to warm the rail
Storage:    TimescaleDB
Tech stack: PLC controllers, Python, MQTT, Met Office API
```

---

## Example 249

**Intent:**
escalator fault and stop count for shopping mall

**Spec:**
```
Type:       IoT system (escalator monitoring)
Data model: Escalator(id, name, floor)
            StopEvent(id, escalator_id -> Escalator, cause, stopped_at, restarted_at)
Features:   - Read stop signals and fault codes from escalator controllers
            - Count emergency stop button presses
            - Show escalators out of service on the security screen
            - Report downtime per escalator monthly
Storage:    PostgreSQL
Tech stack: Modbus gateway, Node-RED, Grafana
```

---

## Example 250

**Intent:**
HVAC filter pressure so we change filters when actually dirty not every 3 months

**Spec:**
```
Type:       IoT system (filter condition monitoring)
Data model: AirHandler(id, building, name)
            PressureReading(id, unit_id -> AirHandler, delta_pa, recorded_at)
            FilterChange(id, unit_id -> AirHandler, changed_on)
Features:   - Measure differential pressure across each filter bank
            - Predict when pressure will reach the change limit
            - Create a work order when a filter needs changing
            - Track filter life after each change
Storage:    PostgreSQL
Tech stack: Differential pressure sensors, ESP32, MQTT, Python
```

---

## Example 251

**Intent:**
rack temperature sensors in our small data center with heatmap

**Spec:**
```
Type:       IoT system (data center thermal map)
Data model: Rack(id, row, position)
            Sensor(id, rack_id -> Rack, height)
            Reading(id, sensor_id -> Sensor, inlet_c, recorded_at)
Features:   - Read inlet temperatures at top, middle and bottom of each rack
            - Show a floor heat map of the room
            - Alert on hot spots above 27 °C
            - Correlate hot spots with CRAC unit status
Storage:    InfluxDB
Tech stack: SNMP temperature probes, Telegraf, Grafana
```

---

## Example 252

**Intent:**
telecom battery cabinet monitoring for remote sites

**Spec:**
```
Type:       IoT system (battery string monitoring)
Data model: Site(id, name)
            BatteryString(id, site_id -> Site, cells)
            CellReading(id, string_id -> BatteryString, cell_no, voltage, internal_resistance, temp_c, recorded_at)
Features:   - Measure voltage and resistance of each cell
            - Detect weak cells by rising internal resistance
            - Report discharge events during outages
            - Estimate backup runtime per site
            - Alert on high cabinet temperature
Storage:    TimescaleDB
Tech stack: Battery monitoring units, SNMP, Python, Grafana
```

---

## Example 253

**Intent:**
electronic shelf labels update prices from our pos

**Spec:**
```
Type:       Webhook service (shelf label sync)
Data model: Label(id, mac, product_id)
            PriceUpdate(id, product_id, price, sent_at, status)
Features:   - Receive price change webhooks from the point of sale system
            - Find the labels linked to the product
            - Push the new price to the ESL access point
            - Retry labels that do not confirm
            - Report labels with low battery
API:        REST
            POST /webhooks/price-change
            GET  /labels?status=failed
Storage:    PostgreSQL
Tech stack: Go, chi router, OpenEPaperLink AP
```

---

## Example 254

**Intent:**
on air light for my home studio when mic is live

**Spec:**
```
Type:       IoT system (on-air sign)
Features:   - Detect when the microphone is in use on the computer
            - Turn on an on-air sign outside the door over Wi-Fi
            - Turn it off when the meeting or recording ends
            - Allow manual override from a button
Tech stack: Python on the PC, ESP8266, MQTT
```

---

## Example 255

**Intent:**
guitar effects pedal with arduino, delay and tremolo

**Spec:**
```
Type:       IoT system (digital guitar pedal)
Features:   - Sample the guitar signal with an audio codec
            - Apply delay with adjustable time and feedback
            - Apply tremolo with adjustable rate and depth
            - Switch effects with footswitches
            - Save presets to EEPROM
Tech stack: Teensy 4.0, Teensy Audio Library, Arduino C++
```

---

## Example 256

**Intent:**
midi foot controller for my looper

**Spec:**
```
Type:       IoT system (MIDI foot controller)
Features:   - Send MIDI program and control changes from footswitches
            - Show the current bank on an LED display
            - Switch banks with a long press
            - Configure button mappings from a desktop editor
Tech stack: Arduino Pro Micro, MIDIUSB library, Python editor
```

---

## Example 257

**Intent:**
band rehearsal room booking with door code

**Spec:**
```
Type:       Web application (rehearsal room booking)
Data model: Room(id, name, hourly_rate)
            Booking(id, room_id -> Room, band_name, starts_at, ends_at, door_code, paid)
Features:   - Show room availability by week
            - Book and pay by the hour
            - Generate a door code valid only during the booking
            - Send the code by email
            - Let admins block maintenance time
API:        REST
            GET  /rooms/{id}/availability
            POST /bookings
Storage:    PostgreSQL
Tech stack: Django, Stripe, Nuki smart lock API
```

---

## Example 258

**Intent:**
TV in the masjid hall should count down to the next iqama and show adhan times plus notices

**Spec:**
```
Type:       Web application (prayer times display)
Data model: PrayerTime(date, fajr, dhuhr, asr, maghrib, isha)
            IqamaRule(id, prayer, offset_min, fixed_time)
            Announcement(id, text, from_date, to_date)
Features:   - Calculate daily prayer times for the mosque location
            - Show adhan and iqama times on a TV screen
            - Count down to the next iqama
            - Show announcements in Arabic and English
            - Let the admin set iqama offsets
API:        REST
            GET  /display/today
            PUT  /iqama-rules
Storage:    SQLite
Tech stack: Python, Flask, adhan library, Raspberry Pi kiosk
```

---

## Example 259

**Intent:**
candle lighting times + shabbat mode for synagogue lights

**Spec:**
```
Type:       IoT system (Shabbat lighting schedule)
Features:   - Calculate candle lighting and havdalah times for the location
            - Switch hall lights on a Shabbat schedule
            - Follow holiday schedules from a Jewish calendar
            - Lock manual changes during Shabbat
Tech stack: Raspberry Pi, Python, Hebcal API, Shelly relays
```

---

## Example 260

**Intent:**
Hand hygiene compliance in hospital ward, dispenser counts vs room entries

**Spec:**
```
Type:       IoT system (hand hygiene monitoring)
Data model: Room(id, ward, number)
            Dispenser(id, room_id -> Room)
            DispenseEvent(id, dispenser_id -> Dispenser, at)
            EntryEvent(id, room_id -> Room, at)
Features:   - Count dispenser uses with a sensor in each dispenser
            - Count room entries with a door sensor
            - Calculate compliance per room and shift
            - Show ward compliance on a dashboard
            - Send weekly reports to ward managers
API:        REST
            GET  /wards/{id}/compliance?week={w}
Storage:    PostgreSQL
Tech stack: BLE dispensers, ESP32 gateways, Python, Metabase
```

---

## Example 261

**Intent:**
dental office autoclave sterilization cycle log

**Spec:**
```
Type:       Web application (sterilization log)
Data model: Autoclave(id, name)
            Cycle(id, autoclave_id -> Autoclave, cycle_no, temp_c, pressure_kpa, duration_min, passed, run_at)
            Pouch(id, cycle_id -> Cycle, instrument_set, label)
Features:   - Import cycle printouts from the autoclave USB log
            - Record indicator results for each cycle
            - Print pouch labels linked to the cycle
            - Trace which patient got instruments from a cycle
            - Remind weekly spore tests
Storage:    SQLite
Tech stack: Python, Django, Zebra label printer
```

---

## Example 262

**Intent:**
vet clinic surgery anesthesia monitor recording

**Spec:**
```
Type:       Desktop application (anesthesia record)
Data model: Patient(id, name, species, weight_kg)
            Procedure(id, patient_id -> Patient, started_at)
            VitalSample(id, procedure_id -> Procedure, heart_rate, spo2, etco2, temp_c, at)
Features:   - Read vitals from the patient monitor over serial
            - Record drugs given with dose and time
            - Chart vitals every 5 minutes as an anesthesia sheet
            - Warn on vitals outside species ranges
            - Print the record for the patient file
Storage:    SQLite
Tech stack: C#, WPF, LiveCharts
```

---

## Example 263

**Intent:**
infusion pump fleet tracking in hospital, where is each pump

**Spec:**
```
Type:       IoT system (asset tracking)
Data model: Pump(id, serial, model, maintenance_due_on)
            Zone(id, name, floor)
            Sighting(id, pump_id -> Pump, zone_id -> Zone, seen_at)
Features:   - Locate pumps with BLE tags and room receivers
            - Search for the nearest free pump
            - Show pumps due for maintenance and where they are
            - Alert when a pump leaves the building
API:        REST
            GET  /pumps?status=free&near={zone}
            GET  /pumps/maintenance-due
Storage:    PostgreSQL
Tech stack: BLE asset tags, Kontakt.io gateways, Node.js, React
```

---

## Example 264

**Intent:**
dialysis water treatment logs

**Spec:**
```
Type:       Web application (water treatment log)
Data model: TestType(id, name, limit)
            Test(id, type_id -> TestType, value, passed, tested_by, tested_at)
Features:   - Record daily chlorine, conductivity and hardness tests
            - Compare results with dialysis water limits
            - Require a supervisor sign-off for failures
            - Show trends for the medical director
            - Export monthly reports
Storage:    PostgreSQL
Tech stack: Ruby on Rails
```

---

## Example 265

**Intent:**
Hospital bed availability board for ER

**Spec:**
```
Type:       Web application (bed board)
Data model: Ward(id, name)
            Bed(id, ward_id -> Ward, number, status, patient_ref, updated_at)
            Request(id, from_er_ref, ward_id -> Ward, requested_at, assigned_bed_id -> Bed)
Features:   - Show beds per ward as occupied, clean, dirty or free
            - Let housekeeping mark beds clean from a phone
            - Let ER request a bed in a ward
            - Assign beds and notify the ward
            - Show average turnaround time
API:        REST
            GET  /beds
            PATCH /beds/{id}
            POST /requests
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, Angular, WebSockets
```

---

## Example 266

**Intent:**
smart insole for diabetic foot pressure

**Spec:**
```
Type:       IoT system (pressure insole)
Features:   - Measure plantar pressure with sensors in the insole
            - Detect high pressure held too long at one spot
            - Vibrate a wristband to tell the wearer to shift
            - Send daily pressure maps to a phone app
            - Share reports with a podiatrist
Tech stack: nRF52832, FSR sensors, BLE, Flutter
```

---

## Example 267

**Intent:**
wheelchair tilt and pressure relief reminder

**Spec:**
```
Type:       IoT system (wheelchair pressure relief)
Features:   - Detect seat tilt angle with an accelerometer
            - Remind the user to tilt every 30 minutes
            - Log how long each tilt is held
            - Show daily compliance to the therapist
Tech stack: ESP32, MPU-6050, BLE, React Native
```

---

## Example 268

**Intent:**
Big button phone for my mum, only 4 contacts with photos

**Spec:**
```
Type:       Mobile application (simplified phone launcher)
Data model: Contact(id, name, phone, photo_path, position)
Features:   - Show four large photo buttons that call a contact
            - Read out the contact name before calling
            - Lock settings behind a PIN for family
            - Answer calls automatically from favourites
Storage:    Local storage on the device
Tech stack: Kotlin, Android launcher app
```

---

## Example 269

**Intent:**
Smart cane that vibrates when obstacle ahead

**Spec:**
```
Type:       IoT system (obstacle detecting cane)
Features:   - Measure distance ahead with an ultrasonic sensor
            - Vibrate stronger as obstacles get closer
            - Detect head-height obstacles with an upward sensor
            - Run all day on a rechargeable battery
Tech stack: Arduino Nano, HC-SR04 sensors, vibration motor
```

---

## Example 270

**Intent:**
doorbell for deaf person that flashes lights and vibrates watch

**Spec:**
```
Type:       IoT system (visual doorbell)
Features:   - Detect a doorbell press
            - Flash smart lights in the house
            - Vibrate a smartwatch with a notification
            - Detect a smoke alarm sound and alert the same way
Tech stack: Zigbee button, Philips Hue, Home Assistant, Wear OS companion app
```

---

## Example 271

**Intent:**
wheelchair ramp ble door opener

**Spec:**
```
Type:       IoT system (accessible door opener)
Features:   - Detect a registered phone or fob approaching the door
            - Trigger the automatic door opener
            - Hold the door open longer for wheelchair users
            - Log uses for the building manager
Tech stack: ESP32, BLE beacons, relay, Arduino C++
```

---

## Example 272

**Intent:**
lifting harness usage log for care home hoists, need inspection every 6 month

**Spec:**
```
Type:       Web application (hoist and sling register)
Data model: Hoist(id, location, serial, inspected_on)
            Sling(id, size, serial, inspected_on)
            Inspection(id, item_type, item_id, result, inspector, done_on)
Features:   - Register hoists and slings with QR labels
            - Record six-monthly LOLER inspections
            - Remove failed items from use
            - Remind managers of upcoming inspections
            - Report all items per home
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Livewire
```

---

## Example 273

**Intent:**
dementia friendly clock which say morning, afternoon, evening

**Spec:**
```
Type:       IoT system (day clock)
Features:   - Show the weekday, date and part of day in large words
            - Show reminders such as take medicine at set times
            - Dim the screen at night
            - Let family set reminders from a phone
Tech stack: Raspberry Pi, 10-inch display, Python, Flask
```

---

## Example 274

**Intent:**
elderly friendly radio with 3 stations only, one knob

**Spec:**
```
Type:       IoT system (simple internet radio)
Features:   - Play internet radio stations
            - Change station with one large knob
            - Set stations remotely by family
            - Speak the station name when changed
Tech stack: ESP32-S3, I2S amplifier, rotary encoder, Arduino C++
```

---

## Example 275

**Intent:**
sports hall lighting booking connected to the lights

**Spec:**
```
Type:       Web application (hall lighting by booking)
Data model: Court(id, name)
            Booking(id, court_id -> Court, club, starts_at, ends_at)
Features:   - Book courts by the hour
            - Switch court lights on 5 minutes before each booking
            - Switch lights off after the booking ends
            - Report light hours per club for billing
API:        REST
            POST /bookings
            GET  /courts/{id}/schedule
Storage:    PostgreSQL
Tech stack: Python, Django, KNX IP gateway
```

---

## Example 276

**Intent:**
tennis court ball machine app control

**Spec:**
```
Type:       Mobile application (ball machine control)
Features:   - Connect to the ball machine over Bluetooth
            - Set speed, spin and feed rate
            - Create drills with sequences of shots
            - Run random drills
Storage:    Local storage
Tech stack: Swift, Core Bluetooth
```

---

## Example 277

**Intent:**
golf course irrigation by zone using soil sensors and ET

**Spec:**
```
Type:       IoT system (golf course irrigation)
Data model: Zone(id, hole, type, area_m2)
            SoilReading(id, zone_id -> Zone, moisture_pct, recorded_at)
            Run(id, zone_id -> Zone, minutes, started_at)
Features:   - Read soil moisture sensors on greens and fairways
            - Calculate water need from evapotranspiration
            - Schedule night watering per zone
            - Skip zones after rain
            - Report water use per hole
API:        REST
            GET  /zones
            POST /zones/{id}/run
Storage:    PostgreSQL
Tech stack: LoRaWAN soil sensors, Python, FastAPI, Rain Bird controller API
```

---

## Example 278

**Intent:**
horse arena footing moisture + water truck

**Spec:**
```
Type:       IoT system (arena footing monitoring)
Features:   - Measure arena footing moisture at several points
            - Show dry spots on a map of the arena
            - Turn on sprinklers for dry sections
            - Log watering per day
Tech stack: ESP32, capacitive sensors, LoRa, Node-RED
```

---

## Example 279

**Intent:**
Ice fishing tip-up alarm

**Spec:**
```
Type:       IoT system (tip-up alert)
Features:   - Detect a flag going up on the tip-up
            - Send an alert to a phone in the shelter over LoRa
            - Show which hole had the bite
            - Run in freezing temperatures for a day
Tech stack: Arduino, LoRa RFM95, tilt switch, Android app
```

---

## Example 280

**Intent:**
trail camera for hunting, send picture to phone

**Spec:**
```
Type:       IoT system (cellular trail camera)
Features:   - Take a photo when the PIR sensor detects motion
            - Send a compressed photo over LTE
            - Batch photos at night to save battery
            - Show photos in a phone app by date
Tech stack: ESP32-CAM, SIM7600 LTE module, Firebase Storage
```

---

## Example 281

**Intent:**
fish finder sonar data logging to map depth of our lake

**Spec:**
```
Type:       Data analysis script (bathymetry mapping)
Features:   - Parse sonar logs into depth points
            - Filter out bad readings
            - Interpolate a depth grid
            - Draw contour lines
            - Export a map as GeoTIFF and image
Tech stack: Python, pandas, SciPy, GDAL, matplotlib
```

---

## Example 282

**Intent:**
kayak rental with smart locks on the rack

**Spec:**
```
Type:       Mobile application with backend (self-service kayak rental)
Data model: Kayak(id, rack_slot, type, status)
            Rental(id, kayak_id -> Kayak, user_id, started_at, ended_at, amount)
            User(id, phone, waiver_signed_at)
Features:   - Sign a safety waiver in the app
            - Pay and unlock a kayak from the rack
            - Track rental time
            - Lock the kayak back to end the rental
            - Report kayak usage and revenue
API:        REST
            POST /rentals
            POST /rentals/{id}/end
Storage:    PostgreSQL
Tech stack: Flutter, Node.js, Stripe, BLE smart locks
```

---

## Example 283

**Intent:**
Paddle board rental waitlist

**Spec:**
```
Type:       Web application (rental waitlist)
Data model: WaitlistEntry(id, name, phone, party_size, joined_at, notified_at)
Features:   - Let customers join the waitlist on a phone
            - Show their position
            - Text them when a board is free
            - Remove no-shows after 10 minutes
API:        REST
            POST /waitlist
            POST /waitlist/{id}/notify
Storage:    SQLite
Tech stack: Python, Flask, Twilio
```

---

## Example 284

**Intent:**
me and my friend we have small boat for tourist, I want to know where is boat and how much fuel, in Greek and English please

**Spec:**
```
Type:       Mobile application with backend (tour boat tracking)
Data model: Boat(id, name)
            Position(id, boat_id -> Boat, lat, lng, speed_kn, recorded_at)
            FuelReading(id, boat_id -> Boat, level_pct, recorded_at)
Features:   - Show each boat position on a map
            - Show fuel level and speed
            - Alert when fuel is low far from port
            - Show trip history per day
            - Offer the app in Greek and English
API:        REST
            GET  /boats
            GET  /boats/{id}/track?date={d}
Storage:    PostgreSQL
Tech stack: GPS tracker with fuel sensor input, Traccar, React Native
```

---

## Example 285

**Intent:**
sailing regatta start sequence timer

**Spec:**
```
Type:       Mobile application (regatta start timer)
Features:   - Run 5-4-1-0 start sequences
            - Sound a horn through a Bluetooth speaker at each signal
            - Sync the timer to the race committee gun
            - Record finishing times by sail number
Storage:    Local storage
Tech stack: Flutter, just_audio
```

---

## Example 286

**Intent:**
Regatta results with handicap calculation

**Spec:**
```
Type:       Web application (regatta results)
Data model: Regatta(id, name)
            Boat(id, sail_no, name, handicap)
            Race(id, regatta_id -> Regatta, number, start_at)
            Finish(id, race_id -> Race, boat_id -> Boat, finished_at, status)
Features:   - Enter finish times per race
            - Calculate corrected times with Portsmouth Yardstick handicaps
            - Score series with discards
            - Handle DNF, DNS and OCS codes
            - Publish results to the club site
API:        REST
            POST /races/{id}/finishes
            GET  /regattas/{id}/results
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 287

**Intent:**
reefer container temps on the ship

**Spec:**
```
Type:       IoT system (reefer container monitoring)
Data model: Vessel(id, name, imo)
            Container(id, number, vessel_id -> Vessel, setpoint_c, cargo)
            ReeferReading(id, container_id -> Container, supply_c, return_c, power_on, recorded_at)
Features:   - Collect reefer controller data over power-line modems on deck
            - Send summaries over the ship's satellite link
            - Alert when a container drifts from its setpoint
            - Detect containers that lost power
            - Give cargo owners a temperature report on discharge
API:        REST
            GET  /vessels/{id}/reefers
            GET  /containers/{number}/report
Storage:    PostgreSQL
Tech stack: Reefer modems, Python, FastAPI, React
```

---

## Example 288

**Intent:**
container door opened alarm for shipments

**Spec:**
```
Type:       IoT system (container security)
Features:   - Detect container door opening with a light and magnetic sensor
            - Record GPS position of each opening
            - Send an alert if opened outside an approved geofence
            - Report shock events during transport
Tech stack: Nordic nRF9160, LTE-M, Golioth, Node.js
```

---

## Example 289

**Intent:**
truck tyre pressure and temp to the dispatcher

**Spec:**
```
Type:       IoT system (tyre pressure monitoring)
Data model: Truck(id, plate)
            Tyre(id, truck_id -> Truck, position)
            TyreReading(id, tyre_id -> Tyre, pressure_bar, temp_c, recorded_at)
Features:   - Receive TPMS sensor data in the cab gateway
            - Send readings to the fleet backend
            - Alert the driver and dispatcher on slow leaks
            - Show tyre positions on a truck diagram
Storage:    TimescaleDB
Tech stack: BLE TPMS sensors, Teltonika gateway, Python, Grafana
```

---

## Example 290

**Intent:**
Pallet temperature tags for our fruit exports, read when pallet arrives

**Spec:**
```
Type:       Mobile application with backend (pallet temperature tags)
Data model: Pallet(id, sscc, product, origin)
            Tag(id, pallet_id -> Pallet, nfc_uid)
            TagReading(id, tag_id -> Tag, temp_c, recorded_at)
Features:   - Read the NFC temperature tag with a phone at arrival
            - Upload the full temperature history
            - Flag pallets with excursions
            - Calculate remaining shelf life from temperature history
            - Share a report with the importer
API:        REST
            POST /tags/{uid}/upload
            GET  /pallets/{sscc}
Storage:    PostgreSQL
Tech stack: Kotlin, Android NFC, Spring Boot
```

---

## Example 291

**Intent:**
NOTAM bot for my home airfield

**Spec:**
```
Type:       Bot (aviation NOTAM alerts)
Features:   - Fetch NOTAMs for a list of airfields every hour
            - Detect new or changed NOTAMs
            - Post them to a Telegram group in plain English
            - Highlight runway closures
Storage:    SQLite
Tech stack: Python, FAA NOTAM API, python-telegram-bot
```

---

## Example 292

**Intent:**
hot air balloon flight log + envelope hours

**Spec:**
```
Type:       Mobile application (balloon flight log)
Data model: Envelope(id, registration, hours, next_inspection_hours)
            Flight(id, envelope_id -> Envelope, launch_site, landing_site, duration_min, flown_on, passengers)
Features:   - Log flights with launch and landing sites
            - Add envelope hours automatically
            - Warn when inspection hours are near
            - Record GPS track during flight
Storage:    Local SQLite
Tech stack: Flutter, geolocator
```

---

## Example 293

**Intent:**
SDR spectrum waterfall logger to find interference

**Spec:**
```
Type:       Command-line tool (spectrum survey)
Features:   - Sweep the band with an RTL-SDR
            - Record power per frequency over time
            - Render a waterfall image
            - Flag signals above the noise floor
            - Save results to CSV
Tech stack: Python, pyrtlsdr, NumPy, matplotlib
```

---

## Example 294

**Intent:**
repeater controller with voice id and timeout

**Spec:**
```
Type:       IoT system (radio repeater controller)
Features:   - Detect carrier on the receiver
            - Key the transmitter while signal is present
            - Send the callsign ID in Morse or voice every 10 minutes
            - Time out long transmissions after 3 minutes
            - Allow remote commands via DTMF tones
Tech stack: Arduino, MT8870 DTMF decoder, Arduino C++
```

---

## Example 295

**Intent:**
robot arm pick and place with camera

**Spec:**
```
Type:       IoT system (vision pick and place)
Features:   - Detect parts on a tray with a camera
            - Convert pixel positions to robot coordinates
            - Plan a pick and place move
            - Sort parts by colour into bins
            - Show a live view with detections
Tech stack: Python, OpenCV, ROS 2, uFactory xArm SDK
```

---

## Example 296

**Intent:**
small warehouse robot that follows a line and carries totes between stations

**Spec:**
```
Type:       IoT system (tote transport robot)
Data model: Station(id, name, marker_id)
            Task(id, from_station_id -> Station, to_station_id -> Station, status, created_at)
Features:   - Follow a floor tape path between stations
            - Read station markers with QR codes
            - Accept transport tasks from a web page
            - Stop for obstacles with a lidar
            - Report battery and position
API:        REST
            POST /tasks
            GET  /robot/status
Storage:    SQLite
Tech stack: ROS 2, Raspberry Pi 4, RPLIDAR A1, Python
```

---

## Example 297

**Intent:**
pcb test jig that checks each board and prints pass fail label

**Spec:**
```
Type:       Desktop application (PCB functional tester)
Data model: Board(id, serial, tested_at, result)
            Measurement(id, board_id -> Board, test_name, value, low, high, passed)
Features:   - Measure voltages and currents on test points through a fixture
            - Flash firmware and run self-tests
            - Compare each value with limits
            - Print a pass or fail label with serial
            - Save results for traceability
Storage:    SQLite
Tech stack: Python, PyVISA, Tkinter, Brother label printer
```

---

## Example 298

**Intent:**
burn in rack logs for power supplies

**Spec:**
```
Type:       IoT system (burn-in monitoring)
Data model: Unit(id, serial, slot)
            BurnIn(id, unit_id -> Unit, started_at, ended_at, passed)
            Sample(id, burnin_id -> BurnIn, voltage, current, temp_c, at)
Features:   - Read output voltage and current for each slot
            - Run a 48-hour burn-in with load cycling
            - Fail units that drift out of tolerance
            - Show the rack status on a screen
            - Export results per serial
Storage:    PostgreSQL
Tech stack: Raspberry Pi, INA219 sensors, electronic loads (SCPI), Python
```

---

## Example 299

**Intent:**
electronic parts inventory with drawer locations, scan barcode from digikey bag

**Spec:**
```
Type:       Web application (component inventory)
Data model: Part(id, mpn, manufacturer, description, footprint)
            Location(id, cabinet, drawer)
            Stock(id, part_id -> Part, location_id -> Location, qty)
Features:   - Scan Digi-Key bag barcodes to add parts
            - Fetch descriptions and datasheets automatically
            - Assign drawer locations
            - Search parts by value and footprint
            - Reduce stock from a project BOM
API:        REST
            POST /parts/scan
            GET  /parts?q={q}
            POST /boms/{id}/consume
Storage:    SQLite
Tech stack: Python, Django, Digi-Key API
```

---

## Example 300

**Intent:**
oscilloscope screenshot grabber

**Spec:**
```
Type:       Command-line script (scope screenshot)
Features:   - Connect to the scope over LAN with SCPI
            - Request a screen capture
            - Save it as a PNG with a timestamp
            - Optionally save waveform data as CSV
Tech stack: Python, PyVISA
```

---

## Example 301

**Intent:**
cnc router spindle hours and tool wear

**Spec:**
```
Type:       Web application (CNC tool tracking)
Data model: Tool(id, type, diameter_mm, max_minutes)
            Job(id, file, started_at, ended_at)
            ToolUse(id, tool_id -> Tool, job_id -> Job, minutes)
Features:   - Read job runtime from the CNC controller logs
            - Track minutes per tool
            - Warn when a tool needs sharpening or replacing
            - Track spindle total hours
Storage:    SQLite
Tech stack: Python, Flask, GRBL log parsing
```

---

## Example 302

**Intent:**
blacksmith forge temperature with color guide

**Spec:**
```
Type:       IoT system (forge thermometer)
Features:   - Read forge temperature with a K-type thermocouple
            - Show temperature and the matching steel colour on a display
            - Beep when the target forging temperature is reached
Tech stack: Arduino, MAX6675, TFT display
```

---

## Example 303

**Intent:**
glass kiln annealing schedule from phone

**Spec:**
```
Type:       IoT system (glass kiln controller)
Features:   - Run annealing schedules with ramps and holds
            - Choose programs for glass types
            - Watch progress from a phone
            - Alert if the kiln overshoots
Tech stack: ESP32, MAX31855, solid state relay, Blynk
```

---

## Example 304

**Intent:**
watch repair shop job tracking with timegrapher results

**Spec:**
```
Type:       Web application (watch repair jobs)
Data model: Customer(id, name, phone)
            Watch(id, customer_id -> Customer, brand, model, serial)
            Job(id, watch_id -> Watch, issue, status, quote)
            TimegrapherResult(id, job_id -> Job, rate_s_day, amplitude, beat_error_ms, measured_at)
Features:   - Log incoming watches with photos
            - Quote and track repair status
            - Record timegrapher results before and after service
            - Text the customer when the watch is ready
            - Print a service certificate
API:        REST
            POST /jobs
            POST /jobs/{id}/timegrapher
            PATCH /jobs/{id}
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Twilio
```

---

## Example 305

**Intent:**
piano humidity control in concert hall

**Spec:**
```
Type:       IoT system (piano climate control)
Features:   - Read humidity near the piano
            - Turn a humidifier or dehumidifier on to keep 45 percent
            - Log humidity for the piano technician
            - Alert when water tank is empty
Tech stack: ESP32, SHT31, smart plugs, ESPHome
```

---

## Example 306

**Intent:**
drone mapping images to orthomosaic automatic pipeline

**Spec:**
```
Type:       Data pipeline (drone photogrammetry)
Data model: Mission(id, site, flown_on)
            ImageSet(id, mission_id -> Mission, count, storage_path)
            Output(id, mission_id -> Mission, type, path)
Features:   - Pick up uploaded drone image sets from cloud storage
            - Run photogrammetry to build an orthomosaic and elevation model
            - Generate map tiles
            - Notify the client when outputs are ready
            - Archive raw images after 30 days
Storage:    S3
Tech stack: Python, OpenDroneMap (NodeODM), Celery, GDAL
```

---

## Example 307

**Intent:**
drone no fly zone checker before flight

**Spec:**
```
Type:       Web application (airspace check)
Data model: Zone(id, name, type, geometry, max_altitude_m)
Features:   - Let pilots draw a flight area on a map
            - Check it against restricted airspace zones
            - Show maximum allowed altitude
            - Show temporary restrictions for the date
            - Save checks as PDF
API:        REST
            POST /checks
Storage:    PostgreSQL with PostGIS
Tech stack: Python, FastAPI, Leaflet, OpenAIP data
```

---

## Example 308

**Intent:**
crop spraying drone job records

**Spec:**
```
Type:       Web application (spray job records)
Data model: Field(id, farm, boundary)
            Chemical(id, name, registration_no)
            SprayJob(id, field_id -> Field, chemical_id -> Chemical, rate_l_ha, area_ha, flown_at, wind_kmh)
Features:   - Plan jobs per field with chemical and rate
            - Import flight logs to confirm area sprayed
            - Record wind and weather at spray time
            - Produce the legal spray record
            - Invoice farmers by hectare
Storage:    PostgreSQL with PostGIS
Tech stack: Django, GeoDjango, Leaflet
```

---

## Example 309

**Intent:**
robotics club parts inventory and who borrowed the servos

**Spec:**
```
Type:       Web application (club parts library)
Data model: Item(id, name, category, qty_total)
            Loan(id, item_id -> Item, member, qty, out_on, back_on)
Features:   - List kit parts and quantities
            - Let members borrow parts
            - Show what is out and by whom
            - Remind borrowers after two weeks
Storage:    SQLite
Tech stack: Python, Flask, Bootstrap
```

---

## Example 310

**Intent:**
VEX robotics skills run timer and score sheet

**Spec:**
```
Type:       Web application (skills run scoring)
Data model: Team(id, number)
            Run(id, team_id -> Team, type, score, run_at)
Features:   - Run a 60-second timer with start and end sounds
            - Enter scores for driver and programming runs
            - Keep the best of each per team
            - Show a combined ranking
Storage:    SQLite
Tech stack: SvelteKit
```

---

## Example 311

**Intent:**
battle bot weapon arming safety, arm only with key and remote

**Spec:**
```
Type:       IoT system (combat robot safety)
Features:   - Require a physical key and a remote signal to arm the weapon
            - Disarm instantly on signal loss
            - Show arming state with an LED
            - Log arm and disarm events
Tech stack: Arduino, RC receiver PWM input, ESC control
```

---

## Example 312

**Intent:**
underwater rov telemetry overlay

**Spec:**
```
Type:       Desktop application (ROV control station)
Features:   - Show the ROV camera video
            - Overlay depth, heading and temperature
            - Control thrusters with a gamepad
            - Record video with telemetry
Tech stack: Python, PyQt5, OpenCV, MAVLink (pymavlink)
```

---

## Example 313

**Intent:**
smart glasses that describe objects for blind users

**Spec:**
```
Type:       Mobile application (scene description)
Features:   - Capture images from a head-mounted camera
            - Describe the scene with a vision model
            - Read text found in the image aloud
            - Answer questions about the scene by voice
Tech stack: Swift, Core ML, Vision framework, AVSpeechSynthesizer
```

---

## Example 314

**Intent:**
kid gps watch geofence for school

**Spec:**
```
Type:       Mobile application with backend (child location alerts)
Data model: Child(id, name, device_id)
            Place(id, name, lat, lng, radius_m)
            LocationEvent(id, child_id -> Child, place_id -> Place, type, at)
Features:   - Receive positions from the watch
            - Notify parents when the child arrives at or leaves school
            - Show the last position on a map
            - Let parents define places
API:        REST
            GET  /children/{id}/location
            POST /places
Storage:    PostgreSQL
Tech stack: Flutter, Firebase Cloud Messaging, Node.js
```

---

## Example 315

**Intent:**
posture sensor clip that buzzes when I slouch

**Spec:**
```
Type:       IoT system (posture trainer)
Features:   - Measure upper back angle with an IMU
            - Calibrate a good posture at start
            - Vibrate after 30 seconds of slouching
            - Show daily slouch minutes in an app
Tech stack: nRF52840, LSM6DS3, BLE, Flutter
```

---

## Example 316

**Intent:**
baby room monitor temp and crying

**Spec:**
```
Type:       IoT system (nursery monitor)
Features:   - Detect crying with a microphone and sound classifier
            - Read room temperature and humidity
            - Send phone alerts to parents
            - Play white noise on demand
Tech stack: Raspberry Pi, USB microphone, YAMNet TFLite, Home Assistant
```

---

## Example 317

**Intent:**
sleep apnea snoring recorder overnight

**Spec:**
```
Type:       Mobile application (snoring recorder)
Data model: Night(id, started_at, ended_at)
            Episode(id, night_id -> Night, started_at, duration_s, loudness_db)
Features:   - Record audio overnight from the phone
            - Detect snoring and silent pauses
            - Save short clips of episodes
            - Show a morning report
Storage:    Local storage
Tech stack: Kotlin, TensorFlow Lite audio classifier
```

---

## Example 318

**Intent:**
tremor measurement app for parkinson patient

**Spec:**
```
Type:       Mobile application (tremor tracking)
Data model: Test(id, hand, frequency_hz, amplitude, taken_at, medication_taken_at)
Features:   - Measure hand tremor with the phone accelerometer for 30 seconds
            - Calculate dominant frequency and amplitude
            - Log tests with medication times
            - Show trends for the neurologist
Storage:    Local SQLite
Tech stack: Swift, Core Motion, Accelerate (FFT)
```

---

## Example 319

**Intent:**
hearing loop status at venues

**Spec:**
```
Type:       Web application (hearing loop directory)
Data model: Venue(id, name, address, lat, lng)
            LoopReport(id, venue_id -> Venue, working, reported_at)
Features:   - List venues with hearing loops
            - Let users report if a loop worked
            - Show venues on a map
            - Flag loops reported broken
API:        REST
            GET  /venues
            POST /venues/{id}/reports
Storage:    PostgreSQL
Tech stack: Next.js, Supabase, Mapbox
```

---

## Example 320

**Intent:**
speech therapy app with mic for kids practicing sounds

**Spec:**
```
Type:       Mobile application (speech practice)
Data model: Child(id, name)
            Exercise(id, target_sound, words)
            Attempt(id, child_id -> Child, exercise_id -> Exercise, word, score, recorded_at)
Features:   - Show picture words for a target sound
            - Record the child saying each word
            - Score pronunciation with a speech model
            - Give stars and animations
            - Share progress with the therapist
Storage:    Firebase
Tech stack: Flutter, Azure Speech pronunciation assessment
```

---

## Example 321

**Intent:**
switch accessible game for kids using one button

**Spec:**
```
Type:       Browser game (one-switch adventure)
Features:   - Play a side-scrolling game controlled with one switch
            - Scan between actions automatically
            - Adjust scan speed and timing
            - Support keyboard and USB switch input
            - Use high-contrast graphics and sound cues
Storage:    Browser localStorage
Tech stack: JavaScript, Phaser 3
```

---

## Example 322

**Intent:**
Plain grip strength tracker for physio

**Spec:**
```
Type:       IoT system (grip dynamometer)
Features:   - Measure grip force with a load cell in a handle
            - Record best of three attempts per hand
            - Show results in a tablet app
            - Chart progress over weeks
Tech stack: ESP32, load cell, HX711, BLE, React Native
```

---

## Example 323

**Intent:**
prosthetic socket pressure sensors data viewer

**Spec:**
```
Type:       Desktop application (socket pressure viewer)
Features:   - Read pressure sensor arrays from inside the socket over Bluetooth
            - Show a live colour map of pressures
            - Record walking trials
            - Compare two socket fittings side by side
Storage:    Local files (HDF5)
Tech stack: Python, PyQt5, pyqtgraph, bleak
```

---

## Example 324

**Intent:**
we want to see how many people are in the reading room of our university study hall so students don't walk there for nothing

**Spec:**
```
Type:       Web application (study space occupancy)
Data model: Space(id, name, building, seats)
            OccupancySnapshot(id, space_id -> Space, people, at)
Features:   - Count people entering and leaving with door sensors
            - Show live occupancy per study space
            - Predict busy times from history
            - Show a campus map coloured by free seats
API:        REST
            GET  /spaces
            GET  /spaces/{id}/forecast
Storage:    PostgreSQL
Tech stack: Xovis sensors, Python, FastAPI, Vue.js
```

---

## Example 325

**Intent:**
lecture hall clicker system for quizzes

**Spec:**
```
Type:       Web application (classroom response system)
Data model: Session(id, lecturer_id, code)
            Question(id, session_id -> Session, text, options)
            Answer(id, question_id -> Question, student_token, option)
Features:   - Create live multiple-choice questions
            - Let students answer from phones
            - Show a live bar chart of answers
            - Export results per session
API:        REST
            POST /sessions
            POST /questions/{id}/answers
            GET  /questions/{id}/results
Storage:    Redis, PostgreSQL
Tech stack: Elixir, Phoenix LiveView
```

---

## Example 326

**Intent:**
need a thing 4 my van so i know the leisure battery % when im camping

**Spec:**
```
Type:       IoT system (campervan battery monitor)
Features:   - Read battery voltage and current with a shunt
            - Calculate state of charge
            - Show percent and hours left on a phone over Bluetooth
            - Alert when below 20 percent
Tech stack: ESP32, INA226 shunt, BLE, Flutter
```

---

## Example 327

**Intent:**
campervan water tank lvl + gas bottle weight

**Spec:**
```
Type:       IoT system (campervan tank monitoring)
Features:   - Measure fresh and grey water levels
            - Weigh the gas bottle with a load cell
            - Show levels on a small screen by the door
            - Send the data to a phone app
Tech stack: ESP32, ultrasonic sensors, HX711, ESPHome
```

---

## Example 328

**Intent:**
tiny house off grid dashboard solar battery water all in 1 screen

**Spec:**
```
Type:       Data dashboard (off-grid home)
Features:   - Collect solar, battery and inverter data
            - Collect water tank and propane levels
            - Show everything on a wall tablet
            - Keep 90 days of history
            - Send alerts for low battery or water
Storage:    InfluxDB
Tech stack: Raspberry Pi, Victron Venus OS, Node-RED, Grafana
```

---

## Example 329

**Intent:**
sailboat instruments to my ipad, wind speed depth etc

**Spec:**
```
Type:       IoT system (NMEA to tablet bridge)
Features:   - Read NMEA 0183 sentences from boat instruments
            - Convert them to NMEA 2000 or JSON
            - Broadcast data over the boat Wi-Fi
            - Show wind, depth and speed in a tablet app
Tech stack: Raspberry Pi, Signal K server, OpenCPN
```

---

## Example 330

**Intent:**
boat battery switch remote, turn off from phone when i leave

**Spec:**
```
Type:       IoT system (remote battery switch)
Features:   - Control a latching battery relay from a phone
            - Show current switch state
            - Prevent switching off while the bilge pump runs
            - Report battery voltage
Tech stack: ESP32, latching relay, LTE modem, Blynk
```

---

## Example 331

**Intent:**
yacht charter checkin checklist inventory photos

**Spec:**
```
Type:       Mobile application with backend (charter check-in)
Data model: Yacht(id, name, base)
            InventoryItem(id, yacht_id -> Yacht, name, qty)
            Checkin(id, yacht_id -> Yacht, charter_ref, type, done_at, signed_by)
            CheckinLine(id, checkin_id -> Checkin, item_id -> InventoryItem, qty_found, photo_url)
Features:   - Walk through the yacht inventory at check-in and check-out
            - Take photos of damage
            - Compare check-out against check-in
            - Get client signature on the tablet
            - Email a PDF report
API:        REST
            POST /checkins
            GET  /yachts/{id}/inventory
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Express
```

---

## Example 332

**Intent:**
sea kayak trip plan sharing so coastguard friend knows when im overdue

**Spec:**
```
Type:       Mobile application with backend (trip plan alerts)
Data model: TripPlan(id, user_id, route, launch_at, return_by, contacts)
            CheckIn(id, plan_id -> TripPlan, lat, lng, at)
Features:   - Create a trip plan with route and return time
            - Share it with emergency contacts
            - Check in during the trip with location
            - Alert contacts automatically if not back by the return time
API:        REST
            POST /plans
            POST /plans/{id}/checkins
            POST /plans/{id}/close
Storage:    PostgreSQL
Tech stack: Flutter, Go, Twilio
```

---

## Example 333

**Intent:**
ferry passenger counter both gangways

**Spec:**
```
Type:       IoT system (ferry passenger counting)
Data model: Sailing(id, route, departs_at)
            PassengerCount(id, sailing_id -> Sailing, boarded, disembarked)
Features:   - Count passengers at each gangway with 3D sensors
            - Stop boarding when the licensed capacity is reached
            - Record counts per sailing
            - Send counts to the port authority
Tech stack: Stereo vision people counters, Raspberry Pi, Python, MQTT
```

---

## Example 334

**Intent:**
lighthouse lamp failure alarm

**Spec:**
```
Type:       IoT system (navigation light monitoring)
Features:   - Monitor lamp current to detect failure
            - Switch to the backup lamp automatically
            - Send an alarm over satellite
            - Report battery and solar status daily
Tech stack: Arduino, current sensor, RockBLOCK, solar charge controller
```

---

## Example 335

**Intent:**
fishing net buoy tracker cuz nets get lost

**Spec:**
```
Type:       IoT system (net buoy tracking)
Features:   - Report buoy GPS every 30 minutes over LoRa
            - Show all buoys on a map in the wheelhouse
            - Alert when a buoy drifts away from its set position
            - Run on battery for a season
Tech stack: LoRa GPS trackers, Raspberry Pi gateway, OpenCPN plugin
```

---

## Example 336

**Intent:**
Marina pump out station usage log + full tank alert

**Spec:**
```
Type:       IoT system (pump-out station)
Features:   - Count pump-out sessions and litres
            - Detect when the holding tank is near full
            - Notify the harbour master
            - Report monthly usage
Tech stack: ESP32, flow meter, level sensor, MQTT
```

---

## Example 337

**Intent:**
airport bird strike log app for wildlife officers

**Spec:**
```
Type:       Mobile application with backend (wildlife hazard log)
Data model: Patrol(id, officer, started_at)
            Sighting(id, patrol_id -> Patrol, species, count, lat, lng, action, at)
            Strike(id, aircraft, species, phase, at)
Features:   - Log bird sightings on runway patrols
            - Record dispersal actions
            - Report bird strikes with aircraft details
            - Show hot spots on an airfield map
            - Export reports for the authority
API:        REST
            POST /sightings
            POST /strikes
            GET  /heatmap
Storage:    PostgreSQL with PostGIS
Tech stack: Flutter, Django, Leaflet
```

---

## Example 338

**Intent:**
runway light failure monitor small airport

**Spec:**
```
Type:       IoT system (airfield lighting monitoring)
Features:   - Monitor current on each lighting circuit
            - Detect failed lamps from current drop
            - Show circuits on an airfield map
            - Alert the duty officer
Tech stack: PLC, current transducers, Node-RED
```

---

## Example 339

**Intent:**
flight school aircraft booking + instructor

**Spec:**
```
Type:       Web application (flight school scheduling)
Data model: Aircraft(id, registration, status)
            Instructor(id, name, ratings)
            Student(id, name, stage)
            Booking(id, aircraft_id -> Aircraft, instructor_id -> Instructor, student_id -> Student, starts_at, ends_at, lesson)
Features:   - Book an aircraft and instructor together
            - Block aircraft under maintenance
            - Check student currency and medical expiry
            - Send weather briefing links before flights
            - Log flight time to the student record
API:        REST
            GET  /availability?date={d}
            POST /bookings
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Prisma
```

---

## Example 340

**Intent:**
pilot logbook from flight sim and real flights

**Spec:**
```
Type:       Desktop application (pilot logbook)
Data model: Entry(id, date, aircraft_type, registration, from_icao, to_icao, total_min, pic_min, night_min, landings, simulated)
Features:   - Log flights with time categories
            - Import flights from a flight simulator log
            - Total hours by category
            - Check currency rules for night and passengers
            - Export to PDF in logbook format
Storage:    SQLite
Tech stack: C#, Avalonia UI
```

---

## Example 341

**Intent:**
atc training voice simulator

**Spec:**
```
Type:       Desktop application (ATC phraseology trainer)
Features:   - Play scenario radio calls from simulated aircraft
            - Recognise the student's spoken clearance
            - Check phraseology against the expected answer
            - Score each response
            - Increase traffic as the student improves
Tech stack: Python, Whisper, PyQt6, pyttsx3
```

---

## Example 342

**Intent:**
helicopter rescue hoist cycle counter

**Spec:**
```
Type:       IoT system (hoist usage monitoring)
Features:   - Count hoist cycles and cable length paid out
            - Record load peaks
            - Warn when cable inspection is due
            - Download data after each mission
Tech stack: STM32, load cell, rotary encoder, USB
```

---

## Example 343

**Intent:**
i work at ambulance station, need app showing which medicine expire soon in each bag

**Spec:**
```
Type:       Web application (drug expiry tracking)
Data model: Bag(id, name, vehicle)
            Drug(id, name)
            Stock(id, bag_id -> Bag, drug_id -> Drug, batch, expires_on, qty)
Features:   - Record drugs in each bag with expiry dates
            - List items expiring in the next 30 days
            - Send a weekly expiry email
            - Record replacements
Storage:    SQLite
Tech stack: Python, Django
```

---

## Example 344

**Intent:**
112 call wait time dashbaord for our center

**Spec:**
```
Type:       Data dashboard (emergency call metrics)
Features:   - Read call events from the telephony system
            - Show calls waiting and longest wait live
            - Show answer times against the 10-second target
            - Show call taker status
            - Show hourly volume compared with last week
Storage:    PostgreSQL
Tech stack: Python, Asterisk AMI, Grafana
```

---

## Example 345

**Intent:**
Radio check for firefighters inside building tracking which floor

**Spec:**
```
Type:       IoT system (firefighter accountability)
Data model: Firefighter(id, name, tag_id)
            Entry(id, firefighter_id -> Firefighter, entered_at, exited_at, air_start_bar)
            FloorSighting(id, firefighter_id -> Firefighter, floor, at)
Features:   - Record entry time and air pressure at the entry point
            - Estimate floor with beacons dropped on stairwells
            - Show who is inside on a command tablet
            - Warn when air time is running out
            - Trigger an evacuation signal to all tags
Tech stack: BLE beacons, ESP32 tags, Android tablet app (Kotlin)
```

---

## Example 346

**Intent:**
firefighter breathing apparatus test records

**Spec:**
```
Type:       Web application (SCBA maintenance)
Data model: Set(id, serial, station)
            Cylinder(id, serial, hydro_due_on)
            Test(id, set_id -> Set, type, result, tested_by, at)
Features:   - Log weekly and annual SCBA tests
            - Track cylinder hydrostatic test dates
            - Take sets out of service on failure
            - Report readiness per station
Storage:    PostgreSQL
Tech stack: PHP, Laravel
```

---

## Example 347

**Intent:**
volunteer search dog training log

**Spec:**
```
Type:       Mobile application (search dog training log)
Data model: Dog(id, name, certification)
            Session(id, dog_id -> Dog, type, area, duration_min, find_success, track_gpx, at)
Features:   - Log training sessions with type and result
            - Record GPS tracks of the dog and handler
            - Track hours toward certification
            - Share logs with the team trainer
Storage:    Firebase
Tech stack: Flutter, geolocator, Firebase
```

---

## Example 348

**Intent:**
river rescue throw bag inspection QR

**Spec:**
```
Type:       Web application (rescue equipment register)
Data model: Station(id, location, lat, lng)
            Inspection(id, station_id -> Station, bag_present, rope_ok, sign_ok, inspected_at, by)
Features:   - Scan a QR code at each riverside station
            - Report missing or damaged equipment
            - Show stations on a map with last inspection
            - Alert the council when equipment is missing
API:        REST
            POST /stations/{id}/inspections
Storage:    PostgreSQL
Tech stack: Python, Flask, Leaflet
```

---

## Example 349

**Intent:**
refugee camp water point usage

**Spec:**
```
Type:       IoT system (water point monitoring)
Data model: WaterPoint(id, block, lat, lng)
            FlowLog(id, point_id -> WaterPoint, litres, hour)
Features:   - Measure litres dispensed at each tap stand
            - Send hourly totals over GSM
            - Detect broken taps from zero flow
            - Report litres per person per day per block
Storage:    PostgreSQL
Tech stack: Arduino, flow meters, SIM800, Python, Metabase
```

---

## Example 350

**Intent:**
food distribution at camp with ration cards qr

**Spec:**
```
Type:       Mobile application with backend (aid distribution)
Data model: Household(id, card_qr, size, block)
            Distribution(id, name, date)
            Collection(id, household_id -> Household, distribution_id -> Distribution, items_json, collected_at)
Features:   - Scan household ration cards
            - Show the entitlement by household size
            - Prevent double collection
            - Work offline and sync later
            - Report coverage per block
API:        REST
            POST /collections/sync
            GET  /distributions/{id}/coverage
Storage:    PostgreSQL, SQLite on device
Tech stack: Kotlin, Android, Django
```

---

## Example 351

**Intent:**
Family tracing for separated refugees, match missing persons reports

**Spec:**
```
Type:       Web application (family tracing)
Data model: Report(id, reporter_name, sought_name, sought_age, last_seen_place, last_seen_on)
            Person(id, name, age, location)
            Match(id, report_id -> Report, person_id -> Person, score, confirmed)
Features:   - Register missing person reports
            - Register people found or in camps
            - Suggest matches with fuzzy name matching
            - Let caseworkers confirm matches
            - Protect data with strict access logs
Storage:    PostgreSQL
Tech stack: Python, Django, RapidFuzz
```

---

## Example 352

**Intent:**
interpreter on demand phone line for clinic, patient choose language with keypad

**Spec:**
```
Type:       Webhook service (interpreter phone routing)
Data model: Language(id, name, keypad_digit)
            Interpreter(id, name, phone, language_id -> Language, available)
            CallLog(id, language_id -> Language, interpreter_id -> Interpreter, started_at, duration_s)
Features:   - Answer calls with a multilingual voice menu
            - Route the call to an available interpreter for the chosen language
            - Try the next interpreter if no answer
            - Log call minutes for billing
API:        REST
            POST /voice/incoming
            POST /voice/language-selected
Storage:    PostgreSQL
Tech stack: Node.js, Express, Twilio Voice
```

---

## Example 353

**Intent:**
prison yard headcount with cameras

**Spec:**
```
Type:       Machine learning model (crowd headcount)
Features:   - Detect people in each frame
            - Count heads per zone
            - Compare with the expected count
            - Alert officers on mismatch
Tech stack: Python, YOLOv8, OpenCV
```

---

## Example 354

**Intent:**
inmate property storage tracking with bins

**Spec:**
```
Type:       Web application (inmate property)
Data model: Inmate(id, number)
            Bin(id, code, shelf)
            PropertyItem(id, inmate_id -> Inmate, bin_id -> Bin, description, photo_url, logged_at)
Features:   - Log property at intake with photos
            - Assign items to storage bins
            - Release property at discharge with signature
            - Search by inmate number
Storage:    PostgreSQL
Tech stack: Java, Spring Boot, React
```

---

## Example 355

**Intent:**
video visit tablets for jail

**Spec:**
```
Type:       Web application (video visitation)
Data model: Visitor(id, name, verified)
            VisitSlot(id, starts_at, kiosk)
            VideoVisit(id, slot_id -> VisitSlot, inmate_id, visitor_id -> Visitor, status, recording_path)
Features:   - Book video visit slots
            - Connect visitors at home to unit kiosks
            - Record visits for security review
            - End calls at the scheduled time
            - Let staff monitor live
API:        REST
            POST /visits
            GET  /visits/{id}/join-token
Storage:    PostgreSQL, S3
Tech stack: Node.js, WebRTC (Janus), React
```

---

## Example 356

**Intent:**
graveyard plot reservation online, with payment

**Spec:**
```
Type:       Web application (plot reservations)
Data model: Plot(id, section, number, price, status)
            Reservation(id, plot_id -> Plot, customer_id, paid, reserved_at)
Features:   - Show available plots on a map
            - Reserve and pay online
            - Issue a deed certificate PDF
            - Let admins release unpaid reservations
API:        REST
            GET  /plots?status=available
            POST /reservations
Storage:    PostgreSQL
Tech stack: Laravel, Stripe, Leaflet
```

---

## Example 357

**Intent:**
crematorium cremation scheduling and ashes tracking

**Spec:**
```
Type:       Web application (cremation tracking)
Data model: Case(id, deceased_name, funeral_home, received_at)
            Cremation(id, case_id -> Case, retort, scheduled_at, completed_at)
            Urn(id, case_id -> Case, tag_no, released_to, released_at)
Features:   - Schedule cremations per retort
            - Track identity tags through each step
            - Record release of remains with signatures
            - Show the daily schedule
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core
```

---

## Example 358

**Intent:**
war graves volunteer photo project

**Spec:**
```
Type:       Web application (war memorial records)
Data model: Soldier(id, name, unit, death_date)
            Grave(id, soldier_id -> Soldier, cemetery, lat, lng)
            Photo(id, grave_id -> Grave, url, taken_on, volunteer)
Features:   - Import soldier records from archives
            - Let volunteers upload grave photos
            - Show graves on a map
            - Let relatives search and request photos
Storage:    PostgreSQL, S3
Tech stack: Python, Django, Leaflet
```

---

## Example 359

**Intent:**
obituary page generator from funeral home form

**Spec:**
```
Type:       Web application (obituary pages)
Data model: Obituary(id, name, birth_date, death_date, text, photo_url, service_info)
            Condolence(id, obituary_id -> Obituary, author, message, approved)
Features:   - Create an obituary page from a form
            - Show service time and place
            - Let visitors leave condolences
            - Moderate condolences before showing
API:        REST
            POST /obituaries
            POST /obituaries/{id}/condolences
Storage:    PostgreSQL
Tech stack: Next.js, Prisma
```

---

## Example 360

**Intent:**
lab sample freezer -80 inventory racks boxes

**Spec:**
```
Type:       Web application (biobank inventory)
Data model: Freezer(id, name)
            Rack(id, freezer_id -> Freezer, position)
            Box(id, rack_id -> Rack, label)
            Sample(id, box_id -> Box, position, sample_type, donor_code, stored_on)
Features:   - Map freezers, racks, boxes and positions
            - Scan 2D barcodes on tubes
            - Find a sample's exact position
            - Record withdrawals
            - Alert on freezer temperature from a sensor
Storage:    PostgreSQL
Tech stack: Django, ZXing barcode scanning
```

---

## Example 361

**Intent:**
liquid nitrogen dewar level alarm

**Spec:**
```
Type:       IoT system (LN2 level alarm)
Features:   - Weigh the dewar with a load cell
            - Estimate level and boil-off rate
            - Alert when the level is low
            - Log weights for refill planning
Tech stack: ESP32, load cell, HX711, Slack webhook
```

---

## Example 362

**Intent:**
data logger for horse trailer, temp and if horse falls

**Spec:**
```
Type:       IoT system (horse trailer monitor)
Features:   - Read trailer temperature and humidity
            - Detect hard braking and unusual motion
            - Stream a camera view to the tow vehicle
            - Alert the driver on the phone
Tech stack: Raspberry Pi, camera, MPU-6050, Wi-Fi hotspot, Flutter
```

---

## Example 363

**Intent:**
Racing pigeon arrival clock

**Spec:**
```
Type:       IoT system (pigeon race timing)
Data model: Bird(id, ring_no, rfid_uid)
            Race(id, release_point, released_at)
            Arrival(id, race_id -> Race, bird_id -> Bird, arrived_at, velocity_mpm)
Features:   - Detect bird rings at the loft entrance
            - Record arrival times to the second
            - Calculate velocity from release distance
            - Upload results to the club
Storage:    SQLite
Tech stack: Arduino, RFID antenna mat, Python
```

---

## Example 364

**Intent:**
bat box occupancy counter

**Spec:**
```
Type:       IoT system (bat box counter)
Features:   - Count bats leaving and entering with IR beams
            - Log counts per night
            - Upload data weekly
            - Chart emergence times
Tech stack: Arduino, IR beam sensors, SD card, LoRa
```

---

## Example 365

**Intent:**
hedgehog house camera and visit counts

**Spec:**
```
Type:       IoT system (wildlife feeding station)
Features:   - Trigger an IR camera on motion
            - Save clips with timestamp
            - Count visits per night
            - Weigh the hedgehog with a platform scale
Tech stack: Raspberry Pi, NoIR camera, HX711 scale, motionEye
```

---

## Example 366

**Intent:**
So I run a tiny bakery and twice now our walk-in fridge died over a weekend and we lost everything, like hundreds of dollars of butter and cream. I'm not techy at all but my nephew can install stuff. I just want my phone to scream at me if it gets warm, and ideally a record I can show insurance.

**Spec:**
```
Type:       IoT system (fridge failure alert)
Data model: Reading(id, temp_c, recorded_at)
            Alert(id, kind, sent_at, acknowledged_at)
Features:   - Measure the walk-in temperature every minute with a wireless probe
            - Call and text the owner when it stays above 5 °C for 15 minutes
            - Keep calling until the alert is acknowledged
            - Send a power failure alert using a battery-backed hub
            - Export a temperature history PDF for insurance claims
Storage:    SQLite
Tech stack: Raspberry Pi, Govee Bluetooth thermometer, Python, Twilio Voice
```

---

## Example 367

**Intent:**
I'm the facilities person at a small museum-sized church, no wait, it's a historic house, and the old timber floors crack when humidity drops in winter. We have 12 rooms. I'd like sensors in each room and something that tells me which humidifier to refill and shows the history for the conservator.

**Spec:**
```
Type:       IoT system (historic house climate)
Data model: Room(id, name, floor)
            ClimateReading(id, room_id -> Room, temp_c, rh_pct, recorded_at)
            Humidifier(id, room_id -> Room, tank_low, last_refilled_at)
Features:   - Record temperature and humidity in all 12 rooms every 15 minutes
            - Show rooms outside 45 to 55 percent RH
            - Detect humidifiers with an empty tank from a float switch
            - Send a daily refill list to the facilities phone
            - Export monthly charts for the conservator
API:        REST
            GET  /rooms
            GET  /rooms/{id}/history
            GET  /humidifiers/refill-list
Storage:    InfluxDB
Tech stack: Zigbee climate sensors, ESP32 tank sensors, Home Assistant, Grafana
```

---

## Example 368

**Intent:**
My dad has an old tractor and a field 20 minutes from the house. Sometimes he forgets the electric fence is off or it shorts out on wet grass and the cows get out. Can we make something that checks the fence voltage and messages him?

**Spec:**
```
Type:       IoT system (electric fence monitor)
Features:   - Measure fence pulse voltage with a divider probe
            - Send the voltage every 15 minutes over LoRaWAN
            - Alert by SMS when the voltage drops below 4 kV
            - Alert when the energiser stops pulsing
            - Show a 7-day voltage chart
Tech stack: Arduino MKR WAN 1310, The Things Network, Node-RED, Twilio
```

---

## Example 369

**Intent:**
our makerspace has laser cutter, cnc, and lathe and only trained members can use them. I want badge readers that only switch the machine on for people who did the training, and log usage for billing

**Spec:**
```
Type:       IoT system (machine access control)
Data model: Member(id, name, badge_uid, balance)
            Machine(id, name, hourly_rate)
            Training(id, member_id -> Member, machine_id -> Machine, passed_on)
            Session(id, member_id -> Member, machine_id -> Machine, started_at, ended_at, cost)
Features:   - Read a member badge at each machine
            - Switch power on only for trained members
            - Record session time and charge the member
            - Let trainers mark training as passed
            - Show machine usage and revenue per month
API:        REST
            POST /machines/{id}/authorize
            POST /sessions/{id}/end
            GET  /reports/usage
Storage:    PostgreSQL
Tech stack: ESP32 with RC522 reader, contactor relays, Python, Django
```

---

## Example 370

**Intent:**
im a beekeeper with 40 hives spread over 5 farms and I lose track of which hive got which treatment and when I last saw the queen. paper notes get wet. something on my phone that works without signal in the fields

**Spec:**
```
Type:       Mobile application (apiary inspection records)
Data model: Yard(id, name, lat, lng)
            Hive(id, yard_id -> Yard, label, qr_code)
            Inspection(id, hive_id -> Hive, queen_seen, brood_frames, temper, notes, inspected_at)
            Treatment(id, hive_id -> Hive, product, dose, applied_on, withdrawal_ends_on)
Features:   - Scan a QR label on the hive to open its record
            - Record inspections with queen seen, brood and temper
            - Log mite treatments with withdrawal dates
            - Work fully offline and sync when back in signal
            - Show hives overdue for inspection by yard
Storage:    Local SQLite with cloud sync (Supabase)
Tech stack: Flutter, drift, Supabase
```

---

## Example 371

**Intent:**
we're a small airline ground handling team, every turnaround we have to do like 30 steps (fuel, catering, baggage, doors) and right now it's on clipboards. Want a tablet app that times each step and shows delays to ops

**Spec:**
```
Type:       Mobile application with backend (aircraft turnaround tracking)
Data model: Flight(id, number, registration, sta, std)
            Turnaround(id, flight_id -> Flight, stand)
            StepTemplate(id, name, planned_offset_min)
            Step(id, turnaround_id -> Turnaround, template_id -> StepTemplate, started_at, ended_at, delay_code)
Features:   - Show the turnaround steps for each flight on a tablet
            - Record start and end of each step with one tap
            - Highlight steps running late against plan
            - Require a delay code for late steps
            - Show all active turnarounds live to the ops room
API:        REST
            GET  /turnarounds?date={d}
            PATCH /steps/{id}
            GET  /ops/live
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI, WebSockets
```

---

## Example 372

**Intent:**
hi, we are small factory in Vietnam make furniture, I want screen in office show each machine is running or stop now, and why stop

**Spec:**
```
Type:       Data dashboard (machine status board)
Data model: Machine(id, name, line)
            StatusEvent(id, machine_id -> Machine, status, reason, at)
Features:   - Detect running or stopped from machine current sensors
            - Let operators choose a stop reason on a tablet
            - Show all machines with live status and stop time
            - Show stop reasons per day
            - Show the board in Vietnamese and English
API:        REST
            GET  /machines/status
            POST /machines/{id}/stop-reason
Storage:    PostgreSQL
Tech stack: ESP32, current transformers, MQTT, Node.js, React
```

---

## Example 373

**Intent:**
we are cooperative of coffee farmers in Peru, we want to measure moisture of coffee beans when drying and send to the buyer, my english not good sorry

**Spec:**
```
Type:       Mobile application with backend (coffee drying records)
Data model: Farmer(id, name, village)
            Lot(id, farmer_id -> Farmer, variety, kg, harvested_on)
            MoistureReading(id, lot_id -> Lot, moisture_pct, measured_at)
Features:   - Register coffee lots per farmer
            - Read bean moisture from a Bluetooth meter
            - Show when a lot reaches 11 percent and is ready
            - Share lot drying records with buyers
            - Show the app in Spanish and English
API:        REST
            POST /lots
            POST /lots/{id}/readings
            GET  /lots/{id}/report
Storage:    PostgreSQL
Tech stack: Flutter, flutter_blue_plus, Django REST Framework
```

---

## Example 374

**Intent:**
Our hospital in Nigeria have oxygen concentrators in many wards, we need to know if they are working and hours used, power is not stable

**Spec:**
```
Type:       IoT system (oxygen concentrator monitoring)
Data model: Ward(id, name)
            Concentrator(id, ward_id -> Ward, serial)
            Reading(id, concentrator_id -> Concentrator, flow_lpm, purity_pct, power_on, recorded_at)
Features:   - Measure oxygen flow and purity at each concentrator
            - Count run hours for maintenance
            - Detect power cuts and log them
            - Alert the biomedical engineer on low purity
            - Buffer data locally when the network is down
Storage:    PostgreSQL
Tech stack: ESP32, oxygen sensor, flow sensor, SIM800 GSM, Python
```

---

## Example 375

**Intent:**
we have small clinic in rural India, we want record of baby weight and vaccine and send reminder SMS to mothers in Hindi

**Spec:**
```
Type:       Web application (child health records)
Data model: Mother(id, name, phone, village)
            Child(id, mother_id -> Mother, name, birth_date)
            Weight(id, child_id -> Child, kg, measured_on)
            Vaccination(id, child_id -> Child, vaccine, due_on, given_on)
Features:   - Register mothers and babies
            - Record weights and plot growth charts
            - Calculate vaccine due dates from the national schedule
            - Send SMS reminders in Hindi before due dates
            - Work on low bandwidth connections
API:        REST
            POST /children
            POST /children/{id}/weights
            GET  /vaccinations/due
Storage:    PostgreSQL
Tech stack: Python, Django, MSG91 SMS API
```

---

## Example 376

**Intent:**
in our village in Nepal we have micro hydro power, I want measure the power and the frequency and the money each house pay

**Spec:**
```
Type:       IoT system (micro-hydro monitoring)
Data model: House(id, owner, meter_id)
            MeterReading(id, house_id -> House, kwh, recorded_at)
            PlantReading(id, frequency_hz, voltage, power_kw, recorded_at)
            Bill(id, house_id -> House, month, amount, paid)
Features:   - Measure plant output, voltage and frequency
            - Read energy meters for each house
            - Calculate monthly bills
            - Record payments
            - Alert the operator when frequency is unstable
API:        REST
            GET  /plant/status
            GET  /houses/{id}/bills
Storage:    SQLite
Tech stack: PZEM-004T meters, ESP32, Python, Flask
```

---

## Example 377

**Intent:**
Is possible to make app for my parking garage that read car plate and open the gate for monthly customers? We are in Brazil.

**Spec:**
```
Type:       IoT system (plate recognition gate)
Data model: Customer(id, name, plate, plan_until)
            GateEvent(id, plate, image_path, allowed, at)
Features:   - Read license plates from a camera at the gate
            - Open the gate for customers with an active plan
            - Print a ticket for visitors
            - Log every entry and exit with photo
            - Show the interface in Portuguese
API:        REST
            POST /events
            GET  /customers?plate={p}
Storage:    PostgreSQL
Tech stack: Python, OpenALPR, Raspberry Pi, relay, Django
```

---

## Example 378

**Intent:**
kindergarden in Germany, we want sign in kids when parents bring them by tablet and know who is still inside if fire

**Spec:**
```
Type:       Web application (kindergarten sign-in)
Data model: Child(id, name, group)
            Guardian(id, child_id -> Child, name, photo_url)
            Presence(id, child_id -> Child, arrived_at, left_at, dropped_by)
Features:   - Let parents tap their child's photo to sign in and out
            - Record who picked the child up
            - Show children present per group
            - Print or show an evacuation list instantly
            - Show the app in German and English
API:        REST
            POST /presence
            GET  /presence/now
Storage:    PostgreSQL
Tech stack: Vue.js, Laravel
```

---

## Example 379

**Intent:**
my factory in Turkey, i want count products on conveyor and show per hour vs target on big screen

**Spec:**
```
Type:       IoT system (production counter)
Data model: Line(id, name, target_per_hour)
            Count(id, line_id -> Line, hour, quantity)
Features:   - Count products with a photoelectric sensor
            - Show actual vs target per hour on a big screen
            - Colour the screen red when behind target
            - Store counts per shift
            - Export daily totals
Storage:    SQLite
Tech stack: Arduino, photoelectric sensor, Raspberry Pi, Python, Flask
```

---

## Example 380

**Intent:**
we are school in Kenya, the bell is ring by hand, we want automatic bell but electricity go off sometimes

**Spec:**
```
Type:       IoT system (battery-backed school bell)
Features:   - Ring the bell on the school timetable
            - Keep time with a battery-backed clock
            - Keep working on battery during power cuts
            - Let the head teacher change times with buttons and a display
            - Ring a special pattern for assembly
Tech stack: Arduino Uno, DS3231 RTC, relay, LCD keypad shield
```

---

## Example 381

**Intent:**
Bee hive scale cheap

**Spec:**
```
Type:       IoT system (hive scale)
Features:   - Weigh the hive daily with four load cells
            - Send weight over Wi-Fi
            - Show a weight chart
Tech stack: ESP8266, HX711, ThingSpeak
```

---

## Example 382

**Intent:**
egg counter conveyor

**Spec:**
```
Type:       IoT system (egg counting)
Features:   - Count eggs on the collection conveyor with a sensor
            - Total eggs per house per day
            - Compare with the flock size to get lay rate
            - Show counts on a phone
Tech stack: ESP32, IR sensors, MQTT, Grafana
```

---

## Example 383

**Intent:**
tractor engine hours log

**Spec:**
```
Type:       Mobile application (machinery hours log)
Data model: Machine(id, name, service_interval_h)
            HoursEntry(id, machine_id -> Machine, hours, logged_on)
            Service(id, machine_id -> Machine, at_hours, notes)
Features:   - Log engine hours per machine
            - Warn when service is due
            - Record services done
            - Show history per machine
Storage:    Local SQLite
Tech stack: React Native, Expo
```

---

## Example 384

**Intent:**
cow heat detection with neck collar

**Spec:**
```
Type:       IoT system (oestrus detection)
Data model: Cow(id, ear_tag, collar_id)
            ActivityReading(id, cow_id -> Cow, steps, rumination_min, hour)
            HeatAlert(id, cow_id -> Cow, detected_at)
Features:   - Measure activity and rumination with a collar accelerometer
            - Compare activity with each cow's baseline
            - Detect heat when activity rises sharply
            - Alert the farmer with the best insemination window
            - Show a herd list sorted by alert
Storage:    PostgreSQL
Tech stack: LoRaWAN collars, Python, scikit-learn, React
```

---

## Example 385

**Intent:**
calving camera alert

**Spec:**
```
Type:       IoT system (calving detection)
Features:   - Stream video from the calving pen
            - Detect a cow lying with straining posture using a model
            - Send an alert with a snapshot
            - Let the farmer watch live from the phone
Tech stack: Raspberry Pi 5, IP camera, YOLOv8 pose, Frigate, Home Assistant
```

---

## Example 386

**Intent:**
pig barn ventilation alarm

**Spec:**
```
Type:       IoT system (barn ventilation alarm)
Features:   - Monitor barn temperature and fan status
            - Detect power failure
            - Call the farmer by phone on alarm
            - Repeat calls until acknowledged with a keypress
Tech stack: Arduino, SIM800L, temperature sensors, relay inputs
```

---

## Example 387

**Intent:**
fish tank water change reminder

**Spec:**
```
Type:       Mobile application (aquarium care reminders)
Data model: Tank(id, name, litres)
            Task(id, tank_id -> Tank, type, every_days, last_done_on)
Features:   - Add tanks and care tasks
            - Remind when water changes or filter cleaning are due
            - Log tasks done
            - Show history
Storage:    Local storage
Tech stack: Flutter, flutter_local_notifications
```

---

## Example 388

**Intent:**
hydroponic tower pump cycle timer

**Spec:**
```
Type:       IoT system (tower pump timer)
Features:   - Run the pump 15 minutes on, 45 off
            - Change the cycle from a phone
            - Check flow with a flow sensor
            - Alert when the pump runs dry
Tech stack: ESP32, flow sensor, relay, Blynk
```

---

## Example 389

**Intent:**
Mobile app for farmers to scan disease on cassava leaves offline

**Spec:**
```
Type:       Mobile application (crop disease detection)
Data model: Scan(id, image_path, disease, confidence, lat, lng, scanned_at)
Features:   - Take a photo of a cassava leaf
            - Classify the disease on the device without internet
            - Show treatment advice
            - Save scans with location
            - Upload scans when online for extension officers
Storage:    Local SQLite
Tech stack: Kotlin, TensorFlow Lite, MobileNetV3
```

---

## Example 390

**Intent:**
Train a model that detects varroa mites on bee photos

**Spec:**
```
Type:       Machine learning model (varroa detection)
Features:   - Split the dataset into train, validation and test sets
            - Train an object detection model for mites
            - Report precision and recall
            - Estimate infestation rate per hive
            - Export to ONNX for an edge camera
Tech stack: Python, Ultralytics YOLOv8, PyTorch, ONNX
```

---

## Example 391

**Intent:**
predict chiller failures from bms data

**Spec:**
```
Type:       Machine learning model (chiller anomaly detection)
Features:   - Resample trends to 5-minute intervals
            - Train an isolation forest on normal operation
            - Score live data for anomalies
            - Explain which signals drove each anomaly
            - Push alerts to the maintenance system
Tech stack: Python, pandas, scikit-learn, SHAP
```

---

## Example 392

**Intent:**
anomaly detection on bridge strain gauges

**Spec:**
```
Type:       Data analysis script (structural monitoring)
Features:   - Remove temperature effects from strain readings
            - Detect sudden shifts and drift per gauge
            - Compare with traffic load
            - Plot flagged periods
            - Write a monthly summary for the engineers
Tech stack: Python, pandas, statsmodels, matplotlib
```

---

## Example 393

**Intent:**
lightning strike counter on our tower

**Spec:**
```
Type:       IoT system (lightning detection)
Features:   - Detect lightning with an AS3935 sensor
            - Estimate storm distance
            - Count strikes per storm
            - Send a warning when a storm is within 10 km
Tech stack: ESP32, AS3935 sensor, MQTT, Home Assistant
```

---

## Example 394

**Intent:**
earthquake early warning for my house using phone accelerometer network

**Spec:**
```
Type:       Mobile application with backend (crowd-sourced quake alerts)
Data model: Device(id, lat, lng, last_seen_at)
            Trigger(id, device_id -> Device, peak_g, at)
            Alert(id, lat, lng, magnitude_est, issued_at)
Features:   - Detect shaking on phones while charging and still
            - Send triggers to the server
            - Confirm a quake when many nearby phones trigger
            - Push alerts to phones further away
            - Show recent events on a map
API:        REST
            POST /triggers
            GET  /alerts/recent
Storage:    PostgreSQL with PostGIS
Tech stack: Kotlin, Go, Firebase Cloud Messaging
```

---

## Example 395

**Intent:**
tsunami siren test logs for coast

**Spec:**
```
Type:       Web application (siren test records)
Data model: Siren(id, name, lat, lng)
            Test(id, siren_id -> Siren, audible, battery_ok, tester, at)
Features:   - Record siren tests by observers
            - Show failing sirens on a map
            - Schedule monthly tests
            - Report results to the province
Storage:    PostgreSQL
Tech stack: Python, Django, Leaflet
```

---

## Example 396

**Intent:**
snowplow gps so residents see which streets are plowed

**Spec:**
```
Type:       Web application (plow tracker)
Data model: Plow(id, unit_no)
            Position(id, plow_id -> Plow, lat, lng, blade_down, at)
            Street(id, name, geometry, last_plowed_at)
Features:   - Receive plow GPS and blade state
            - Match positions to streets
            - Mark streets plowed with time
            - Show a public map with plowed streets
            - Show plows live to dispatch
API:        REST
            GET  /streets?plowed_since={t}
            GET  /plows/live
Storage:    PostgreSQL with PostGIS
Tech stack: Go, PostGIS, MapLibre GL
```

---

## Example 397

**Intent:**
road salt spreader tracking per truck

**Spec:**
```
Type:       Data pipeline (spreader data)
Features:   - Collect spread rate and GPS from spreader controllers
            - Calculate tonnes of salt per route
            - Detect overspreading
            - Load results into the depot reporting database
Storage:    PostgreSQL
Tech stack: Python, Apache Airflow, pandas
```

---

## Example 398

**Intent:**
street light outage reporting with qr on poles

**Spec:**
```
Type:       Web application (street light reporting)
Data model: Pole(id, code, lat, lng)
            Report(id, pole_id -> Pole, issue, photo_url, reported_at, fixed_at)
Features:   - Let residents scan the pole QR code to report a fault
            - Attach a photo
            - Notify the maintenance crew
            - Show fixed status to the reporter
API:        REST
            POST /poles/{code}/reports
            PATCH /reports/{id}
Storage:    PostgreSQL
Tech stack: SvelteKit, Supabase
```

---

## Example 399

**Intent:**
Bridge opening schedule for boaters and drivers

**Spec:**
```
Type:       Web application (bridge opening notices)
Data model: Bridge(id, name)
            Opening(id, bridge_id -> Bridge, starts_at, ends_at, vessel)
Features:   - Let operators log scheduled and actual openings
            - Show the next opening for each bridge
            - Push notifications to subscribers
            - Publish an API for navigation apps
API:        REST
            GET  /bridges/{id}/openings
            POST /openings
Storage:    PostgreSQL
Tech stack: Node.js, Fastify, Web Push
```

---

## Example 400

**Intent:**
level crossing barrier fault log railway

**Spec:**
```
Type:       IoT system (level crossing monitoring)
Features:   - Monitor barrier position and lamp current
            - Detect barrier timeouts
            - Report faults to the signal center
            - Keep event logs for incident investigation
Tech stack: Industrial PLC, MQTT, InfluxDB, Grafana
```

---

## Example 401

**Intent:**
train delay telegram for my commute

**Spec:**
```
Type:       Bot (train delay alerts)
Features:   - Watch my usual trains on weekday mornings
            - Message me when a train is delayed or cancelled
            - Suggest the next alternative train
            - Pause alerts on holidays
Tech stack: Python, python-telegram-bot, national rail open data API
```

---

## Example 402

**Intent:**
tram stop arrival display raspberry pi at home

**Spec:**
```
Type:       IoT system (transit arrival display)
Features:   - Fetch real-time arrivals for my stop from GTFS-RT
            - Show the next three trams on an e-ink display
            - Refresh every 30 seconds
            - Show service alerts
Tech stack: Raspberry Pi Zero, Waveshare e-paper, Python, gtfs-realtime-bindings
```

---

## Example 403

**Intent:**
bus stop shelter solar light and usage counter

**Spec:**
```
Type:       IoT system (bus shelter lighting)
Features:   - Switch shelter lights on at dusk from a light sensor
            - Brighten lights when someone is detected
            - Count waiting passengers per hour
            - Report battery health to the transit office
Tech stack: ESP32, PIR sensor, LDR, LoRaWAN
```

---

## Example 404

**Intent:**
scooter sharing battery swap route

**Spec:**
```
Type:       Web application (battery swap planning)
Data model: Scooter(id, code, battery_pct, lat, lng, updated_at)
            SwapTask(id, scooter_id -> Scooter, assigned_to, done_at)
Features:   - Show scooters with low battery on a map
            - Plan an efficient swap route for each van
            - Assign tasks to swappers
            - Mark swaps done from a phone
API:        REST
            GET  /scooters?battery_lt=20
            POST /routes/plan
            PATCH /tasks/{id}
Storage:    PostgreSQL with PostGIS
Tech stack: Python, FastAPI, OR-Tools, Mapbox GL JS
```

---

## Example 405

**Intent:**
bike shed with smart lock for apartment, residents open with phone

**Spec:**
```
Type:       Mobile application with backend (bike room access)
Data model: Resident(id, name, unit, approved)
            AccessLog(id, resident_id -> Resident, opened_at)
Features:   - Unlock the bike room door from the app over Bluetooth
            - Let the building manager approve residents
            - Log every opening
            - Revoke access when residents move out
API:        REST
            POST /unlock-token
            GET  /access-log
Storage:    PostgreSQL
Tech stack: React Native, Supabase, ESP32 BLE lock controller
```

---

## Example 406

**Intent:**
bike trainer smart fan speed follows my heart rate

**Spec:**
```
Type:       IoT system (heart-rate fan)
Features:   - Read heart rate from a Bluetooth strap
            - Map heart rate zones to fan speeds
            - Drive the fan through a PWM controller
            - Turn the fan off after the workout ends
Tech stack: ESP32, BLE heart rate profile, PWM fan driver
```

---

## Example 407

**Intent:**
velodrome lap timing

**Spec:**
```
Type:       IoT system (track cycling timing)
Features:   - Detect riders with transponders at the finish line
            - Record laps and split times
            - Show live times on the infield screen
            - Export results per event
Storage:    SQLite
Tech stack: MyLaps-compatible decoder, Python, Flask
```

---

## Example 408

**Intent:**
horse race photo finish camera software

**Spec:**
```
Type:       Desktop application (photo finish)
Features:   - Capture a line-scan image at the finish line
            - Show the composite image with a time scale
            - Let the judge place a cursor on each nose
            - Print the official finish order
Tech stack: C++, Qt, line-scan camera SDK
```

---

## Example 409

**Intent:**
dog agility course timer with photocells

**Spec:**
```
Type:       IoT system (agility timing)
Data model: Run(id, dog_name, handler, class, time_s, faults, run_at)
Features:   - Start the timer when the dog breaks the start beam
            - Stop it at the finish beam
            - Let the judge add faults
            - Show results ranked by class on a screen
Storage:    SQLite
Tech stack: Arduino, photocell sensors, Raspberry Pi, Python
```

---

## Example 410

**Intent:**
show jumping scoreboard

**Spec:**
```
Type:       Web application (equestrian scoreboard)
Data model: Class(id, name, time_allowed_s)
            Entry(id, class_id -> Class, rider, horse, faults, time_s, place)
Features:   - Enter faults and times for each round
            - Add time faults automatically
            - Rank riders with jump-off results
            - Show the scoreboard on a screen and online
API:        REST
            POST /entries/{id}/round
            GET  /classes/{id}/results
Storage:    PostgreSQL
Tech stack: Node.js, Socket.IO, Vue.js
```

---

## Example 411

**Intent:**
bocce league scores

**Spec:**
```
Type:       Web application (bocce league)
Data model: Team(id, name)
            Game(id, home_id -> Team, away_id -> Team, home_score, away_score, played_on)
Features:   - Schedule games for the season
            - Enter scores
            - Show standings
            - Show each team's results
Storage:    SQLite
Tech stack: Python, Flask
```

---

## Example 412

**Intent:**
smart scale for climbing chalk... no wait, for our hangboard to measure finger strength

**Spec:**
```
Type:       IoT system (hangboard force gauge)
Features:   - Measure pulling force with a load cell under the hangboard
            - Show live force on a phone
            - Record max force and repeaters workouts
            - Chart finger strength over months
Tech stack: ESP32, crane scale load cell, HX711, BLE, Flutter
```

---

## Example 413

**Intent:**
ski wax room temperature + snow temperature for race team

**Spec:**
```
Type:       Mobile application (ski wax log)
Data model: Session(id, location, snow_temp_c, air_temp_c, humidity_pct, snow_type, at)
            WaxChoice(id, session_id -> Session, wax, result_rating)
Features:   - Read snow and air temperature from a Bluetooth probe
            - Record snow type and conditions
            - Log wax choices and test results
            - Suggest waxes from past similar conditions
Storage:    Local SQLite
Tech stack: Kotlin, Android BLE
```

---

## Example 414

**Intent:**
kitesurf spot wind alert

**Spec:**
```
Type:       Scheduled script (wind alert)
Features:   - Check the wind forecast for my spots every 3 hours
            - Find windows of 15 to 25 knots from the right direction
            - Send me an email with the best windows
            - Skip nights
Tech stack: Python, Open-Meteo API, smtplib, cron
```

---

## Example 415

**Intent:**
surf cam crowd counter

**Spec:**
```
Type:       Machine learning model (surfer counting)
Features:   - Detect surfers in the water
            - Count surfers per frame
            - Smooth counts over 10 minutes
            - Publish crowd level to a web page
Tech stack: Python, YOLOv8, OpenCV, Flask
```

---

## Example 416

**Intent:**
pool lifeguard drowning detection with underwater camera

**Spec:**
```
Type:       Machine learning model (drowning risk detection)
Features:   - Track swimmers between frames
            - Detect a swimmer motionless near the bottom
            - Raise an alarm on the lifeguard smartwatch after 10 seconds
            - Save clips for review
Tech stack: Python, PyTorch, ByteTrack, OpenCV
```

---

## Example 417

**Intent:**
hotel minibar sensor billing

**Spec:**
```
Type:       IoT system (minibar sensing)
Data model: Room(id, number)
            Slot(id, room_id -> Room, product, price)
            Removal(id, slot_id -> Slot, removed_at, billed)
Features:   - Detect items removed with weight sensors per slot
            - Ignore items put back within 60 seconds
            - Post charges to the hotel PMS
            - Create a restock list per floor
Storage:    PostgreSQL
Tech stack: ESP32, load cells, MQTT, Python, Opera PMS API
```

---

## Example 418

**Intent:**
hotel housekeeping room status from door sensors and do not disturb button

**Spec:**
```
Type:       IoT system (room status for housekeeping)
Features:   - Read do not disturb and make up room buttons
            - Detect guest presence with a door and motion sensor
            - Show room status to housekeeping on a tablet
            - Log cleaning time per room
Tech stack: Zigbee buttons and sensors, Home Assistant, Node-RED, React
```

---

## Example 419

**Intent:**
elevator for hospital, give priority to bed transport with badge

**Spec:**
```
Type:       IoT system (elevator priority call)
Features:   - Read staff badges at elevator landings
            - Put a car into priority mode for porters with beds
            - Release priority after 5 minutes
            - Log priority uses
Tech stack: RFID readers, PLC interface, Python
```

---

## Example 420

**Intent:**
sharpening service with locker dropoff for knives

**Spec:**
```
Type:       Web application (locker drop-off service)
Data model: Locker(id, location, door_no, status)
            Order(id, customer_id, locker_id -> Locker, items, status, pin, paid)
Features:   - Book a locker for drop-off and pay online
            - Send a PIN to open the locker
            - Notify the sharpener of new drop-offs
            - Send a pick-up PIN when the knives are ready
API:        REST
            POST /orders
            POST /lockers/{id}/open
Storage:    PostgreSQL
Tech stack: Django, Stripe, ESP32 locker controllers
```

---

## Example 421

**Intent:**
smart parcel box for apartment with code for couriers

**Spec:**
```
Type:       IoT system (parcel locker)
Data model: Compartment(id, size, occupied)
            Delivery(id, compartment_id -> Compartment, resident_id, pickup_code, delivered_at, picked_at)
Features:   - Let couriers choose a free compartment on a touchscreen
            - Generate a pickup code and text the resident
            - Open the compartment with the code
            - Remind residents after 48 hours
API:        REST
            POST /deliveries
            POST /pickups
Storage:    SQLite
Tech stack: Raspberry Pi, touchscreen, solenoid locks, Python, Twilio
```

---

## Example 422

**Intent:**
library book return box full sensor

**Spec:**
```
Type:       IoT system (book drop fill alert)
Features:   - Measure the pile height in the return bin
            - Notify staff when the bin is 80 percent full
            - Count returns by a beam at the slot
Tech stack: ESP8266, VL53L1X distance sensor, IFTTT webhooks
```

---

## Example 423

**Intent:**
escape room timer display

**Spec:**
```
Type:       Web application (escape room countdown)
Features:   - Show a 60-minute countdown on the room TV
            - Show hint messages from the game master
            - Play sound effects at set times
            - Pause and add time from a control page
Tech stack: HTML, JavaScript, WebSockets, Node.js
```

---

## Example 424

**Intent:**
theater fly system rope lock reminders

**Spec:**
```
Type:       Mobile application (fly rail checklist)
Data model: Lineset(id, number, load_kg, status)
            Check(id, lineset_id -> Lineset, locked, checked_by, at)
Features:   - List linesets with their loads
            - Check off locks before each show
            - Flag out-of-weight linesets
            - Keep a history of checks
Storage:    Firebase
Tech stack: Flutter, Firebase
```

---

## Example 425

**Intent:**
DMX lighting control from tablet for small venue

**Spec:**
```
Type:       Web application (DMX lighting control)
Data model: Fixture(id, name, dmx_start, channels)
            Scene(id, name, values_json)
            Cue(id, scene_id -> Scene, fade_s, order)
Features:   - Patch fixtures to DMX addresses
            - Control fixtures with sliders
            - Save and recall scenes
            - Run a cue list with fades
API:        REST
            GET  /scenes
            POST /cues/{id}/go
Storage:    SQLite
Tech stack: Node.js, Art-Net, ENTTEC ODE, React
```

---

## Example 426

**Intent:**
concert hall decibel log for licensing

**Spec:**
```
Type:       IoT system (sound level logging)
Features:   - Measure LAeq every minute during events
            - Show the level to the sound engineer
            - Warn when the 15-minute average is near the licence limit
            - Export reports for the council
Tech stack: Raspberry Pi, calibrated USB measurement mic, Python, Grafana
```

---

## Example 427

**Intent:**
festival wristband cashless top up

**Spec:**
```
Type:       Web application (cashless festival payments)
Data model: Wristband(id, uid, balance)
            TopUp(id, wristband_id -> Wristband, amount, at)
            Purchase(id, wristband_id -> Wristband, stand, amount, at)
Features:   - Top up wristbands online or at booths
            - Charge purchases by tapping the wristband at bars
            - Work offline at stands and sync
            - Refund remaining balance after the festival
API:        REST
            POST /topups
            POST /purchases
            POST /refunds
Storage:    PostgreSQL
Tech stack: Android NFC (Kotlin), Spring Boot, Stripe
```

---

## Example 428

**Intent:**
Lost and found at festival with photos

**Spec:**
```
Type:       Web application (lost and found)
Data model: Item(id, category, description, photo_url, found_at, location, claimed_by)
Features:   - Log found items with photos
            - Let visitors search by category and date
            - Verify claims at the info tent
            - Mark items as returned
Storage:    PostgreSQL
Tech stack: Next.js, Supabase
```

---

## Example 429

**Intent:**
bell tower clock adjust for daylight saving automatically

**Spec:**
```
Type:       IoT system (tower clock controller)
Features:   - Drive the tower clock slave motor every minute
            - Sync time with GPS
            - Advance or hold the clock for daylight saving
            - Detect and correct missed pulses after a power cut
Tech stack: Arduino, GPS module, motor driver
```

---

## Example 430

**Intent:**
Grandfather clock chime silencer at night

**Spec:**
```
Type:       IoT system (chime silencer)
Features:   - Engage a servo to stop the chime at night
            - Release it in the morning
            - Set the hours from a phone
Tech stack: ESP8266, servo, Blynk
```

---

## Example 431

**Intent:**
radio telescope hydrogen line student project

**Spec:**
```
Type:       Data analysis script (hydrogen line spectra)
Features:   - Compute averaged power spectra around 1420 MHz
            - Subtract a baseline
            - Calculate Doppler velocity from the line shift
            - Plot spectra for different galactic longitudes
Tech stack: Python, NumPy, Astropy, matplotlib
```

---

## Example 432

**Intent:**
rain gauge tipping bucket for my school kids

**Spec:**
```
Type:       IoT system (rain gauge)
Features:   - Count tipping bucket pulses
            - Convert to millimetres of rain
            - Send daily totals to a class web page
            - Compare months in a chart
Tech stack: Arduino MKR WiFi 1010, tipping bucket gauge, Google Sheets
```

---

## Example 433

**Intent:**
stairs counter to motivate employees take stairs not elevator

**Spec:**
```
Type:       IoT system (stair usage counter)
Features:   - Count people on the stairs with a beam sensor
            - Show today's count on a screen at the elevator
            - Show calories saved
            - Run monthly team challenges
Tech stack: ESP32, IR beam, Raspberry Pi display, Flask
```

---

## Example 434

**Intent:**
desk occupancy sensors for hot desking

**Spec:**
```
Type:       IoT system (desk occupancy)
Data model: Desk(id, floor, code)
            Occupancy(id, desk_id -> Desk, occupied, at)
Features:   - Detect desk use with under-desk sensors
            - Show free desks on a floor map app
            - Release booked desks not used within 30 minutes
            - Report utilisation per floor
API:        REST
            GET  /floors/{id}/desks
Storage:    PostgreSQL
Tech stack: Zigbee PIR sensors, Node.js, React
```

---

## Example 435

**Intent:**
Paper towel and soap level in office toilets

**Spec:**
```
Type:       IoT system (washroom consumables)
Features:   - Measure towel and soap levels with sensors in dispensers
            - Show refill needs on a cleaner app
            - Report usage per washroom
Tech stack: ESP32, ToF sensors, MQTT, Node-RED
```

---

## Example 436

**Intent:**
i make cosplay props, want LED sword that changes color with motion

**Spec:**
```
Type:       IoT system (motion-reactive prop)
Features:   - Read motion from an accelerometer
            - Change LED colour with swing speed
            - Flash on impact
            - Charge by USB
Tech stack: Seeed XIAO nRF52840 Sense, WS2812B LEDs, Arduino C++
```

---

## Example 437

**Intent:**
haunted house scare props triggered by motion

**Spec:**
```
Type:       IoT system (prop animation)
Features:   - Detect visitors with PIR sensors
            - Trigger pneumatic props and sounds in sequence
            - Add random delays
            - Reset props between groups
Tech stack: Arduino Mega, PIR sensors, DFPlayer Mini, solenoid valves
```

---

## Example 438

**Intent:**
christmas lights synced to music for the street

**Spec:**
```
Type:       IoT system (light show)
Features:   - Sequence light channels to songs
            - Broadcast audio on FM for cars
            - Run shows on a nightly schedule
            - Allow visitors to request a song from a web page
Tech stack: Raspberry Pi, Falcon Player (FPP), xLights, ESP32 pixel controllers
```

---

## Example 439

**Intent:**
knitting machine pattern uploader

**Spec:**
```
Type:       Desktop application (knitting machine pattern loader)
Features:   - Convert an image into a two-colour stitch pattern
            - Preview the pattern row by row
            - Send the pattern to an electronic knitting machine over serial
            - Track the current row while knitting
Tech stack: Python, Pillow, pyserial, PyQt5
```

---

## Example 440

**Intent:**
sewing machine stitch counter for maintenance

**Spec:**
```
Type:       IoT system (stitch counter)
Features:   - Count needle strokes with a hall sensor
            - Total stitches per machine
            - Remind oiling and needle change after set counts
            - Show counts for all machines in the workroom
Tech stack: ESP32, hall effect sensor, MQTT, Grafana
```

---

## Example 441

**Intent:**
jewelry workshop ultrasonic cleaner timer log

**Spec:**
```
Type:       IoT system (cleaner usage log)
Features:   - Detect cleaner runs by power draw
            - Log runtime per day
            - Remind to change the cleaning fluid after set hours
Tech stack: Shelly Plug, Home Assistant
```

---

## Example 442

**Intent:**
organ pipe tuning helper

**Spec:**
```
Type:       Mobile application (pipe organ tuner)
Features:   - Detect pitch of a sustained pipe with the microphone
            - Show cents off from the target note
            - Support historical temperaments
            - Save tuning notes per rank and pipe
Storage:    Local storage
Tech stack: Swift, AudioKit
```

---

## Example 443

**Intent:**
guitar string change tracker

**Spec:**
```
Type:       Mobile application (instrument string log)
Data model: Instrument(id, name)
            StringChange(id, instrument_id -> Instrument, brand, gauge, changed_on, hours_played)
Features:   - Log string changes per instrument
            - Log practice hours
            - Remind when strings are due
            - Show favourite brands
Storage:    Local storage
Tech stack: React Native, AsyncStorage
```

---

## Example 444

**Intent:**
chicken coop door light sensor no wifi needed

**Spec:**
```
Type:       IoT system (stand-alone coop hatch)
Features:   - Read daylight level with a light sensor
            - Open the hatch above a morning light threshold
            - Close the hatch after dusk with a delay
            - Stop the motor with limit switches
            - Run on a small solar panel and battery
Tech stack: ATmega328P, LDR, DC motor driver, limit switches
```

---

## Example 445

**Intent:**
quail incubator humidity during lockdown days

**Spec:**
```
Type:       IoT system (quail incubation)
Features:   - Track incubation day count
            - Raise humidity to 70 percent for the last 3 days
            - Stop the egg turner on lockdown
            - Alert when temperature drifts
Tech stack: ESP32, SHT31, servo turner, ESPHome
```

---

## Example 446

**Intent:**
shrimp tank tds alarm

**Spec:**
```
Type:       IoT system (TDS monitoring)
Features:   - Read TDS of the shrimp tank water
            - Alert when TDS rises above the set range
            - Log readings daily
Tech stack: Arduino, TDS sensor, Blynk
```

---

## Example 447

**Intent:**
track water temp in my bottle fed lamb milk warmer

**Spec:**
```
Type:       IoT system (milk warmer thermostat)
Features:   - Hold milk at 40 °C with a heater relay
            - Alert if milk gets too hot
            - Show temperature on a display
Tech stack: Arduino Nano, DS18B20, relay, OLED
```

---

## Example 448

**Intent:**
farm gate opener with gsm call, call it and gate opens

**Spec:**
```
Type:       IoT system (GSM gate opener)
Data model: AllowedCaller(id, name, phone)
            GateOpen(id, phone, at)
Features:   - Answer calls from allowed numbers and hang up
            - Open the gate relay for allowed callers
            - Manage allowed numbers by SMS commands from the owner
            - Log each opening
Tech stack: Arduino, SIM800L, relay module
```

---

## Example 449

**Intent:**
Water trough auto fill valve for cattle with remote alert

**Spec:**
```
Type:       IoT system (trough fill control)
Features:   - Open a solenoid valve when the trough is low
            - Close it when full
            - Alert if the valve is open too long
            - Report status over LoRa
Tech stack: Heltec LoRa32, float switches, solenoid valve
```

---

## Example 450

**Intent:**
Thermal camera for detecting sick chickens

**Spec:**
```
Type:       Machine learning model (poultry health screening)
Features:   - Detect individual birds in thermal images
            - Measure head surface temperature
            - Flag birds above the flock average
            - Show flagged areas on a barn map
Tech stack: Python, FLIR Lepton, OpenCV, PyTorch
```

---

## Example 451

**Intent:**
honey bee foraging weather correlation analysis

**Spec:**
```
Type:       Data analysis script (hive weight vs weather)
Features:   - Merge hive weight with hourly weather
            - Calculate daily nectar gain
            - Correlate gain with temperature, rain and wind
            - Plot the best foraging conditions
Tech stack: Python, pandas, seaborn
```

---

## Example 452

**Intent:**
weekly report from our solar farm inverters to the investors

**Spec:**
```
Type:       Scheduled script (solar farm report)
Features:   - Pull last week's energy per inverter from the monitoring API
            - Compare with expected yield from irradiance
            - List inverters with downtime
            - Email a PDF report to investors every Monday
Tech stack: Python, SolarEdge Monitoring API, pandas, WeasyPrint, cron
```

---

## Example 453

**Intent:**
Solar panel cleaning robot schedule based on dust

**Spec:**
```
Type:       IoT system (panel cleaning scheduler)
Features:   - Compare output of a reference clean cell with a dirty panel
            - Estimate soiling loss
            - Start the cleaning robot when loss is above 5 percent
            - Skip cleaning before forecast rain
Tech stack: ESP32, reference cells, LoRa, Python
```

---

## Example 454

**Intent:**
battery storage arbitrage bot

**Spec:**
```
Type:       Scheduled script (battery arbitrage)
Features:   - Fetch day-ahead prices
            - Plan charge and discharge hours to maximise savings
            - Respect battery state of charge limits
            - Send the schedule to the inverter
            - Report daily savings
Tech stack: Python, Nord Pool API, pymodbus, cron
```

---

## Example 455

**Intent:**
EV fleet charging for our delivery vans overnight, all must be full by 6am but not exceed building power

**Spec:**
```
Type:       Web application (fleet charging management)
Data model: Van(id, plate, battery_kwh)
            Charger(id, name, max_kw)
            ChargeSession(id, van_id -> Van, charger_id -> Charger, start_soc, target_soc, started_at)
Features:   - Read the state of charge of each van
            - Balance charging power under the building limit
            - Prioritise vans leaving first
            - Control chargers over OCPP smart charging
            - Report energy per van
API:        REST
            GET  /sessions/active
            PUT  /site/power-limit
Storage:    PostgreSQL
Tech stack: Python, FastAPI, OCPP 1.6 smart charging, React
```

---

## Example 456

**Intent:**
EV charger at my airbnb, guests pay per kwh

**Spec:**
```
Type:       Web application (guest EV charging payments)
Data model: Session(id, guest_ref, kwh, price_per_kwh, amount, started_at, ended_at, paid)
Features:   - Let guests start charging by scanning a QR code
            - Read energy from the charger
            - Charge their card per kWh
            - Email a receipt
API:        REST
            POST /sessions
            POST /sessions/{id}/stop
Storage:    SQLite
Tech stack: Node.js, Stripe Checkout, OCPP
```

---

## Example 457

**Intent:**
heat meter reading for apartment block billing

**Spec:**
```
Type:       Data pipeline (heat meter billing)
Features:   - Read M-Bus heat meters monthly
            - Validate readings against the previous month
            - Calculate each apartment's share of heating cost
            - Export bills to the accounting system
Storage:    PostgreSQL
Tech stack: Python, pyMeterBus, pandas
```

---

## Example 458

**Intent:**
radiator valves in school controlled by timetable of each room

**Spec:**
```
Type:       IoT system (classroom heating by timetable)
Data model: Room(id, name)
            Lesson(id, room_id -> Room, starts_at, ends_at)
            Valve(id, room_id -> Room, zigbee_id)
Features:   - Import the room timetable
            - Heat rooms only before and during lessons
            - Lower setpoints in empty rooms
            - Report energy saved
Storage:    PostgreSQL
Tech stack: Zigbee thermostatic valves, Zigbee2MQTT, Python
```

---

## Example 459

**Intent:**
library ebook kiosk... no, a library makerspace tool check

**Spec:**
```
Type:       Web application (makerspace tool booking)
Data model: Tool(id, name, requires_training)
            Booking(id, tool_id -> Tool, card_no, starts_at, ends_at)
Features:   - Book tools such as sewing machines and vinyl cutters
            - Block bookings for tools that need training
            - Send reminders
            - Show the day's bookings at the desk
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 460

**Intent:**
cave diving gas planning calculator

**Spec:**
```
Type:       Mobile application (dive gas planner)
Features:   - Enter cylinder sizes and pressures
            - Calculate usable gas by the rule of thirds
            - Plan turn pressure
            - Calculate decompression stops for a mix
Storage:    Local storage
Tech stack: Swift, SwiftUI
```

---

## Example 461

**Intent:**
radio hams emergency message forms offline

**Spec:**
```
Type:       Desktop application (emergency radio messaging)
Data model: Message(id, number, precedence, from, to, text, sent_at, status)
Features:   - Fill ICS-213 and radiogram forms
            - Number messages automatically
            - Send messages over a packet radio modem
            - Track sent and received messages
Storage:    SQLite
Tech stack: Python, Tkinter, Direwolf TNC
```

---

## Example 462

**Intent:**
meshtastic node map for our hiking group

**Spec:**
```
Type:       Web application (mesh node map)
Data model: Node(id, name, lat, lng, battery_pct, last_heard_at)
Features:   - Receive node positions from a Meshtastic gateway
            - Show nodes on a map
            - Show battery and last heard time
            - Show message history
API:        REST
            GET  /nodes
Storage:    SQLite
Tech stack: Python, Meshtastic Python API, Flask, Leaflet
```

---

## Example 463

**Intent:**
lorawan gateway health monitor

**Spec:**
```
Type:       Scheduled script (gateway monitoring)
Features:   - Query the network server for gateway status every 5 minutes
            - Alert when a gateway goes offline
            - Report packets received per day
            - Post alerts to Slack
Tech stack: Python, ChirpStack API, Slack webhook
```

---

## Example 464

**Intent:**
firmware update over the air for our 200 field sensors

**Spec:**
```
Type:       Web application (OTA update management)
Data model: Device(id, serial, firmware_version, last_seen_at)
            Release(id, version, file_path, notes)
            Rollout(id, release_id -> Release, target_group, status)
Features:   - Upload signed firmware releases
            - Roll out to a test group first
            - Track which devices updated successfully
            - Roll back on failure
            - Show device versions
API:        REST
            POST /releases
            POST /rollouts
            GET  /devices?version={v}
Storage:    PostgreSQL, S3
Tech stack: Go, MQTT, ESP-IDF OTA, React
```

---

## Example 465

**Intent:**
device provisioning qr for our iot product wifi setup

**Spec:**
```
Type:       Mobile application (device provisioning)
Features:   - Scan the QR code on the device
            - Connect to the device over BLE
            - Send Wi-Fi credentials
            - Register the device to the user's account
Tech stack: Flutter, ESP-IDF BLE provisioning
```

---

## Example 466

**Intent:**
modbus register scanner cli

**Spec:**
```
Type:       Command-line tool (Modbus scanner)
Features:   - Read holding and input registers in a range
            - Show values as integers, floats and hex
            - Save readings to CSV
            - Poll repeatedly at an interval
Tech stack: Python, pymodbus, Click
```

---

## Example 467

**Intent:**
can bus logger for my car

**Spec:**
```
Type:       IoT system (CAN bus logging)
Features:   - Capture CAN frames from the OBD port
            - Save frames to an SD card
            - Decode known messages with a DBC file
            - Upload logs over Wi-Fi when home
Tech stack: ESP32, MCP2515, Python, cantools
```

---

## Example 468

**Intent:**
forklift impact sensor and operator login

**Spec:**
```
Type:       IoT system (forklift telematics)
Data model: Forklift(id, unit_no)
            Operator(id, name, badge_uid, licence_expires_on)
            Shift(id, forklift_id -> Forklift, operator_id -> Operator, started_at)
            Impact(id, forklift_id -> Forklift, g_force, at)
Features:   - Require a badge to start the forklift
            - Block operators with expired licences
            - Detect impacts with an accelerometer
            - Notify the supervisor of heavy impacts
            - Report hours and impacts per operator
Storage:    PostgreSQL
Tech stack: ESP32, RFID reader, LTE modem, Django
```

---

## Example 469

**Intent:**
warehouse dock door status board

**Spec:**
```
Type:       Web application (dock door board)
Data model: Door(id, number, status, trailer, updated_at)
Features:   - Detect trailers at doors with sensors
            - Show door status on a yard screen
            - Let staff assign trailers to doors
            - Show dwell time per trailer
API:        REST
            GET  /doors
            PATCH /doors/{id}
Storage:    PostgreSQL
Tech stack: Node.js, React, WebSockets
```

---

## Example 470

**Intent:**
conveyor jam detector

**Spec:**
```
Type:       IoT system (conveyor jam detection)
Features:   - Detect cartons with photo eyes along the conveyor
            - Flag a jam when a sensor stays blocked too long
            - Stop the upstream section
            - Light a beacon and notify maintenance
Tech stack: PLC, photo eyes, Node-RED
```

---

## Example 471

**Intent:**
label printer for chemical drums with GHS symbols

**Spec:**
```
Type:       Web application (GHS label printing)
Data model: Chemical(id, name, cas_no, hazards, pictograms)
            Label(id, chemical_id -> Chemical, lot, printed_at)
Features:   - Store chemicals with hazard statements
            - Generate GHS-compliant labels
            - Print to a thermal printer
            - Keep a print history
Storage:    PostgreSQL
Tech stack: Python, Flask, ZPL printing
```

---

## Example 472

**Intent:**
Forklift battery watering reminders

**Spec:**
```
Type:       Scheduled script (battery maintenance reminders)
Features:   - Track charge cycles per battery from charger logs
            - Remind staff to water batteries every 5 cycles
            - Post reminders to Teams
            - Log completed watering
Tech stack: Python, Microsoft Teams webhook, cron
```

---

## Example 473

**Intent:**
fume hood sash open alarm in chem lab

**Spec:**
```
Type:       IoT system (fume hood monitoring)
Features:   - Detect sash height with a distance sensor
            - Beep when left open with no one present
            - Report open hours per hood to save energy
Tech stack: ESP32, VL53L0X, PIR, MQTT
```

---

## Example 474

**Intent:**
Clean room particle counter logging

**Spec:**
```
Type:       IoT system (cleanroom particle logging)
Features:   - Read particle counts from counters over Modbus
            - Log counts for 0.5 and 5 micron
            - Alert on ISO class limit breaches
            - Export batch reports
Storage:    TimescaleDB
Tech stack: Python, pymodbus, Grafana
```

---

## Example 475

**Intent:**
smart pill bottle cap that logs when opened

**Spec:**
```
Type:       IoT system (medication adherence cap)
Features:   - Detect cap opening with a switch
            - Record each opening time
            - Sync to a phone app over BLE
            - Remind when a dose is missed
Tech stack: nRF52832, BLE, Flutter
```

---

## Example 476

**Intent:**
ward round tablets showing vital signs from bedside monitors

**Spec:**
```
Type:       Web application (bedside vitals viewer)
Features:   - Collect vitals from bedside monitors over HL7
            - Show the latest vitals per bed on a tablet
            - Calculate an early warning score
            - Highlight deteriorating patients
Storage:    PostgreSQL
Tech stack: Python, HL7apy, FastAPI, React
```

---

## Example 477

**Intent:**
autism sensory room light and sound control

**Spec:**
```
Type:       Web application (sensory room control)
Data model: Preset(id, name, light_color, brightness, sound_file, volume)
Features:   - Control lights and sounds from a tablet
            - Save calming presets per child
            - Fade changes slowly
            - Lock controls during sessions
Storage:    SQLite
Tech stack: Raspberry Pi, Philips Hue API, Python, Flask
```

---

## Example 478

**Intent:**
Coastguard boat crew callout pager

**Spec:**
```
Type:       Mobile application with backend (lifeboat crew paging)
Data model: Crew(id, name, phone, role)
            Shout(id, type, location, at)
            Reply(id, shout_id -> Shout, crew_id -> Crew, response, at)
Features:   - Send a loud alert to all crew phones
            - Let crew reply responding or not
            - Show who is coming on the station screen
            - Log shouts for reports
API:        REST
            POST /shouts
            POST /shouts/{id}/replies
Storage:    PostgreSQL
Tech stack: Flutter, Firebase Cloud Messaging, Node.js
```

---

## Example 479

**Intent:**
tide clock for my fishing shed

**Spec:**
```
Type:       IoT system (tide clock display)
Features:   - Fetch tide predictions for the nearest station
            - Show hours to next high and low tide on a dial
            - Update daily over Wi-Fi
            - Show the tide height on a small screen
Tech stack: ESP32, stepper motor dial, NOAA CO-OPS API
```

---

## Example 480

**Intent:**
cold storage warehouse forklift driver freezer time limit

**Spec:**
```
Type:       IoT system (freezer exposure tracking)
Data model: Worker(id, name, badge_uid)
            Exposure(id, worker_id -> Worker, entered_at, exited_at)
Features:   - Log badge taps at the freezer door
            - Track minutes spent inside per shift
            - Warn the worker when the limit is near
            - Report exposure per worker for safety
Storage:    PostgreSQL
Tech stack: RFID readers, ESP32, Python, Django
```

---

## Example 481

**Intent:**
hydroponic lettuce root temperature chiller

**Spec:**
```
Type:       IoT system (nutrient chiller control)
Features:   - Measure nutrient solution temperature
            - Run a water chiller above 22 °C
            - Log temperatures
            - Alert on chiller failure
Tech stack: ESP32, DS18B20, relay, Home Assistant
```

---

## Example 482

**Intent:**
ham radio QSL card printer from my log

**Spec:**
```
Type:       Command-line script (QSL card generator)
Features:   - Read contacts from the ADIF file
            - Fill callsign, date, band and mode onto the template
            - Generate printable PDF cards
            - Mark contacts as QSL sent
Tech stack: Python, adif-io, ReportLab
```

---

