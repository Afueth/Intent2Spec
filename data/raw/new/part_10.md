## Example 1

**Intent:**
turn on the hallway light when someone walks past at night

**Spec:**
```
Type:       IoT system (home automation)
Data model: MotionEvent(id, sensor_id, detected_at)
            LightRule(id, start_time, end_time, on_duration_s)
Features:   - Read a PIR motion sensor on a GPIO pin
            - Switch a relay-controlled light on when motion is detected
            - Only trigger between sunset and sunrise
            - Turn the light off after 2 minutes with no motion
            - Log every motion event with a timestamp
Storage:    SQLite on the device
Tech stack: Raspberry Pi, Python, gpiozero, astral (sunrise/sunset times)
```

---

## Example 2

**Intent:**
soil moisture alert for my tomato plants

**Spec:**
```
Type:       IoT system (garden monitoring)
Data model: Reading(id, sensor_id, moisture_pct, read_at)
            Threshold(sensor_id, min_moisture_pct)
Features:   - Read a capacitive soil moisture sensor every 30 minutes
            - Convert the analog value to a moisture percentage
            - Send a phone notification when moisture drops below the threshold
            - Show a 7-day moisture chart
API:        MQTT
            garden/{sensor_id}/moisture
Storage:    InfluxDB (time-series)
Tech stack: ESP32, MicroPython, Mosquitto MQTT broker, Grafana, ntfy (push notifications)
```

---

## Example 3

**Intent:**
I run a small bakery and I want the oven room temperature logged all day so the health inspector can see we kept it safe. Ideally it sends me a text if it goes too hot.

**Spec:**
```
Type:       IoT system (temperature compliance logging)
Data model: Sensor(id, location, min_c, max_c)
            TempReading(id, sensor_id -> Sensor, temperature_c, recorded_at)
            Alert(id, sensor_id -> Sensor, value_c, sent_at)
Features:   - Record temperature from a DS18B20 probe every 5 minutes
            - Send an SMS when the reading goes above the set maximum
            - Repeat the alert every 15 minutes until it is back in range
            - Export a daily PDF log for inspections
            - Flag gaps where no readings were received
Storage:    PostgreSQL
Tech stack: Raspberry Pi, Python, Twilio SMS API, ReportLab (PDF)
```

---

## Example 4

**Intent:**
esp32 weather station that posts to a website

**Spec:**
```
Type:       IoT system (weather station)
Data model: WeatherReading(id, station_id, temperature_c, humidity_pct, pressure_hpa, wind_speed_ms, rain_mm, recorded_at)
Features:   - Read temperature, humidity and pressure from a BME280 over I2C
            - Count anemometer and rain gauge pulses with interrupts
            - Upload readings over Wi-Fi every 5 minutes
            - Show current conditions and 24-hour graphs on a web page
            - Compute daily min, max and total rainfall
API:        REST
            POST /api/readings
            GET  /api/readings/latest
            GET  /api/readings?from={date}&to={date}
Storage:    SQLite
Tech stack: ESP32, Arduino (C++), Python, Flask, Chart.js
```

---

## Example 5

**Intent:**
plz make my garage door open from phone, i always forget if i closed it lol

**Spec:**
```
Type:       IoT system (home automation)
Data model: DoorEvent(id, state, triggered_by, occurred_at)
Features:   - Trigger the garage door opener through a relay
            - Detect open or closed state with a magnetic reed switch
            - Show the current door state in a phone web app
            - Send a notification if the door stays open for more than 10 minutes after 9 pm
            - Keep a history of open and close events
API:        REST
            GET  /door/state
            POST /door/toggle
            GET  /door/events
Storage:    SQLite
Tech stack: ESP8266, Arduino (C++), Node.js, Express, Pushover API
```

---

## Example 6

**Intent:**
Something to monitor air quality in my kid's bedroom - CO2 and dust. I'd like to see it on a small screen on the wall and get warned if it's bad.

**Spec:**
```
Type:       IoT system (air quality monitoring)
Data model: AirReading(id, co2_ppm, pm25_ugm3, pm10_ugm3, temperature_c, humidity_pct, read_at)
Features:   - Read CO2 from an SCD30 sensor and particulates from a PMS5003
            - Show current values on a small e-ink display
            - Color-code readings as good, moderate or poor
            - Send a warning when CO2 stays above 1200 ppm for 15 minutes
            - Store readings for a weekly trend chart
Storage:    InfluxDB (time-series)
Tech stack: Raspberry Pi Zero 2 W, Python, Waveshare e-Paper library, Grafana
```

---

## Example 7

**Intent:**
watering system for greenhouse with schedule and rain skip

**Spec:**
```
Type:       IoT system (greenhouse irrigation)
Data model: Zone(id, name, valve_pin, duration_min)
            Schedule(id, zone_id -> Zone, start_time, days_of_week)
            WateringRun(id, zone_id -> Zone, started_at, duration_min, skipped_reason)
Features:   - Open solenoid valves through a relay board on a schedule
            - Skip runs when the weather forecast shows rain above 5 mm
            - Allow manual start and stop of each zone
            - Log every run and every skipped run
            - Stop all valves if a run exceeds its maximum duration
API:        REST
            GET  /zones
            POST /zones/{id}/start
            POST /zones/{id}/stop
            PUT  /schedules/{id}
Storage:    SQLite
Tech stack: Raspberry Pi, Python, FastAPI, APScheduler, Open-Meteo API
```

---

## Example 8

**Intent:**
i want my 3d printer to text me when the print is done

**Spec:**
```
Type:       Webhook service
Features:   - Receive print status events from OctoPrint webhooks
            - Send a text message when a print finishes or fails
            - Include the file name and total print time in the message
            - Attach a webcam snapshot of the finished print
API:        REST
            POST /webhooks/octoprint
Tech stack: Python, Flask, OctoPrint, Twilio API
```

---

## Example 9

**Intent:**
we are a food bank and need a way to track donations coming in and food going out to families, its all on paper now and volunteers keep losing the sheets

**Spec:**
```
Type:       Web application (inventory)
Auth:       Volunteer login (email + password), admin role for coordinators
Data model: Donor(id, name, contact)
            Donation(id, donor_id -> Donor, received_at, notes)
            Item(id, name, category, unit, quantity_on_hand, expiry_date)
            Distribution(id, family_id -> Family, item_id -> Item, quantity, given_at)
            Family(id, reference_code, household_size)
Features:   - Record incoming donations item by item
            - Record food handed out to registered families
            - Show current stock with items expiring soon highlighted
            - Generate monthly reports of pounds received and distributed
            - Print a thank-you receipt for donors
Storage:    PostgreSQL
Tech stack: Python, Django, Bootstrap
```

---

## Example 10

**Intent:**
Raspberry Pi kiosk showing the bus departure times in our office lobby

**Spec:**
```
Type:       Web application (kiosk)
Features:   - Fetch real-time departures from the transit agency GTFS-Realtime feed every 30 seconds
            - Show the next departures for chosen stops in large text
            - Highlight delayed and cancelled trips
            - Launch full-screen in Chromium kiosk mode on boot
            - Show a clock and the current weather in the header
Tech stack: Raspberry Pi, Python, Flask, gtfs-realtime-bindings, Chromium kiosk mode
```

---

## Example 11

**Intent:**
My grandmother lives alone and I worry she might fall. Can we have something that notices if she hasn't moved around the house all morning and calls me?

**Spec:**
```
Type:       IoT system (elderly care monitoring)
Data model: Room(id, name)
            ActivityEvent(id, room_id -> Room, detected_at)
            Contact(id, name, phone)
            Alert(id, reason, sent_at, acknowledged_at)
Features:   - Collect motion events from PIR sensors in each room
            - Learn her usual wake-up time from past activity
            - Send an alert call to family if there is no activity by the expected time plus 2 hours
            - Escalate to a second contact if the first alert is not acknowledged
            - Show a daily activity timeline to family members
Storage:    PostgreSQL
Tech stack: Zigbee motion sensors, Zigbee2MQTT, Home Assistant, Python, Twilio Voice API
```

---

## Example 12

**Intent:**
hello, i am working in a library and we want a system so people can borrow the laptops with their card, please. now we write in book.

**Spec:**
```
Type:       Web application (equipment loans)
Auth:       Staff login; patrons identified by scanning their library card barcode
Data model: Patron(id, card_number, name, email)
            Laptop(id, asset_tag, model, status)
            Loan(id, laptop_id -> Laptop, patron_id -> Patron, checked_out_at, due_at, returned_at)
Features:   - Check out a laptop by scanning the patron card and the laptop asset tag
            - Check in a laptop and mark it available
            - Show which laptops are out and which are overdue
            - Email patrons a reminder before the due time
            - Block patrons with an overdue laptop from borrowing another
Storage:    PostgreSQL
Tech stack: Python, Django, USB barcode scanner (keyboard input)
```

---

## Example 13

**Intent:**
track my solar panels production vs house usage

**Spec:**
```
Type:       Data dashboard (energy monitoring)
Data model: EnergyReading(id, solar_w, consumption_w, grid_import_w, grid_export_w, recorded_at)
Features:   - Read the inverter over Modbus TCP every 10 seconds
            - Read house consumption from a CT clamp energy meter
            - Show live production and consumption gauges
            - Show daily, monthly and yearly kWh totals
            - Calculate self-consumption percentage
Storage:    InfluxDB (time-series)
Tech stack: Python, pymodbus, Telegraf, InfluxDB, Grafana
```

---

## Example 14

**Intent:**
fridge door left open alarm

**Spec:**
```
Type:       IoT system (appliance monitoring)
Features:   - Detect door open state with a magnetic reed switch
            - Start a timer when the door opens
            - Sound a buzzer after the door is open for 60 seconds
            - Send a phone notification after 3 minutes
Tech stack: Arduino Nano 33 IoT, Arduino (C++), IFTTT Webhooks
```

---

## Example 15

**Intent:**
digital menu board for my cafe on two TVs, i want to change prices from my laptop without going to the screens

**Spec:**
```
Type:       Web application (digital signage)
Auth:       Owner login (email + password)
Data model: Screen(id, name, layout)
            MenuItem(id, name, price, category, is_sold_out, image_url)
            ScreenAssignment(screen_id -> Screen, category)
Features:   - Edit menu items and prices in an admin page
            - Assign menu categories to each screen
            - Push changes to the screens instantly over WebSockets
            - Mark items as sold out so they show greyed out
            - Rotate a promo slide every 20 seconds
API:        REST
            GET  /api/menu
            PUT  /api/menu/{id}
            GET  /api/screens/{id}/content
Storage:    SQLite
Tech stack: Node.js, Express, Socket.IO, Raspberry Pi players in Chromium kiosk mode
```

---

## Example 16

**Intent:**
count how many people visit the museum each hour

**Spec:**
```
Type:       IoT system (visitor counting)
Data model: Counter(id, entrance_name)
            CountEvent(id, counter_id -> Counter, direction, counted_at)
Features:   - Detect people crossing the entrance with a time-of-flight sensor
            - Tell the difference between entering and leaving
            - Aggregate counts per hour and per day
            - Show current occupancy on a staff dashboard
            - Export monthly visitor totals to CSV
API:        MQTT
            museum/{counter_id}/count
Storage:    TimescaleDB
Tech stack: ESP32, VL53L1X sensor, Arduino (C++), Mosquitto, Python, Grafana
```

---

## Example 17

**Intent:**
i have home assistant and want the heating to go down when everyone leaves the house

**Spec:**
```
Type:       IoT system (home automation)
Features:   - Detect presence from each family member's phone using the Home Assistant companion app
            - Lower the thermostat to the away temperature when the last person leaves
            - Restore the comfort temperature when someone is 5 km from home
            - Skip the rule when a guest mode toggle is on
            - Send a notification each time the mode changes
Tech stack: Home Assistant, YAML automations, Zones and device_tracker, smart thermostat integration
```

---

## Example 18

**Intent:**
Our church wants people to be able to give money on a screen in the lobby with their card.

**Spec:**
```
Type:       Web application (donation kiosk)
Data model: Fund(id, name, description, is_active)
            Donation(id, fund_id -> Fund, amount, payment_intent_id, receipt_email, donated_at)
Features:   - Show giving funds (tithes, missions, building) on a touchscreen
            - Let the donor pick an amount or type a custom one
            - Take card payments through a card reader
            - Email a receipt if the donor enters an email
            - Show totals per fund to the treasurer
Storage:    PostgreSQL
Tech stack: Next.js, Stripe Terminal, Raspberry Pi touchscreen in kiosk mode
```

---

## Example 19

**Intent:**
beehive scale that tells me the weight every day

**Spec:**
```
Type:       IoT system (beekeeping monitoring)
Data model: Hive(id, name, apiary)
            HiveReading(id, hive_id -> Hive, weight_kg, temperature_c, battery_v, recorded_at)
Features:   - Measure hive weight with load cells and an HX711 amplifier
            - Send one reading per hour over LoRaWAN
            - Sleep between readings to save battery
            - Show weight trends to spot nectar flow and swarming
            - Alert when weight drops more than 2 kg in an hour
Storage:    InfluxDB
Tech stack: Arduino MKR WAN 1310, The Things Network, Node-RED, InfluxDB, Grafana
```

---

## Example 20

**Intent:**
trucks gps tracking for my 8 delivery vans and see them on map

**Spec:**
```
Type:       Web application (fleet tracking)
Auth:       Dispatcher login (email + password)
Data model: Vehicle(id, plate, driver_name, tracker_imei)
            Position(id, vehicle_id -> Vehicle, lat, lon, speed_kmh, recorded_at)
Features:   - Receive GPS positions from vehicle trackers every 30 seconds
            - Show all vans live on a map
            - Replay a van's route for a chosen day
            - Alert when a van leaves a geofenced service area
            - Report daily distance driven per van
API:        REST
            POST /api/positions
            GET  /api/vehicles
            GET  /api/vehicles/{id}/route?date={date}
Storage:    PostgreSQL with PostGIS
Tech stack: Python, FastAPI, Leaflet, OpenStreetMap tiles, Traccar-compatible GPS trackers
```

---

## Example 21

**Intent:**
Can you make a Python script that reads my Arduino temperature sensor over USB and saves it to a CSV file?

**Spec:**
```
Type:       Command-line script (data logging)
Features:   - Open the Arduino's serial port at a set baud rate
            - Parse each temperature line sent by the Arduino
            - Append the reading with a timestamp to a CSV file
            - Reconnect automatically if the USB cable is unplugged
            - Print the latest reading to the console
Input:      Serial port name, baud rate, output CSV path
Tech stack: Python, pyserial
```

---

## Example 22

**Intent:**
Food pantry check-in tablet for clients

**Spec:**
```
Type:       Web application (kiosk)
Data model: Client(id, household_id, name, zip_code)
            Visit(id, client_id -> Client, visited_at, items_received)
Features:   - Look up a client by name or ID card
            - Register new clients with household size and zip code
            - Record each visit with a timestamp
            - Warn staff if a client already visited this week
            - Show daily visit count
Storage:    Firebase Firestore
Tech stack: React, Firebase, Android tablet in kiosk mode
```

---

## Example 23

**Intent:**
smart plug energy usage report each month

**Spec:**
```
Type:       Scheduled script (energy reporting)
Features:   - Read kWh totals from each Shelly smart plug's local HTTP API
            - Store a monthly snapshot per plug
            - Calculate cost using the electricity tariff
            - Email a monthly report ranking devices by usage
Input:      List of smart plug IP addresses, tariff per kWh
Storage:    SQLite
Tech stack: Python, requests, cron, smtplib
```

---

## Example 24

**Intent:**
so i got a bunch of ds18b20 sensors and i want to put one in each room of the house and see all the temps on one page, maybe with history. using a pi 4 i have lying around

**Spec:**
```
Type:       IoT system (temperature monitoring)
Data model: Room(id, name, sensor_address)
            Reading(id, room_id -> Room, temperature_c, read_at)
Features:   - Read every DS18B20 on the 1-Wire bus every minute
            - Map each sensor address to a room name
            - Show current temperatures for all rooms on one web page
            - Show a 24-hour and 7-day history chart per room
            - Highlight rooms colder than a set minimum
API:        REST
            GET  /api/rooms
            GET  /api/rooms/{id}/history?range={range}
Storage:    SQLite
Tech stack: Raspberry Pi 4, Python, w1thermsensor, Flask, Chart.js
```

---

## Example 25

**Intent:**
Hi, I'm a nurse at a small clinic. We want a screen in the waiting room that shows which ticket number is being called, like at the bank.

**Spec:**
```
Type:       Web application (queue management)
Data model: Ticket(id, number, service, status, issued_at, called_at)
            Counter(id, name)
Features:   - Issue a numbered ticket from a reception page and print it
            - Let staff call the next ticket to their counter
            - Show the current called number and counter on the waiting room TV
            - Play a chime and read out the number with text-to-speech
            - Reset numbering every morning
Storage:    SQLite
Tech stack: Node.js, Express, Socket.IO, thermal receipt printer (ESC/POS), Web Speech API
```

---

## Example 26

**Intent:**
plant growth chamber controller lights + fan + humidity

**Spec:**
```
Type:       IoT system (grow chamber control)
Data model: Setpoint(id, light_on_time, light_off_time, target_humidity_pct, max_temp_c)
            Reading(id, temperature_c, humidity_pct, recorded_at)
Features:   - Switch grow lights on a daily photoperiod schedule
            - Run an exhaust fan when temperature goes above the maximum
            - Run a humidifier to keep humidity at the target
            - Log readings every minute
            - Let setpoints be changed from a web page
Storage:    SQLite
Tech stack: Raspberry Pi, Python, Adafruit SHT31 library, relay HAT, Flask
```

---

## Example 27

**Intent:**
alert when water leak under sink

**Spec:**
```
Type:       IoT system (leak detection)
Features:   - Detect water with a leak sensor probe
            - Send a push notification within seconds of a leak
            - Sound a local buzzer until reset
            - Run on batteries and wake from deep sleep on the sensor interrupt
Tech stack: ESP32, ESPHome, Home Assistant
```

---

## Example 28

**Intent:**
we are 3 volunteers running a animal shelter, need app for listing dogs and cats for adoption with photos and people can apply

**Spec:**
```
Type:       Web application (adoption listings)
Auth:       Staff login for volunteers; public browsing without login
Data model: Animal(id, name, species, breed, age_months, description, status)
            Photo(id, animal_id -> Animal, url)
            Application(id, animal_id -> Animal, applicant_name, email, phone, home_type, message, status, submitted_at)
Features:   - List adoptable animals with photos and filters by species and age
            - Let the public submit an adoption application
            - Let volunteers review, approve or reject applications
            - Mark animals as adopted
            - Email the applicant when their application status changes
Storage:    PostgreSQL, S3-compatible storage (photos)
Tech stack: Ruby on Rails, Active Storage, Tailwind CSS
```

---

## Example 29

**Intent:**
barcode scanner + receipt printer cash register for my little shop

**Spec:**
```
Type:       Desktop application (point of sale)
Data model: Product(id, barcode, name, price, stock_qty)
            Sale(id, total, payment_method, sold_at)
            SaleLine(id, sale_id -> Sale, product_id -> Product, quantity, unit_price)
Features:   - Add products to the cart by scanning a barcode
            - Calculate totals with tax
            - Print a receipt on a thermal printer
            - Reduce stock after each sale
            - Show an end-of-day sales summary
Storage:    SQLite
Tech stack: Python, PySide6, python-escpos, USB barcode scanner
```

---

## Example 30

**Intent:**
Is there a way for the town hall to let residents report potholes and broken street lights on a map with a photo?

**Spec:**
```
Type:       Web application (public issue reporting)
Auth:       Optional resident login; staff login for the public works team
Data model: Report(id, category, description, lat, lon, photo_url, status, reporter_email, created_at)
            StatusUpdate(id, report_id -> Report, status, note, updated_at)
Features:   - Let residents drop a pin on a map and add a photo and description
            - Choose a category such as pothole, street light or graffiti
            - Show staff a list of reports filtered by status and area
            - Update the report status and notify the reporter by email
            - Show public reports on a map so duplicates are avoided
Storage:    PostgreSQL with PostGIS, object storage for photos
Tech stack: Python, Django, Leaflet, OpenStreetMap
```

---

## Example 31

**Intent:**
automatic hen house door so the fox cant get my hens at night

**Spec:**
```
Type:       IoT system (farm automation)
Features:   - Calculate sunrise and sunset times from the coop's location
            - Drive a linear actuator to open and close the door
            - Confirm the door position with limit switches
            - Send an alert if the door fails to close
            - Allow manual open and close from a phone
Tech stack: ESP32, Arduino (C++), Dusk2Dawn library, Blynk
```

---

## Example 32

**Intent:**
i have a raspberry pi pico w and want it to show the current electricity price on a little OLED screen

**Spec:**
```
Type:       IoT system (energy price display)
Features:   - Connect to Wi-Fi on boot
            - Fetch the current hourly electricity price from the provider API every 15 minutes
            - Show the price and the next 3 hours on a 128x64 OLED
            - Turn an LED red when the price is above a set threshold
Tech stack: Raspberry Pi Pico W, MicroPython, SSD1306 driver, urequests
```

---

## Example 33

**Intent:**
help my disabled brother control the TV and lights with his voice since he can't use his hands

**Spec:**
```
Type:       IoT system (accessibility home control)
Features:   - Turn lights on and off with voice commands
            - Control the TV power, volume and channel through an infrared blaster
            - Create simple phrases like "movie time" that run several actions
            - Confirm each action with spoken feedback
            - Work offline so it does not depend on the internet
Tech stack: Home Assistant, Home Assistant Assist with local Whisper and Piper, Broadlink IR blaster, Zigbee smart bulbs
```

---

## Example 34

**Intent:**
sensor for the water level in my rain tank

**Spec:**
```
Type:       IoT system (tank level monitoring)
Data model: LevelReading(id, distance_cm, level_pct, volume_l, read_at)
Features:   - Measure distance to the water surface with an ultrasonic sensor
            - Convert distance to percent full and litres using tank dimensions
            - Send a reading every 15 minutes
            - Alert when the tank is below 20 percent
API:        MQTT
            tank/level
Tech stack: ESP8266, JSN-SR04T waterproof ultrasonic sensor, ESPHome, Home Assistant
```

---

## Example 35

**Intent:**
The science teacher wants the students to log pH and temperature from their experiments directly into a spreadsheet instead of writing it down.

**Spec:**
```
Type:       Data pipeline (lab data logging)
Data model: Experiment(id, group_name, title, started_at)
            Measurement(id, experiment_id -> Experiment, ph, temperature_c, measured_at)
Features:   - Read a pH probe and temperature probe through an analog-to-digital converter
            - Let a group start and stop an experiment with a button
            - Append each measurement as a row to a Google Sheet
            - Show the current values on a small LCD
            - Recalibrate the pH probe with two buffer solutions
Tech stack: Raspberry Pi, Python, ADS1115, gspread (Google Sheets API)
```

---

## Example 36

**Intent:**
Parcel lockers for apartment building - courier puts box in, resident gets code

**Spec:**
```
Type:       IoT system (smart lockers)
Auth:       Courier and admin PIN login on the locker touchscreen
Data model: Locker(id, size, is_occupied, lock_pin)
            Resident(id, name, unit, phone)
            Delivery(id, locker_id -> Locker, resident_id -> Resident, pickup_code, delivered_at, collected_at)
Features:   - Let a courier choose a resident and a free locker of the right size
            - Unlock the locker with a solenoid lock
            - Send the resident a pickup code by SMS
            - Unlock the locker when the resident types the code
            - Remind residents about parcels left more than 3 days
Storage:    SQLite
Tech stack: Raspberry Pi, Python, Kivy (touchscreen UI), relay board, Twilio SMS API
```

---

## Example 37

**Intent:**
pi hole stats on my desk display

**Spec:**
```
Type:       IoT system (status display)
Features:   - Poll the Pi-hole API every minute
            - Show total queries, blocked queries and block percentage
            - Show the top blocked domain
            - Dim the screen at night
Tech stack: Raspberry Pi Zero, Python, Pi-hole API, Pimoroni Inky pHAT
```

---

## Example 38

**Intent:**
In our village we have a little free library box and I would like to know when people use it, to show the council it's used

**Spec:**
```
Type:       IoT system (usage counting)
Data model: DoorOpen(id, opened_at, duration_s)
Features:   - Count door openings with a reed switch
            - Send a daily count over LoRaWAN to save power
            - Run on a solar panel and battery
            - Show daily and monthly usage on a public web page
Storage:    InfluxDB
Tech stack: Heltec LoRa32 (ESP32), Arduino (C++), The Things Network, Grafana
```

---

## Example 39

**Intent:**
medication reminder for my dad that beeps and lights up the right box

**Spec:**
```
Type:       IoT system (medication reminder)
Data model: Dose(id, compartment, scheduled_time, medication_name)
            DoseLog(id, dose_id -> Dose, taken_at, missed)
Features:   - Light an LED on the correct pill box compartment at dose time
            - Beep until the compartment lid is opened
            - Detect lid opening with a hall effect sensor
            - Text a family member if a dose is missed for 30 minutes
            - Let family set the schedule from a web page
Storage:    SQLite
Tech stack: ESP32, Arduino (C++), Flask, Twilio SMS API
```

---

## Example 40

**Intent:**
farm tractor hours tracker for maintenance

**Spec:**
```
Type:       Mobile application with backend
Auth:       Farm staff login (email + password)
Data model: Machine(id, name, type, current_hours)
            HourLog(id, machine_id -> Machine, hours, logged_at, logged_by)
            ServiceTask(id, machine_id -> Machine, name, interval_hours, last_done_hours)
Features:   - Log engine hours for each machine
            - Show services that are due or overdue based on hours
            - Mark a service as done with notes and parts used
            - Send a reminder when a service is within 10 hours of due
            - Keep a full maintenance history per machine
API:        REST
            GET  /machines
            POST /machines/{id}/hours
            GET  /machines/{id}/services
            POST /services/{id}/complete
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI
```

---

## Example 41

**Intent:**
notify me on telegram if my server room gets too hot

**Spec:**
```
Type:       IoT system (environmental alerting)
Features:   - Read temperature and humidity from a DHT22 every minute
            - Send a Telegram message when temperature exceeds 28 C
            - Send a recovery message when it drops back
            - Answer a /status command with the current reading
Tech stack: Raspberry Pi, Python, Adafruit CircuitPython DHT, python-telegram-bot
```

---

## Example 42

**Intent:**
hey so my mum has dementia and she sometimes goes out the front door at night, i want to know when the door opens between like 11pm and 6am, without making her feel watched with cameras

**Spec:**
```
Type:       IoT system (elderly care alerts)
Data model: DoorEvent(id, opened_at, alert_sent)
            QuietHours(start_time, end_time)
Features:   - Detect the front door opening with a contact sensor
            - Send a loud phone alert to the carer only during quiet hours
            - Ignore openings outside quiet hours but log them
            - Let the carer pause alerts for a night
            - Show a weekly log of night-time door openings
Storage:    SQLite
Tech stack: Zigbee door contact sensor, Zigbee2MQTT, Node-RED, Pushover (priority alerts)
```

---

## Example 43

**Intent:**
lab freezer -80 monitoring with alarms for our university lab

**Spec:**
```
Type:       IoT system (lab equipment monitoring)
Auth:       Lab member login with university SSO (SAML)
Data model: Freezer(id, name, room, alarm_threshold_c)
            Reading(id, freezer_id -> Freezer, temperature_c, recorded_at)
            Alarm(id, freezer_id -> Freezer, started_at, acknowledged_by, acknowledged_at)
Features:   - Read thermocouple temperatures every minute
            - Raise an alarm when a freezer warms above its threshold for 5 minutes
            - Call and text the on-call list in order until someone acknowledges
            - Detect lost connection to a sensor and alarm on that too
            - Keep a 2-year temperature history for audits
Storage:    TimescaleDB
Tech stack: Raspberry Pi, MAX31856 thermocouple board, Python, Django, Twilio
```

---

## Example 44

**Intent:**
E-ink room booking sign outside each meeting room

**Spec:**
```
Type:       IoT system (digital signage)
Features:   - Fetch today's bookings for the room from the Microsoft 365 calendar
            - Show the current meeting, next meeting and free/busy status
            - Refresh the e-ink display every 5 minutes
            - Run on battery with deep sleep between refreshes
Tech stack: ESP32, Waveshare 7.5 inch e-paper, Arduino (C++), Microsoft Graph API (via a small Python proxy)
```

---

## Example 45

**Intent:**
an app for our mosque to show the prayer times on a tv

**Spec:**
```
Type:       Web application (digital signage)
Data model: Mosque(id, name, latitude, longitude, calculation_method)
            IqamahTime(id, prayer, time, valid_from)
Features:   - Calculate the five daily prayer times from the mosque's location
            - Show adhan and iqamah times with a countdown to the next prayer
            - Show announcements and the Hijri date
            - Let the admin change iqamah times from a phone
            - Run full-screen on a TV stick
Storage:    SQLite
Tech stack: Python, Flask, adhanpy (prayer time calculation), Raspberry Pi in Chromium kiosk mode
```

---

## Example 46

**Intent:**
Arduino reaction time game with buttons and LEDs for the science fair

**Spec:**
```
Type:       Desktop game (hardware reaction game)
Features:   - Light an LED after a random delay
            - Measure the time until the player presses the button
            - Show the reaction time on a 4-digit 7-segment display
            - Detect false starts before the LED lights
            - Keep the best score in EEPROM
Tech stack: Arduino Uno, Arduino (C++), TM1637 display library
```

---

## Example 47

**Intent:**
track which volunteer drivers delivered meals to which seniors each day

**Spec:**
```
Type:       Web application (meal delivery coordination)
Auth:       Coordinator login and driver login (magic link email)
Data model: Driver(id, name, phone)
            Recipient(id, name, address, dietary_notes)
            Route(id, driver_id -> Driver, date)
            Stop(id, route_id -> Route, recipient_id -> Recipient, order, delivered_at, note)
Features:   - Create daily delivery routes and assign drivers
            - Show each driver their stops in order on a phone
            - Let drivers mark each meal as delivered or note a problem
            - Flag recipients who did not answer the door for a welfare call
            - Report meals delivered per month
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 48

**Intent:**
dog water bowl refill automatically

**Spec:**
```
Type:       IoT system (pet care automation)
Features:   - Detect a low water level with a float switch
            - Open a small solenoid valve to refill the bowl
            - Close the valve when the high-level float triggers
            - Stop and alert if refilling takes longer than 30 seconds (possible leak)
Tech stack: Arduino Nano, Arduino (C++), 12V solenoid valve with MOSFET driver
```

---

## Example 49

**Intent:**
I want a dashboard for our 40 hectare farm that shows rainfall, soil temperature and moisture from sensors spread over the fields. Wifi doesn't reach out there.

**Spec:**
```
Type:       IoT system (farm sensor network)
Data model: Node(id, field_name, lat, lon)
            Reading(id, node_id -> Node, soil_temp_c, soil_moisture_pct, rain_mm, battery_v, received_at)
Features:   - Collect readings from battery-powered field nodes over LoRaWAN
            - Decode uplink payloads into sensor values
            - Show each node on a farm map with its latest readings
            - Chart moisture and rainfall trends per field
            - Warn when a node's battery is low or it stops reporting
API:        MQTT
            v3/{app_id}/devices/{device_id}/up
Storage:    InfluxDB
Tech stack: LoRaWAN soil sensor nodes, ChirpStack (LoRaWAN network server), Node-RED, InfluxDB, Grafana
```

---

## Example 50

**Intent:**
rfid door lock for our makerspace members

**Spec:**
```
Type:       IoT system (access control)
Auth:       Admin login for the member management page
Data model: Member(id, name, rfid_uid, is_active, expires_on)
            AccessLog(id, member_id -> Member, door, granted, scanned_at)
Features:   - Read member RFID cards with an RC522 reader
            - Unlock the door strike for 5 seconds when a card is valid and active
            - Reject expired or unknown cards and log the attempt
            - Let admins add, deactivate and renew members
            - Keep working with a cached member list when the server is offline
API:        REST
            GET  /api/members/active
            POST /api/access-logs
Storage:    PostgreSQL (server), SPIFFS cache on the reader
Tech stack: ESP32, MFRC522 library, Arduino (C++), Python, Django
```

---

## Example 51

**Intent:**
Kiosk where visitors to our office sign in and the host gets a message

**Spec:**
```
Type:       Web application (visitor kiosk)
Data model: Host(id, name, email, slack_user_id)
            Visit(id, visitor_name, company, host_id -> Host, signed_in_at, signed_out_at, badge_printed)
Features:   - Let visitors type their name, company and pick who they are visiting
            - Notify the host on Slack when their visitor arrives
            - Print a name badge on a label printer
            - Let visitors sign out on the way out
            - Show reception a list of who is in the building for fire safety
Storage:    PostgreSQL
Tech stack: React, Node.js, Express, Slack API, Brother QL label printer
```

---

## Example 52

**Intent:**
monitor how much my washing machine and dryer cost per load

**Spec:**
```
Type:       Data analysis script (appliance energy)
Features:   - Read power readings logged by smart plugs
            - Detect start and end of each wash cycle from power above 5 W
            - Calculate kWh and cost per cycle using the tariff
            - Show average cost per load per appliance
            - Plot cost per week as a bar chart
Input:      CSV export of power readings (timestamp, device, watts), tariff per kWh
Tech stack: Python, pandas, matplotlib
```

---

## Example 53

**Intent:**
arduino parking sensor for my garage so i dont hit the wall

**Spec:**
```
Type:       IoT system (parking assist)
Features:   - Measure the distance to the car with an HC-SR04 ultrasonic sensor
            - Show green, yellow and red on an LED strip as the car gets closer
            - Flash red when the car is within 30 cm
            - Turn the LEDs off after the car is stationary for 1 minute
Tech stack: Arduino Uno, Arduino (C++), WS2812B LED strip, FastLED library
```

---

## Example 54

**Intent:**
homeless shelter bed availability shown live so outreach workers know where to send people

**Spec:**
```
Type:       Web application (shelter availability)
Auth:       Shelter staff login; outreach workers login with read access
Data model: Shelter(id, name, address, phone, lat, lon, eligibility_notes)
            BedCount(id, shelter_id -> Shelter, total_beds, available_beds, updated_at)
Features:   - Let shelter staff update available beds in one tap
            - Show all shelters on a map with available beds and last update time
            - Filter by eligibility such as women only, families or pets allowed
            - Mark counts as stale if not updated for 4 hours
            - Show the total beds available across the city
API:        REST
            GET  /api/shelters
            PUT  /api/shelters/{id}/beds
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Leaflet, Supabase
```

---

## Example 55

**Intent:**
vibration sensor on the pump at the farm well tells me if it fails

**Spec:**
```
Type:       IoT system (machine condition monitoring)
Data model: VibrationSample(id, rms_g, peak_g, dominant_freq_hz, sampled_at)
            PumpEvent(id, event_type, occurred_at)
Features:   - Sample an ADXL345 accelerometer at 1 kHz
            - Compute RMS and dominant frequency with an FFT every minute
            - Detect pump running or stopped from vibration level
            - Alert when vibration rises 50 percent above the baseline
            - Alert when the pump has not run for 24 hours
API:        MQTT
            farm/well_pump/vibration
Storage:    InfluxDB
Tech stack: ESP32, Arduino (C++), arduinoFFT, Mosquitto, Node-RED
```

---

## Example 56

**Intent:**
How do I make my Christmas lights change colors with music?

**Spec:**
```
Type:       IoT system (light show)
Features:   - Capture audio from a microphone or line input
            - Split the audio into frequency bands with an FFT
            - Map bass, mid and treble levels to colors on an addressable LED strip
            - Offer several effect modes switchable with a button
            - Run at 60 frames per second
Tech stack: Raspberry Pi, Python, NumPy, PyAudio, rpi_ws281x
```

---

## Example 57

**Intent:**
library self checkout station

**Spec:**
```
Type:       Web application (self-service kiosk)
Auth:       Patron sign-in by scanning the library card and entering a PIN
Data model: Patron(id, card_number, pin_hash, name)
            Item(id, barcode, title, status)
            Checkout(id, item_id -> Item, patron_id -> Patron, checked_out_at, due_date)
Features:   - Scan the patron card and verify the PIN
            - Scan item barcodes to check them out
            - Deactivate the RFID security tag after checkout
            - Print or email a receipt with due dates
            - Refuse checkout when the patron has fines over the limit
API:        SIP2 protocol to the library management system
Tech stack: Python, Flask, Koha ILS (SIP2), RFID pad reader, Chromium kiosk mode
```

---

## Example 58

**Intent:**
we have 20 kiosks in malls and i want to know if any is offline or the screen frozen

**Spec:**
```
Type:       Infrastructure setup (device fleet monitoring)
Data model: Kiosk(id, name, location, ip_address, last_heartbeat_at, last_screenshot_url)
            Incident(id, kiosk_id -> Kiosk, type, opened_at, resolved_at)
Features:   - Have each kiosk send a heartbeat every minute
            - Upload a screenshot every 15 minutes to detect frozen screens
            - Mark a kiosk offline after 3 missed heartbeats
            - Alert the support team on Slack and open an incident
            - Restart the kiosk browser remotely
API:        REST
            POST /api/heartbeat
            POST /api/kiosks/{id}/screenshot
            POST /api/kiosks/{id}/restart
Storage:    PostgreSQL, S3 (screenshots)
Tech stack: Python, FastAPI, systemd timers on kiosks, Slack webhooks
```

---

## Example 59

**Intent:**
Can I use ESPHome to see my gas meter readings?

**Spec:**
```
Type:       IoT system (utility meter reading)
Features:   - Count gas meter pulses with a magnetic reed or hall sensor
            - Convert pulses to cubic metres using the meter's pulse factor
            - Report total and hourly gas usage to Home Assistant
            - Show usage in the Home Assistant energy dashboard
Tech stack: ESP8266 (Wemos D1 mini), ESPHome pulse_meter sensor, Home Assistant
```

---

## Example 60

**Intent:**
Smart mailbox

**Spec:**
```
Type:       IoT system (mailbox notification)
Features:   - Detect the mailbox flap opening with a tilt switch
            - Wake from deep sleep on the interrupt
            - Send a "you've got mail" notification
            - Report the battery voltage once per day
Tech stack: ESP32, ESPHome, Home Assistant, LiPo battery
```

---

## Example 61

**Intent:**
My cousin is blind and wants a little device that tells him the color of his clothes when he points at it

**Spec:**
```
Type:       IoT system (assistive color identification)
Features:   - Read colour values from a TCS34725 colour sensor with its built-in LED
            - Map the RGB reading to the nearest common colour name
            - Speak the colour name through a small speaker when a button is pressed
            - Give a tactile vibration when the reading is complete
            - Run on a rechargeable battery
Tech stack: Raspberry Pi Zero 2 W, Python, Adafruit TCS34725 library, espeak-ng
```

---

## Example 62

**Intent:**
We sell vegetables at the farmers market and want to take card payments and know what sold out. Something on an ipad.

**Spec:**
```
Type:       Mobile application (point of sale)
Data model: Product(id, name, price, unit, stock_qty)
            Sale(id, total, payment_method, sold_at)
            SaleLine(id, sale_id -> Sale, product_id -> Product, quantity)
Features:   - Show products as large tappable tiles
            - Take card payments through a Bluetooth card reader
            - Accept cash and calculate change
            - Track remaining stock and mark items sold out
            - Show sales per product at the end of the market day
Storage:    On-device SQLite with cloud sync
Tech stack: Swift, SwiftUI, Square Mobile Payments SDK
```

---

## Example 63

**Intent:**
we want our 3d print farm to have a queue so students submit stl files and we print them

**Spec:**
```
Type:       Web application (print queue)
Auth:       Student login with school Google accounts; staff role for operators
Data model: PrintJob(id, user_id -> User, file_url, material, color, status, printer_id -> Printer, submitted_at, finished_at)
            Printer(id, name, octoprint_url, api_key, status)
            User(id, email, role)
Features:   - Let students upload STL files with material and colour choices
            - Let staff approve or reject jobs with a reason
            - Send approved jobs to a free printer through the OctoPrint API
            - Show live progress of each printer
            - Email the student when their print is ready to collect
Storage:    PostgreSQL, local file storage for STL files
Tech stack: Python, Django, OctoPrint REST API, Google OAuth
```

---

## Example 64

**Intent:**
pool water temperature on my phone

**Spec:**
```
Type:       IoT system (pool monitoring)
Features:   - Read a waterproof DS18B20 probe floating in the pool
            - Send the temperature every 10 minutes over Wi-Fi
            - Show the current temperature and a daily graph in the phone app
Tech stack: ESP8266, Blynk IoT platform
```

---

## Example 65

**Intent:**
home assistant automation to close blinds when sun hits the living room in summer

**Spec:**
```
Type:       IoT system (home automation)
Features:   - Use the sun's azimuth and elevation to know when it shines on the south window
            - Close the blinds to 30 percent when outdoor temperature is above 25 C
            - Open them again after the sun moves past
            - Skip the automation when the TV is not on and nobody is home
            - Allow manual override for 2 hours
Tech stack: Home Assistant, sun integration, Zigbee blind motors, YAML automations
```

---

## Example 66

**Intent:**
Our charity runs a clothing bank. Need to book appointments for families referred by social workers.

**Spec:**
```
Type:       Web application (appointment booking)
Auth:       Referrer login for social workers; staff login for the charity
Data model: Referrer(id, name, organisation, email)
            Referral(id, referrer_id -> Referrer, family_name, children_ages, sizes_needed, status)
            Appointment(id, referral_id -> Referral, slot_start, slot_end, attended)
Features:   - Let social workers submit a referral with children's ages and sizes
            - Let staff approve referrals and offer an appointment slot
            - Send the family an SMS with the date and time
            - Record attendance and what was given
            - Report families helped per month for funders
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Twilio SMS API
```

---

## Example 67

**Intent:**
logger for my car obd2 data like speed rpm coolant temp

**Spec:**
```
Type:       IoT system (vehicle telemetry)
Data model: Trip(id, started_at, ended_at, distance_km)
            ObdSample(id, trip_id -> Trip, speed_kmh, rpm, coolant_temp_c, fuel_level_pct, recorded_at)
Features:   - Read OBD-II PIDs from an ELM327 Bluetooth adapter once per second
            - Start and end trips automatically with the ignition
            - Store samples locally and upload them when home Wi-Fi is available
            - Show trip graphs of speed, RPM and coolant temperature
            - Warn when coolant temperature goes above 105 C
Storage:    SQLite (on device), PostgreSQL (server)
Tech stack: Raspberry Pi Zero 2 W, Python, python-OBD, Grafana
```

---

## Example 68

**Intent:**
Can you design a system for the hospital ward that shows nurses which call buttons were pressed and how long ago?

**Spec:**
```
Type:       IoT system (nurse call)
Data model: Bed(id, room, bed_number)
            Call(id, bed_id -> Bed, type, pressed_at, answered_at, answered_by)
Features:   - Receive call button presses from each bed over a wireless network
            - Show active calls on the nurses' station screen sorted by waiting time
            - Turn calls amber after 3 minutes and red after 5 minutes
            - Clear a call when the nurse presses the reset button in the room
            - Report average response time per shift
API:        MQTT
            ward/{ward_id}/bed/{bed_id}/call
Storage:    PostgreSQL
Tech stack: ESP32 call buttons, Mosquitto, Python, FastAPI, React
```

---

## Example 69

**Intent:**
ok so im building a cnc router and want a pendant to jog the axes, with a little screen showing the position, connects to grbl

**Spec:**
```
Type:       IoT system (machine control pendant)
Features:   - Read a rotary encoder handwheel and axis select switch
            - Send GRBL jog commands over serial for the selected axis
            - Choose step size of 0.01, 0.1 or 1 mm
            - Show machine and work coordinates on an OLED by polling GRBL status
            - Add an emergency feed hold button
Tech stack: Arduino Nano, Arduino (C++), GRBL 1.1 serial protocol, SSD1306 OLED
```

---

## Example 70

**Intent:**
Tell me the moisture of my hay bales so they dont catch fire

**Spec:**
```
Type:       IoT system (agricultural safety monitoring)
Data model: Probe(id, stack_name)
            Reading(id, probe_id -> Probe, temperature_c, moisture_pct, read_at)
Features:   - Measure internal bale temperature and moisture with probes pushed into the stack
            - Send readings every 30 minutes over LoRa
            - Warn when temperature goes above 55 C
            - Raise an urgent alarm above 65 C (fire risk)
            - Show a history chart per stack
Storage:    InfluxDB
Tech stack: LoRa32 boards, Arduino (C++), Raspberry Pi gateway, Node-RED, InfluxDB
```

---

## Example 71

**Intent:**
museum audio guide where you scan a qr code next to the painting and hear about it

**Spec:**
```
Type:       Web application (audio guide)
Auth:       Curator login for the admin area
Data model: Exhibit(id, title, artist, room, description)
            AudioTrack(id, exhibit_id -> Exhibit, language, file_url, duration_s)
Features:   - Open the exhibit page directly from a QR code without installing an app
            - Play the audio description in the visitor's chosen language
            - Show a text transcript for deaf and hard-of-hearing visitors
            - Let curators upload audio and generate QR codes
            - Count plays per exhibit
Storage:    PostgreSQL, object storage for audio files
Tech stack: SvelteKit, Supabase, qrcode library
```

---

## Example 72

**Intent:**
thermostat i build myself with esp32 and a relay to my boiler

**Spec:**
```
Type:       IoT system (heating control)
Data model: Schedule(id, day_of_week, start_time, target_c)
            State(current_c, target_c, boiler_on, updated_at)
Features:   - Read room temperature from an SHT40 sensor
            - Switch the boiler relay on and off with 0.5 C hysteresis
            - Follow a weekly heating schedule
            - Let the target be changed from a web page served by the ESP32
            - Fall back to a safe 16 C if the sensor fails
Storage:    ESP32 flash (Preferences library)
Tech stack: ESP32, Arduino (C++), ESPAsyncWebServer
```

---

## Example 73

**Intent:**
need software for the church food drive to know which families signed up for christmas hampers and who picked up

**Spec:**
```
Type:       Web application (event registration)
Auth:       Volunteer login (shared admin password per event)
Data model: Family(id, name, phone, household_size, dietary_needs)
            Hamper(id, family_id -> Family, packed, picked_up_at)
Features:   - Register families with household size and dietary needs
            - Print a packing list per hamper
            - Check families in at pickup by name or phone
            - Show how many hampers are packed, waiting and collected
            - Export the list to CSV
Storage:    SQLite
Tech stack: Python, Flask, Bootstrap
```

---

## Example 74

**Intent:**
track temperature during vaccine transport in cool boxes

**Spec:**
```
Type:       IoT system (cold chain monitoring)
Data model: Shipment(id, origin, destination, started_at, delivered_at)
            Logger(id, serial)
            Reading(id, shipment_id -> Shipment, logger_id -> Logger, temperature_c, lat, lon, recorded_at)
            Excursion(id, shipment_id -> Shipment, started_at, ended_at, max_temp_c)
Features:   - Log temperature every 5 minutes inside each cool box
            - Send readings and GPS location over cellular when signal is available
            - Record excursions outside 2-8 C with duration
            - Alert the dispatcher on any excursion longer than 10 minutes
            - Produce a per-shipment temperature report on delivery
API:        MQTT
            coldchain/{logger_id}/telemetry
Storage:    TimescaleDB
Tech stack: Nordic nRF9160 (LTE-M), Zephyr RTOS, EMQX broker, Python, FastAPI
```

---

## Example 75

**Intent:**
mi casa have many lights, i want one button for turn off all when i go sleep

**Spec:**
```
Type:       IoT system (home automation)
Features:   - Pair a wireless button with the smart home hub
            - Turn off all lights and plugs with one press
            - Leave the bedroom lamp on for 1 minute then fade it out
            - Lock the front door at the same time if it has a smart lock
Tech stack: Zigbee button, Zigbee2MQTT, Home Assistant scenes and automations
```

---

## Example 76

**Intent:**
Our town library wants to lend out tools (drills, ladders, etc) like books. Could you plan an app?

**Spec:**
```
Type:       Web application (tool library)
Auth:       Member registration with email + password and ID verification by staff
Data model: Member(id, name, email, phone, verified)
            Tool(id, name, category, condition, photo_url, status)
            Reservation(id, tool_id -> Tool, member_id -> Member, pickup_date, return_date, status)
Features:   - Browse the tool catalogue with photos and availability
            - Reserve a tool for pickup on a chosen date
            - Check tools out and in at the desk
            - Record the tool's condition on return
            - Email reminders before the return date
Storage:    PostgreSQL
Tech stack: Python, Django, Tailwind CSS
```

---

## Example 77

**Intent:**
monitor 2 aquariums ph temp and turn on heater

**Spec:**
```
Type:       IoT system (aquarium control)
Data model: Tank(id, name, target_temp_c, min_ph, max_ph)
            Reading(id, tank_id -> Tank, temperature_c, ph, read_at)
Features:   - Read pH and temperature probes for each tank
            - Switch each tank's heater relay to keep the target temperature
            - Alert when pH leaves the safe range
            - Show both tanks on a dashboard
            - Log readings every 5 minutes
API:        MQTT
            aquarium/{tank}/temperature
            aquarium/{tank}/ph
Storage:    InfluxDB
Tech stack: ESP32, Atlas Scientific pH EZO circuit, ESPHome, Home Assistant
```

---

## Example 78

**Intent:**
the parish wants a screen that shows the hymn numbers and the readings for Sunday instead of the wooden board

**Spec:**
```
Type:       Web application (digital signage)
Auth:       Admin login for the parish secretary
Data model: Service(id, date, title)
            ServiceItem(id, service_id -> Service, kind, number, text, order)
Features:   - Enter hymn numbers and readings for each service in advance
            - Show the current service on a screen in large readable text
            - Advance to the next item with a remote clicker
            - Fetch the lectionary readings for the date automatically
            - Fall back to the next upcoming service if none is set for today
Storage:    SQLite
Tech stack: Python, Flask, Raspberry Pi in Chromium kiosk mode
```

---

## Example 79

**Intent:**
plant monitor with micropython on a pico, shows sad face when thirsty

**Spec:**
```
Type:       IoT system (plant monitoring)
Features:   - Read soil moisture from a capacitive sensor on an ADC pin
            - Show a happy, neutral or sad face on a small OLED
            - Blink an LED when the plant needs watering
            - Calibrate wet and dry values with a button press
Tech stack: Raspberry Pi Pico, MicroPython, SSD1306 driver
```

---

## Example 80

**Intent:**
flood warning for a river near our village, measure the water level and warn people

**Spec:**
```
Type:       IoT system (flood monitoring)
Data model: Gauge(id, name, lat, lon, warning_level_cm, danger_level_cm)
            LevelReading(id, gauge_id -> Gauge, level_cm, read_at)
            Subscriber(id, phone, gauge_id -> Gauge)
Features:   - Measure river level with a radar distance sensor every 5 minutes
            - Send readings over LoRaWAN from a solar-powered station
            - Detect fast rises of more than 20 cm per hour
            - Send SMS warnings to subscribers at warning and danger levels
            - Show live river levels on a public web page
Storage:    TimescaleDB
Tech stack: LoRaWAN sensor node, The Things Network, Python, FastAPI, Twilio SMS API
```

---

## Example 81

**Intent:**
want a raspberry pi to take a photo of my seedlings every hour and make a timelapse

**Spec:**
```
Type:       Scheduled script (timelapse capture)
Features:   - Capture a photo every hour with the Pi camera module
            - Skip captures at night when the image is too dark
            - Name each photo with its timestamp
            - Build an MP4 timelapse every Sunday from the week's photos
            - Delete photos older than 60 days
Storage:    Local SD card or USB drive
Tech stack: Raspberry Pi, Python, picamera2, ffmpeg, cron
```

---

## Example 82

**Intent:**
Hospice volunteers need to sign up for shifts sitting with patients and the coordinator needs to see gaps.

**Spec:**
```
Type:       Web application (volunteer scheduling)
Auth:       Volunteer login (email + password), coordinator role
Data model: Volunteer(id, name, phone, trained_until)
            Shift(id, unit, starts_at, ends_at, slots)
            Signup(id, shift_id -> Shift, volunteer_id -> Volunteer)
Features:   - Show open shifts on a calendar
            - Let volunteers sign up for and cancel shifts
            - Block volunteers whose training has expired
            - Highlight unfilled shifts for the coordinator
            - Send reminder texts the day before a shift
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire, Twilio SMS API
```

---

## Example 83

**Intent:**
bluetooth temp sensors around house xiaomi, put into grafana

**Spec:**
```
Type:       Data pipeline (sensor ingestion)
Features:   - Scan for Xiaomi LYWSD03MMC BLE advertisements running custom firmware
            - Decode temperature, humidity and battery from the advertisement data
            - Write readings to a time-series database
            - Show all rooms on a Grafana dashboard
Storage:    InfluxDB
Tech stack: Raspberry Pi, Python, bleak (BLE), InfluxDB, Grafana
```

---

## Example 84

**Intent:**
Laundry room in our building, want to know if a machine is free before going downstairs

**Spec:**
```
Type:       IoT system (appliance availability)
Data model: Machine(id, name, type, status, status_changed_at)
Features:   - Detect whether each machine is running from its vibration or power draw
            - Mark a machine as free after 3 minutes with no activity
            - Show all machines and their status on a web page
            - Let residents subscribe to a notification when a machine finishes
API:        REST
            GET  /api/machines
            POST /api/machines/{id}/notify
Storage:    Redis
Tech stack: ESP32 with SW-420 vibration sensors, Python, FastAPI, Web Push
```

---

## Example 85

**Intent:**
humidity in basement is too high, turn on dehumidifier

**Spec:**
```
Type:       IoT system (climate control)
Features:   - Read basement humidity every 2 minutes
            - Turn the dehumidifier smart plug on above 60 percent humidity
            - Turn it off below 50 percent
            - Alert if humidity stays above 70 percent for 6 hours
Tech stack: Shelly Plus H&T sensor, Shelly Plug, Home Assistant
```

---

## Example 86

**Intent:**
so we are an ngo working in rural kenya, health workers visit homes and record child weight and vaccines, but often there is no internet. need an app that works offline and syncs later

**Spec:**
```
Type:       Mobile application with backend
Auth:       Health worker login with username + PIN, cached for offline use
Data model: Household(id, village, head_name, gps_lat, gps_lon)
            Child(id, household_id -> Household, name, birth_date, sex)
            Visit(id, child_id -> Child, worker_id, weight_kg, muac_cm, vaccines_given, visited_at)
Features:   - Register households and children offline
            - Record weight, arm circumference and vaccines at each visit
            - Flag children below the growth chart threshold for referral
            - Sync records to the server when a connection is available
            - Show supervisors coverage reports by village
API:        REST
            POST /sync/push
            GET  /sync/pull?since={timestamp}
Storage:    SQLite on device, PostgreSQL on server
Tech stack: Kotlin (Android), Room, WorkManager, Python, Django REST Framework
```

---

## Example 87

**Intent:**
classroom noise traffic light

**Spec:**
```
Type:       IoT system (noise level indicator)
Features:   - Measure sound level with a microphone module
            - Average the level over 2 seconds to ignore short spikes
            - Show green, amber or red on an LED traffic light
            - Let the teacher adjust thresholds with a potentiometer
Tech stack: Arduino Nano, Arduino (C++), MAX4466 microphone, NeoPixel LEDs
```

---

## Example 88

**Intent:**
lightning detector that warns when storm is getting close

**Spec:**
```
Type:       IoT system (storm detection)
Data model: StrikeEvent(id, distance_km, energy, detected_at)
Features:   - Detect lightning strikes with an AS3935 sensor over I2C
            - Estimate the storm distance for each strike
            - Send an alert when strikes come within 15 km
            - Send an all-clear after 30 minutes with no strikes
            - Show a strike count chart for the last 2 hours
API:        MQTT
            weather/lightning
Storage:    InfluxDB
Tech stack: ESP32, Arduino (C++), SparkFun AS3935 library, Mosquitto, Grafana
```

---

## Example 89

**Intent:**
doorbell press sends a photo of who's there to my telegram

**Spec:**
```
Type:       IoT system (smart doorbell)
Features:   - Detect the doorbell button press on a GPIO input
            - Capture a photo from the camera module
            - Send the photo to a Telegram chat with the time
            - Ring a chime inside the house at the same time
Tech stack: ESP32-CAM, Arduino (C++), UniversalTelegramBot library
```

---

## Example 90

**Intent:**
my wife and I just had a baby and we want to know the nursery temperature and get pinged if the baby cries while we're in the garden

**Spec:**
```
Type:       IoT system (baby monitor)
Features:   - Read nursery temperature and humidity every minute
            - Detect crying by sound level above a threshold for 5 seconds
            - Send a phone notification when crying is detected
            - Warn when room temperature is outside 16-20 C
            - Show current values in a simple phone web page
API:        MQTT
            nursery/temperature
            nursery/sound
Tech stack: Raspberry Pi Zero 2 W, Python, USB microphone, SHT31 sensor, Home Assistant
```

---

## Example 91

**Intent:**
app that tells blind people when their bus is coming at the stop by talking

**Spec:**
```
Type:       Mobile application (accessible transit)
Features:   - Find the nearest bus stop using GPS
            - Read upcoming arrivals aloud with the platform screen reader
            - Let the user pick a route and get a vibration alert 2 minutes before the bus arrives
            - Announce when the bus has passed the previous stop
            - Support large text and high-contrast mode
Tech stack: Kotlin (Android), TalkBack accessibility APIs, GTFS-Realtime feed
```

---

## Example 92

**Intent:**
cows gps collars so I can see where the herd is on the hills

**Spec:**
```
Type:       IoT system (livestock tracking)
Data model: Animal(id, tag_number, name)
            Collar(id, animal_id -> Animal, dev_eui, battery_pct)
            Location(id, collar_id -> Collar, lat, lon, recorded_at)
Features:   - Send a GPS fix from each collar every 30 minutes over LoRaWAN
            - Show the latest position of every animal on a satellite map
            - Alert when an animal leaves the virtual paddock boundary
            - Alert when an animal has not moved for 6 hours
            - Warn when a collar battery is low
Storage:    PostgreSQL with PostGIS
Tech stack: LoRaWAN GPS collars, ChirpStack, Python, FastAPI, Mapbox GL JS
```

---

## Example 93

**Intent:**
milk tank temperature on dairy farm must be under 4 degrees within 2 hours of milking

**Spec:**
```
Type:       IoT system (dairy cooling monitoring)
Data model: MilkingSession(id, started_at, ended_at)
            TankReading(id, temperature_c, agitator_on, recorded_at)
Features:   - Read bulk tank temperature with a stainless probe every minute
            - Detect milking sessions from a sudden temperature rise
            - Alert if the milk is not below 4 C within 2 hours of milking ending
            - Alert if the agitator is off for more than 20 minutes
            - Produce a compliance report for the milk buyer
Storage:    InfluxDB
Tech stack: Raspberry Pi, Python, PT100 with MAX31865, InfluxDB, Grafana
```

---

## Example 94

**Intent:**
frost warning text for my vineyard rows

**Spec:**
```
Type:       IoT system (frost alerting)
Data model: Station(id, row_block, lat, lon)
            Reading(id, station_id -> Station, air_temp_c, dew_point_c, recorded_at)
Features:   - Read air temperature and humidity at canopy height in several blocks
            - Compute the dew point from temperature and humidity
            - Send an SMS when any block drops below 1 C
            - Send a second alarm at -1 C so frost fans can be started
            - Show overnight minimum temperatures per block
Storage:    TimescaleDB
Tech stack: LoRaWAN temperature/humidity sensors, The Things Network, Python, Twilio SMS API
```

---

## Example 95

**Intent:**
how much each forklift is actually used in the warehouse per day

**Spec:**
```
Type:       IoT system (equipment utilization)
Data model: Forklift(id, name, zone)
            UsageSession(id, forklift_id -> Forklift, started_at, ended_at, operator_badge)
Features:   - Detect when a forklift is running from its ignition voltage
            - Log the operator by badge scan at start
            - Record usage sessions with start and end times
            - Show utilization percentage per forklift per shift
            - Highlight forklifts used less than 20 percent of the time
API:        MQTT
            warehouse/forklift/{id}/session
Storage:    PostgreSQL
Tech stack: ESP32, RFID badge reader, Mosquitto, Python, Metabase
```

---

## Example 96

**Intent:**
Our restaurant needs a tablet checklist for the food safety temps the cooks have to write down twice a day, and the manager wants to see it all

**Spec:**
```
Type:       Mobile application with backend
Auth:       Staff PIN login; manager login with email + password
Data model: Checkpoint(id, name, min_c, max_c, frequency)
            CheckEntry(id, checkpoint_id -> Checkpoint, staff_id -> Staff, temperature_c, corrective_action, recorded_at)
            Staff(id, name, pin_hash)
Features:   - Show the checks due for the current shift
            - Record each temperature and require a corrective action when it is out of range
            - Flag missed checks to the manager
            - Show a weekly compliance report
            - Export records for inspections as PDF
API:        REST
            GET  /checkpoints/due
            POST /entries
            GET  /reports/weekly
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Express
```

---

## Example 97

**Intent:**
filament spool scale so i know how much is left

**Spec:**
```
Type:       IoT system (3D printer filament tracking)
Data model: Spool(id, material, color, empty_weight_g, full_weight_g)
            WeightReading(id, spool_id -> Spool, weight_g, read_at)
Features:   - Weigh the spool holder with a load cell and HX711
            - Subtract the empty spool weight to get filament left
            - Estimate remaining metres from material density and diameter
            - Show grams left on a small OLED
            - Warn before a print if the job needs more filament than is left
Tech stack: ESP32, Arduino (C++), HX711 library, OctoPrint plugin integration
```

---

## Example 98

**Intent:**
cut the power to my 3d printer if theres smoke

**Spec:**
```
Type:       IoT system (fire safety)
Features:   - Read a smoke sensor and a flame sensor inside the enclosure
            - Cut printer power through a relay when smoke or flame is detected
            - Sound a loud buzzer
            - Send a phone alert
            - Require a manual reset before power comes back
Tech stack: Arduino Uno, MQ-2 smoke sensor, flame sensor, Arduino (C++), ESP-01 for Wi-Fi alerts
```

---

## Example 99

**Intent:**
laser cutter at the makerspace - log how many minutes each member uses so we can charge them

**Spec:**
```
Type:       IoT system (machine usage billing)
Auth:       Members unlock the machine with their RFID card
Data model: Member(id, name, rfid_uid, balance)
            Session(id, member_id -> Member, started_at, ended_at, laser_on_seconds, cost)
Features:   - Enable the laser cutter power only after a valid RFID scan
            - Measure actual laser firing time from the tube current
            - End the session when the member taps out or after 10 minutes idle
            - Charge members per minute of laser time
            - Show members their usage and balance online
API:        REST
            POST /api/sessions/start
            POST /api/sessions/{id}/end
            GET  /api/members/{id}/usage
Storage:    PostgreSQL
Tech stack: ESP32, MFRC522, current transformer sensor, Python, Django
```

---

## Example 100

**Intent:**
dashboard for my 6 prusa printers to see status and time left

**Spec:**
```
Type:       Data dashboard (print farm)
Features:   - Poll each printer's PrusaLink API every 10 seconds
            - Show state, job name, progress and time remaining per printer
            - Show nozzle and bed temperatures
            - Highlight printers that are idle or in error
            - Play a sound when a print finishes
Tech stack: Python, FastAPI, HTMX, PrusaLink API
```

---

## Example 101

**Intent:**
small hotel, want guests to check themselves in at a screen at night when reception is closed

**Spec:**
```
Type:       Web application (self check-in kiosk)
Data model: Booking(id, guest_name, reference, room_id -> Room, check_in_date, nights, checked_in_at)
            Room(id, number, keycard_encoder_slot)
Features:   - Let guests find their booking by reference number and surname
            - Scan the guest's ID with the kiosk camera
            - Take payment for any balance due
            - Encode a room key card
            - Show directions to the room
Storage:    PostgreSQL
Tech stack: React, Node.js, Stripe Terminal, hotel keycard encoder SDK, Windows kiosk mode
```

---

## Example 102

**Intent:**
food truck order screen customers tap and it goes to kitchen

**Spec:**
```
Type:       Web application (self-ordering kiosk)
Data model: MenuItem(id, name, price, options, available)
            Order(id, number, total, status, paid_at)
            OrderLine(id, order_id -> Order, menu_item_id -> MenuItem, quantity, options_selected)
Features:   - Show the menu with photos on a touchscreen tablet
            - Let customers choose options and pay by card
            - Send the order to a kitchen screen
            - Show a ready list with order numbers
            - Hide items when they are marked unavailable
API:        REST
            GET  /api/menu
            POST /api/orders
            PATCH /api/orders/{id}/status
Storage:    Firebase Firestore
Tech stack: React, Firebase, SumUp card reader SDK
```

---

## Example 103

**Intent:**
school hallway tv announcements managed by the office

**Spec:**
```
Type:       Web application (digital signage)
Auth:       Staff login with Google Workspace accounts
Data model: Slide(id, title, body, image_url, starts_on, ends_on, display_seconds)
            Display(id, name, location)
Features:   - Let office staff create announcement slides with an image
            - Schedule start and end dates for each slide
            - Rotate active slides on every hallway display
            - Show the day's lunch menu and bell schedule
            - Push emergency messages to all displays instantly
Storage:    PostgreSQL
Tech stack: Python, Django, Raspberry Pi players in Chromium kiosk mode, Google OAuth
```

---

## Example 104

**Intent:**
kitchen display screen for restaurant orders from the till

**Spec:**
```
Type:       Web application (kitchen display system)
Data model: Ticket(id, order_number, table, station, status, created_at, bumped_at)
            TicketItem(id, ticket_id -> Ticket, name, modifiers, quantity)
Features:   - Receive orders from the POS as soon as they are sent
            - Show tickets per station (grill, fryer, cold)
            - Color tickets by how long they have been waiting
            - Let cooks bump finished tickets with a touch
            - Show average ticket time per hour
API:        REST
            POST /api/tickets
            PATCH /api/tickets/{id}/bump
Storage:    Redis (live tickets), PostgreSQL (history)
Tech stack: Node.js, Socket.IO, Vue.js, wall-mounted touchscreens
```

---

## Example 105

**Intent:**
deli scale that prints price labels with barcode

**Spec:**
```
Type:       Desktop application (weighing and labeling)
Data model: Product(id, plu_code, name, price_per_kg)
            LabelPrint(id, product_id -> Product, weight_g, price, printed_at)
Features:   - Read the weight from a serial scale
            - Choose a product by PLU code
            - Calculate the price from weight and price per kg
            - Print a label with an EAN-13 price-embedded barcode
            - Log every label printed
Storage:    SQLite
Tech stack: Python, pyserial, Tkinter, Zebra printer with ZPL
```

---

## Example 106

**Intent:**
Grandpa needs to check his blood pressure every day, I want the readings to come to my phone automatically from his bluetooth cuff

**Spec:**
```
Type:       Mobile application with backend
Auth:       Family members invite each other by email
Data model: Patient(id, name)
            BpReading(id, patient_id -> Patient, systolic, diastolic, pulse, measured_at)
            Caregiver(id, email, patient_id -> Patient)
Features:   - Pair with a Bluetooth blood pressure monitor and import readings
            - Upload readings to the cloud automatically
            - Show caregivers a chart of readings over time
            - Alert caregivers when a reading is above 160/100
            - Export a PDF summary for the doctor
API:        REST
            POST /readings
            GET  /patients/{id}/readings
Storage:    PostgreSQL
Tech stack: Flutter, flutter_blue_plus (Bluetooth LE Blood Pressure profile), Python, FastAPI
```

---

## Example 107

**Intent:**
fall detect wearable with esp32 and accelerometer

**Spec:**
```
Type:       IoT system (fall detection wearable)
Features:   - Sample an MPU6050 accelerometer at 50 Hz
            - Detect a fall as a free-fall dip followed by an impact spike and no movement
            - Vibrate and give the wearer 30 seconds to cancel
            - Send an alert with the time to caregivers if not cancelled
            - Add a manual SOS button
API:        MQTT
            care/{wearer_id}/fall
Tech stack: ESP32, Arduino (C++), MPU6050 library, Mosquitto, Pushover API
```

---

## Example 108

**Intent:**
hospital keeps losing wheelchairs and pumps, track where they are in the building

**Spec:**
```
Type:       IoT system (indoor asset tracking)
Data model: Asset(id, type, label, beacon_id)
            Gateway(id, room, floor)
            Sighting(id, asset_id -> Asset, gateway_id -> Gateway, rssi, seen_at)
Features:   - Attach BLE beacons to wheelchairs and infusion pumps
            - Pick up beacon signals with gateways in each room
            - Estimate each asset's room from the strongest signal
            - Let staff search for the nearest available asset of a type
            - Alert when an asset leaves the building exit zone
API:        MQTT
            rtls/{gateway_id}/sightings
Storage:    PostgreSQL
Tech stack: BLE beacons, ESP32 gateways running ESPresense, Mosquitto, Python, React
```

---

## Example 109

**Intent:**
Livestock water trough empty alarm

**Spec:**
```
Type:       IoT system (farm water monitoring)
Features:   - Check the trough level with a float switch every 10 minutes
            - Send an SMS when the trough is low
            - Send the battery level once a day
            - Run on solar power in a remote paddock
Tech stack: Arduino MKR NB 1500 (NB-IoT), Arduino (C++), Twilio SMS API
```

---

## Example 110

**Intent:**
hydroponic tower, auto dose nutrients and fix ph

**Spec:**
```
Type:       IoT system (hydroponics control)
Data model: Reading(id, ph, ec_ms, water_temp_c, read_at)
            DoseEvent(id, pump, ml, reason, dosed_at)
            Target(ph_min, ph_max, ec_min, ec_max)
Features:   - Read pH, EC and water temperature every 10 minutes
            - Dose pH down solution with a peristaltic pump when pH is above range
            - Dose nutrient A and B when EC is below range
            - Wait 15 minutes after each dose to let it mix
            - Limit total daily dose volume and alert when reached
Storage:    SQLite
Tech stack: Raspberry Pi, Python, Atlas Scientific EZO circuits, peristaltic pumps on a relay board
```

---

## Example 111

**Intent:**
mushroom fruiting room needs high humidity and fresh air, automate please

**Spec:**
```
Type:       IoT system (mushroom grow room)
Features:   - Read humidity, temperature and CO2 every minute
            - Run the ultrasonic fogger to keep humidity at 85-95 percent
            - Run the fresh air fan when CO2 goes above 800 ppm
            - Turn the fan off when humidity drops too low
            - Log all readings and actuator changes
API:        MQTT
            growroom/sensors
            growroom/actuators/{name}
Tech stack: ESP32, SCD40 sensor, ESPHome, Home Assistant
```

---

## Example 112

**Intent:**
scan the pallets at our loading dock so we know what went on which truck

**Spec:**
```
Type:       Mobile application with backend
Auth:       Warehouse staff login with badge number + PIN
Data model: Shipment(id, truck_plate, dock, departed_at)
            Pallet(id, sscc_barcode, customer, weight_kg)
            LoadScan(id, shipment_id -> Shipment, pallet_id -> Pallet, scanned_by, scanned_at)
Features:   - Start a load by scanning the truck's dock QR code
            - Scan each pallet's SSCC barcode as it is loaded
            - Warn when a pallet belongs to a different shipment
            - Close the load and print a manifest
            - Search which truck a pallet left on
API:        REST
            POST /shipments
            POST /shipments/{id}/scans
            GET  /pallets/{sscc}
Storage:    PostgreSQL
Tech stack: Kotlin (Android) on Zebra handheld scanners, DataWedge, Java, Spring Boot
```

---

## Example 113

**Intent:**
proof of delivery app for our couriers - photo and signature

**Spec:**
```
Type:       Mobile application with backend
Auth:       Driver login (phone number + SMS code)
Data model: Delivery(id, tracking_number, address, recipient_name, status)
            Proof(id, delivery_id -> Delivery, photo_url, signature_url, lat, lon, delivered_at)
Features:   - Show the driver's deliveries for today in route order
            - Capture a photo of the parcel at the door
            - Capture the recipient's signature on screen
            - Record GPS location and time automatically
            - Email the customer a delivery confirmation
API:        REST
            GET  /drivers/me/deliveries
            POST /deliveries/{id}/proof
Storage:    PostgreSQL, S3 (photos and signatures)
Tech stack: React Native, Node.js, NestJS, AWS S3
```

---

## Example 114

**Intent:**
we're a tiny charity with 300 donors in a spreadsheet, we need something better to track gifts and send thank yous

**Spec:**
```
Type:       Web application (donor CRM)
Auth:       Staff login (email + password), two-factor authentication
Data model: Donor(id, name, email, address, gift_aid_eligible)
            Gift(id, donor_id -> Donor, amount, method, campaign, received_on, thanked)
            Campaign(id, name, goal_amount)
Features:   - Import donors and gifts from the existing spreadsheet
            - Record new gifts and link them to campaigns
            - List gifts not yet thanked and send thank-you emails from a template
            - Show campaign totals against goals
            - Export a Gift Aid claim file
Storage:    PostgreSQL
Tech stack: Python, Django, Postmark (email)
```

---

## Example 115

**Intent:**
volunteers clock in and out with qr code at the community garden

**Spec:**
```
Type:       Web application (volunteer hours)
Data model: Volunteer(id, name, email, qr_token)
            HoursEntry(id, volunteer_id -> Volunteer, clock_in, clock_out, task)
Features:   - Scan a volunteer's QR card with a tablet camera to clock in or out
            - Ask what task they worked on when clocking out
            - Show total hours per volunteer
            - Email volunteers a yearly hours certificate
            - Export hours for grant reports
Storage:    SQLite
Tech stack: Python, Flask, html5-qrcode
```

---

## Example 116

**Intent:**
The council wants dog licence applications online instead of paper forms.

**Spec:**
```
Type:       Web application (government form)
Auth:       Resident account with email verification
Data model: Owner(id, name, address, email, phone)
            Dog(id, owner_id -> Owner, name, breed, microchip_number, neutered)
            Licence(id, dog_id -> Dog, year, fee, status, paid_at)
Features:   - Let residents fill in a licence application with the dog's microchip number
            - Calculate the fee with discounts for neutered dogs and seniors
            - Take online payment
            - Let staff review and approve applications
            - Send renewal reminders each January
Storage:    PostgreSQL
Tech stack: Python, Django, GOV.UK Frontend, Stripe
```

---

## Example 117

**Intent:**
track where each building permit is in the approval process, citizens keep calling to ask

**Spec:**
```
Type:       Web application (permit tracking)
Auth:       Applicant login (email + password); staff login with council SSO
Data model: Application(id, reference, applicant_id -> Applicant, address, type, status, submitted_at)
            Applicant(id, name, email)
            StageHistory(id, application_id -> Application, stage, entered_at, note)
Features:   - Let applicants look up their permit by reference number
            - Show the current stage and history on a timeline
            - Let staff move applications between stages with notes
            - Email applicants when the stage changes
            - Show staff the average days spent in each stage
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Azure AD
```

---

## Example 118

**Intent:**
the lab samples freezer is chaos, need barcode labels and to know which box and position each tube is

**Spec:**
```
Type:       Web application (sample inventory)
Auth:       Lab member login with university SSO
Data model: Freezer(id, name, room)
            Box(id, freezer_id -> Freezer, shelf, rack, label)
            Sample(id, box_id -> Box, position, barcode, sample_type, project, owner, created_at)
Features:   - Register samples and assign them a box and grid position
            - Print 2D barcode tube labels
            - Find a sample by scanning its barcode
            - Show a box as a 9x9 grid with filled and empty positions
            - Log when samples are removed or thawed
Storage:    PostgreSQL
Tech stack: Python, Django, Brady label printer, python-barcode (DataMatrix)
```

---

## Example 119

**Intent:**
book the microscope in our lab

**Spec:**
```
Type:       Web application (equipment booking)
Auth:       Lab member login (email + password), admin approval for new users
Data model: Instrument(id, name, room, requires_training)
            Booking(id, instrument_id -> Instrument, user_id -> User, starts_at, ends_at)
            User(id, name, email, trained_instruments)
Features:   - Show a weekly calendar per instrument
            - Let trained users book time slots
            - Prevent overlapping bookings
            - Block untrained users from booking restricted instruments
            - Send a reminder email 1 hour before a booking
Storage:    PostgreSQL
Tech stack: Python, Django, FullCalendar
```

---

## Example 120

**Intent:**
a cli to grab spectra from our usb spectrometer and save each as csv

**Spec:**
```
Type:       Command-line tool (lab instrument)
Features:   - Connect to an Ocean Optics USB spectrometer
            - Set integration time and number of scans to average
            - Capture a spectrum and save wavelength and intensity as CSV
            - Take a dark reference and subtract it from samples
            - Plot the spectrum when the --plot flag is given
Input:      Integration time in ms, scans to average, output file name
Tech stack: Python, python-seabreeze, Click, matplotlib
```

---

## Example 121

**Intent:**
touchscreen in our museum where kids can explore old maps of the town

**Spec:**
```
Type:       Web application (interactive exhibit)
Data model: Map(id, year, title, tile_url)
            PointOfInterest(id, map_id -> Map, title, description, lat, lon, image_url)
Features:   - Show historic maps overlaid on today's map with a fade slider
            - Let visitors pinch to zoom and drag
            - Show points of interest with photos and short stories
            - Return to an attract screen after 2 minutes of no touch
            - Work fully offline
Tech stack: JavaScript, Leaflet, locally hosted map tiles, Electron in kiosk mode
```

---

## Example 122

**Intent:**
gallery humidity has to stay 45-55% for the paintings, monitor every room

**Spec:**
```
Type:       IoT system (museum climate monitoring)
Data model: Gallery(id, name, min_rh, max_rh, min_temp_c, max_temp_c)
            Reading(id, gallery_id -> Gallery, rh_pct, temp_c, read_at)
Features:   - Read humidity and temperature in each gallery every 5 minutes
            - Alert conservators when readings leave the allowed range for 30 minutes
            - Calculate daily humidity fluctuation per gallery
            - Show all galleries on one dashboard
            - Export monthly reports for loan agreements
Storage:    InfluxDB
Tech stack: Zigbee temperature/humidity sensors, Zigbee2MQTT, Telegraf, InfluxDB, Grafana
```

---

## Example 123

**Intent:**
Our synagogue has a memorial board with names and the yahrzeit dates, we want a screen version that lights the names this week

**Spec:**
```
Type:       Web application (digital signage)
Auth:       Admin login for synagogue office
Data model: Memorial(id, name, hebrew_name, date_of_death, hebrew_date_of_death, relative_contact)
Features:   - Store memorial names with their Hebrew date of death
            - Convert Hebrew dates to this year's Gregorian dates
            - Highlight names whose yahrzeit falls this week
            - Email relatives a reminder 2 weeks ahead
            - Show the board full-screen on a TV
Storage:    SQLite
Tech stack: Python, Flask, pyluach (Hebrew calendar), Raspberry Pi in kiosk mode
```

---

## Example 124

**Intent:**
kids ministry check-in at church with name stickers and a code for parents to pick up

**Spec:**
```
Type:       Web application (child check-in)
Auth:       Volunteer login on check-in stations
Data model: Family(id, surname, phone)
            Child(id, family_id -> Family, name, birth_date, allergies)
            CheckIn(id, child_id -> Child, room, security_code, checked_in_at, checked_out_at)
Features:   - Find a family by phone number on a touchscreen
            - Check in each child to their age-group room
            - Print a name label for the child and a matching pickup label for the parent
            - Show allergies on the child's label
            - Check out only when the matching security code is scanned
Storage:    PostgreSQL
Tech stack: React, Node.js, Express, DYMO label printers
```

---

## Example 125

**Intent:**
chrome extension that makes websites easier for my dyslexic son to read

**Spec:**
```
Type:       Browser extension
Features:   - Switch page text to a dyslexia-friendly font such as OpenDyslexic
            - Increase letter and line spacing
            - Add a colored overlay tint chosen by the user
            - Highlight the current line under the mouse as a reading ruler
            - Remember settings per website
Storage:    chrome.storage.sync
Tech stack: JavaScript, Chrome Extension Manifest V3
```

---

## Example 126

**Intent:**
My student has cerebral palsy and can only press one big button. I want her to be able to type on the computer by scanning through letters.

**Spec:**
```
Type:       Desktop application (switch access)
Features:   - Show an on-screen keyboard grouped into rows
            - Highlight rows then letters one at a time at an adjustable speed
            - Select the highlighted item when the switch is pressed
            - Offer word prediction to reduce presses
            - Read out each selected letter or word
Tech stack: Python, PyQt6, pyttsx3, USB switch interface (keyboard key emulation)
```

---

## Example 127

**Intent:**
at our deaf club meetings we want the speaker's words shown on a big screen as captions live

**Spec:**
```
Type:       Web application (live captioning)
Features:   - Capture audio from the room microphone
            - Transcribe speech to text in real time
            - Show captions in large high-contrast text on a projector
            - Let viewers on their own phones follow the captions via a link
            - Save a transcript after the meeting
Tech stack: Python, faster-whisper, WebSockets, FastAPI, HTML/CSS
```

---

## Example 128

**Intent:**
charge my EV only when electricity is cheapest at night

**Spec:**
```
Type:       Scheduled script (EV smart charging)
Features:   - Fetch tomorrow's hourly electricity prices each evening
            - Pick the cheapest hours needed to reach the target charge by 7 am
            - Start and stop the charger through its OCPP or local API
            - Skip charging if the car is already above the target
            - Send a summary of planned hours and cost
Input:      Target state of charge, battery size in kWh, charger power
Tech stack: Python, Nord Pool price API, OCPP 1.6 (ocpp library), cron
```

---

## Example 129

**Intent:**
Heat pump efficiency monitoring - want to see the COP each day

**Spec:**
```
Type:       Data dashboard (heat pump monitoring)
Data model: Reading(id, electrical_power_w, flow_temp_c, return_temp_c, flow_rate_lpm, outdoor_temp_c, recorded_at)
Features:   - Read electrical input from an energy meter over Modbus
            - Read flow and return temperatures and flow rate
            - Calculate heat output and live COP
            - Show daily COP against outdoor temperature
            - Compare efficiency between months
Storage:    InfluxDB
Tech stack: Raspberry Pi, Python, pymodbus, Telegraf, Grafana
```

---

## Example 130

**Intent:**
tell me when power goes out at my holiday house

**Spec:**
```
Type:       IoT system (power outage alert)
Features:   - Send a heartbeat from a device on mains power every minute
            - Detect a power cut when the heartbeat stops for 5 minutes
            - Send a notification on power loss and when power returns
            - Report the outage duration
Tech stack: ESP8266, Arduino (C++), healthchecks.io, Telegram notifications
```

---

## Example 131

**Intent:**
sump pump in basement, alert me if it runs too much or water gets high

**Spec:**
```
Type:       IoT system (sump pump monitoring)
Data model: PumpCycle(id, started_at, ended_at)
            LevelAlarm(id, level, triggered_at)
Features:   - Detect pump running from its current draw with a CT sensor
            - Count pump cycles per hour
            - Alert when cycles exceed 10 per hour
            - Raise a high water alarm from a backup float switch
            - Send a daily summary of runs
Storage:    SQLite
Tech stack: ESP32, ESPHome, Home Assistant
```

---

## Example 132

**Intent:**
bird feeder cam that tells me which birds came

**Spec:**
```
Type:       Machine learning model (bird species recognition)
Data model: Sighting(id, species, confidence, image_path, seen_at)
Features:   - Detect motion at the feeder and capture images
            - Classify the bird species with an image model
            - Save sightings with species, confidence and a cropped photo
            - Show a daily list and gallery of visitors
            - Send a notification for rare species
Storage:    SQLite, local image folder
Tech stack: Raspberry Pi 5, Python, picamera2, TensorFlow Lite (pretrained bird classifier)
```

---

## Example 133

**Intent:**
sauna is ready notification

**Spec:**
```
Type:       IoT system (sauna monitoring)
Features:   - Read sauna temperature with a high-temperature thermocouple
            - Send a notification when it reaches the chosen temperature
            - Show the current temperature on a phone
            - Warn if the heater has been on for more than 3 hours
Tech stack: ESP32, MAX6675 thermocouple module, ESPHome, Home Assistant
```

---

## Example 134

**Intent:**
my workshop has a wood stove, i want to know the flue temperature so i dont get a chimney fire

**Spec:**
```
Type:       IoT system (stove monitoring)
Features:   - Read flue temperature with a K-type thermocouple
            - Show the burn zone (too cold, ideal, too hot) on an LED bar
            - Sound a buzzer above 400 C
            - Log temperature every 30 seconds for later viewing
Tech stack: Arduino Uno, MAX31855 thermocouple amplifier, Arduino (C++), SD card module
```

---

## Example 135

**Intent:**
wine cellar temp and humidity log

**Spec:**
```
Type:       IoT system (cellar monitoring)
Features:   - Read temperature and humidity every 15 minutes
            - Store readings on a free cloud channel
            - Show charts of the last 30 days
            - Email when temperature goes above 16 C
Tech stack: ESP8266, DHT22, ThingSpeak, MATLAB analysis email alerts
```

---

## Example 136

**Intent:**
control each radiator seperately, bedrooms colder at night

**Spec:**
```
Type:       IoT system (zoned heating)
Data model: Zone(id, name, trv_device_id)
            ZoneSchedule(id, zone_id -> Zone, day_of_week, start_time, target_c)
Features:   - Control smart thermostatic radiator valves in each room
            - Follow a separate weekly schedule per room
            - Drop bedrooms to 16 C at night and warm them before waking
            - Turn a radiator down when its room's window is open
            - Show all rooms and targets on one dashboard
Tech stack: Zigbee TRVs, Zigbee2MQTT, Home Assistant, Better Thermostat integration
```

---

## Example 137

**Intent:**
koi pond pump and air pump, want alerts if they stop, fish die fast

**Spec:**
```
Type:       IoT system (pond monitoring)
Features:   - Monitor the water pump and air pump current with CT sensors
            - Read water temperature with a waterproof probe
            - Send an urgent alert if either pump stops for 2 minutes
            - Warn when water temperature goes above 28 C
            - Show pump status and temperature history
Tech stack: ESP32, ESPHome, Home Assistant, Pushover
```

---

## Example 138

**Intent:**
lawn sprinkler controller with phone app

**Spec:**
```
Type:       IoT system (irrigation control)
Features:   - Drive 6 sprinkler zone valves with 24 VAC relays
            - Run zones on weekly programs
            - Adjust watering time by a weather-based percentage
            - Start zones manually from a phone
            - Pause watering after rain
Tech stack: OpenSprinkler firmware, ESP8266, OpenSprinkler mobile app, OpenWeatherMap
```

---

## Example 139

**Intent:**
e ink screen next to front door with weather and whether to take umbrella

**Spec:**
```
Type:       IoT system (status display)
Features:   - Wake every 30 minutes from deep sleep
            - Fetch today's forecast and rain probability
            - Show temperature, an icon and "take an umbrella" when rain probability is above 50 percent
            - Show the battery level in a corner
Tech stack: ESP32, Waveshare 4.2 inch e-paper, Arduino (C++), Open-Meteo API
```

---

## Example 140

**Intent:**
care home carers need to log what each resident drinks during the day, they forget to write it down and residents get dehydrated

**Spec:**
```
Type:       Mobile application with backend
Auth:       Carer login with PIN on shared tablets; manager login (email + password)
Data model: Resident(id, name, room, daily_target_ml)
            FluidEntry(id, resident_id -> Resident, amount_ml, drink_type, recorded_by, recorded_at)
Features:   - Log a drink for a resident with two taps
            - Show each resident's total against their daily target
            - Highlight residents under 50 percent of target by 2 pm
            - Alert the shift lead about residents at risk
            - Produce a daily fluid chart per resident for nursing notes
API:        REST
            GET  /residents
            POST /residents/{id}/fluids
            GET  /residents/{id}/fluids?date={date}
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI
```

---

## Example 141

**Intent:**
video call device for my nan that is just one big button, no menus

**Spec:**
```
Type:       IoT system (simplified video calling)
Features:   - Show a photo of each family member as a large button on a touchscreen
            - Start a video call when a photo is pressed
            - Auto-answer calls from approved family members
            - Keep the screen on a clock and photo slideshow when idle
            - Let family manage contacts remotely
Tech stack: Raspberry Pi 5, 7 inch touchscreen, USB webcam, Python, Jitsi Meet (self-hosted)
```

---

## Example 142

**Intent:**
gps tracker in my dads shoe because he wanders off (alzheimers)

**Spec:**
```
Type:       IoT system (personal GPS tracking)
Data model: Wearer(id, name)
            Location(id, wearer_id -> Wearer, lat, lon, accuracy_m, recorded_at)
            SafeZone(id, wearer_id -> Wearer, center_lat, center_lon, radius_m)
Features:   - Report GPS location every 2 minutes over LTE-M
            - Alert family when he leaves the safe zone around home
            - Show his live location on a map
            - Increase reporting rate to every 15 seconds while outside the zone
            - Warn when the battery is below 20 percent
API:        MQTT
            tracker/{wearer_id}/location
Storage:    PostgreSQL with PostGIS
Tech stack: nRF9160 tracker, Zephyr RTOS, EMQX, Python, FastAPI, Leaflet
```

---

## Example 143

**Intent:**
for my deaf mum, make lights flash when someone rings the doorbell or the baby monitor goes off

**Spec:**
```
Type:       IoT system (accessibility alerts)
Features:   - Detect doorbell presses and baby monitor sound alerts
            - Flash the living room and kitchen lights in a distinct colour for each event
            - Vibrate a wearable pager
            - Send a phone notification with the event type
Tech stack: Home Assistant, Philips Hue bulbs, Zigbee doorbell, Node-RED
```

---

## Example 144

**Intent:**
Map app of restaurants and shops with wheelchair access info that users can add

**Spec:**
```
Type:       Mobile application with backend
Auth:       Sign in with Google or Apple
Data model: Place(id, name, lat, lon, category)
            AccessReport(id, place_id -> Place, user_id -> User, step_free_entrance, accessible_toilet, door_width_cm, photo_url, created_at)
            User(id, display_name)
Features:   - Show nearby places on a map with an accessibility rating
            - Let users submit access details with photos
            - Filter places by step-free entrance or accessible toilet
            - Combine multiple reports into a summary per place
            - Import existing data from OpenStreetMap wheelchair tags
API:        REST
            GET  /places?lat={lat}&lon={lon}
            POST /places/{id}/reports
Storage:    PostgreSQL with PostGIS
Tech stack: React Native, MapLibre, Node.js, Express, Overpass API
```

---

## Example 145

**Intent:**
train model to read sign language alphabet from webcam

**Spec:**
```
Type:       Machine learning model (gesture classification)
Features:   - Extract 21 hand landmarks per frame with MediaPipe
            - Collect labelled landmark samples for each letter
            - Train a classifier on landmark coordinates
            - Show the predicted letter live over the webcam image
            - Build words when a letter is held steady for 1 second
Input:      Webcam video, labelled landmark dataset (CSV)
Tech stack: Python, MediaPipe Hands, scikit-learn, OpenCV
```

---

## Example 146

**Intent:**
a device that reads my post out loud, i lost most of my sight

**Spec:**
```
Type:       IoT system (assistive reading device)
Features:   - Capture a photo of a letter placed under a fixed camera when a big button is pressed
            - Run OCR on the image
            - Read the text aloud with clear speech
            - Let the user pause and repeat with a second button
            - Say "no text found" if OCR fails
Tech stack: Raspberry Pi 4, Raspberry Pi Camera Module 3, Python, Tesseract OCR, Piper TTS
```

---

## Example 147

**Intent:**
soldering iron auto off if i forget it

**Spec:**
```
Type:       IoT system (workshop safety)
Features:   - Detect the iron resting in its stand with a reed switch
            - Turn the iron off through a relay after 10 minutes in the stand
            - Turn it back on when lifted
            - Show remaining time on a small display
Tech stack: Arduino Nano, Arduino (C++), relay module, TM1637 display
```

---

## Example 148

**Intent:**
make timelapse video of my 3d prints, one frame per layer

**Spec:**
```
Type:       Plugin (3D printer timelapse)
Features:   - Take a snapshot at each layer change
            - Park the print head out of view before each snapshot
            - Render the frames into an MP4 when the print ends
            - Upload the video to a shared folder
Tech stack: OctoPrint, Octolapse plugin, Python, ffmpeg
```

---

## Example 149

**Intent:**
raspberry pi cluster - see temperature and load of all nodes in one place

**Spec:**
```
Type:       Infrastructure setup (cluster monitoring)
Features:   - Run an exporter on each node to expose CPU temperature, load and memory
            - Scrape all nodes every 15 seconds
            - Show a Grafana dashboard with one panel per node
            - Alert when any node is above 75 C or throttling
Tech stack: Prometheus, node_exporter, rpi_exporter, Grafana, Alertmanager
```

---

## Example 150

**Intent:**
shutdown my nas safely when the ups battery is low

**Spec:**
```
Type:       Infrastructure setup (UPS monitoring)
Features:   - Connect the UPS by USB to a Raspberry Pi running a NUT server
            - Share UPS status with the NAS and other machines on the network
            - Shut down the clients when battery is below 30 percent
            - Send a notification on power loss and restore
            - Power the machines back on when mains returns via Wake-on-LAN
Tech stack: Network UPS Tools (NUT), Raspberry Pi, Synology NAS NUT client, ntfy
```

---

## Example 151

**Intent:**
grain bin temperature cables, warn if grain is heating up

**Spec:**
```
Type:       IoT system (grain storage monitoring)
Data model: Bin(id, name, capacity_t)
            Cable(id, bin_id -> Bin, position)
            Reading(id, cable_id -> Cable, depth_m, temperature_c, read_at)
Features:   - Read temperatures from sensors at several depths on each cable
            - Send readings every hour over a cellular gateway
            - Detect hot spots rising more than 3 C in a day
            - Recommend turning on aeration fans when outside air is cooler
            - Show a heat map of each bin
Storage:    TimescaleDB
Tech stack: 1-Wire sensor cables, Raspberry Pi with LTE HAT, Python, Grafana
```

---

## Example 152

**Intent:**
greenhouse co2 enrichment controlled by sensor

**Spec:**
```
Type:       IoT system (greenhouse climate)
Features:   - Read CO2 levels with an NDIR sensor every 30 seconds
            - Open the CO2 solenoid when levels are below 800 ppm during daylight
            - Never inject when roof vents are open
            - Close the solenoid above 1200 ppm for safety
            - Log CO2, light and vent position
Tech stack: Arduino Mega, SCD30 sensor, Arduino (C++), light sensor, relay module
```

---

## Example 153

**Intent:**
fish farm ponds oxygen level, need aerators to turn on automatically at night

**Spec:**
```
Type:       IoT system (aquaculture monitoring)
Data model: Pond(id, name, min_do_mgl)
            Reading(id, pond_id -> Pond, dissolved_oxygen_mgl, water_temp_c, read_at)
            AeratorEvent(id, pond_id -> Pond, state, changed_at)
Features:   - Read dissolved oxygen and water temperature probes every 5 minutes
            - Start the aerator when oxygen falls below the pond's minimum
            - Stop it when oxygen recovers above the minimum plus 1 mg/L
            - Send an SMS if oxygen keeps falling with the aerator on
            - Show trends for all ponds
Storage:    InfluxDB
Tech stack: Industrial PLC with Modbus, Raspberry Pi gateway, Node-RED, InfluxDB, Twilio SMS API
```

---

## Example 154

**Intent:**
chicken barn ammonia sensor

**Spec:**
```
Type:       IoT system (poultry house monitoring)
Features:   - Read ammonia concentration with an electrochemical NH3 sensor
            - Increase ventilation fan speed above 20 ppm
            - Alert the farmer above 25 ppm
            - Log readings with barn temperature and humidity
Tech stack: ESP32, ESPHome, Home Assistant
```

---

## Example 155

**Intent:**
count the eggs my hens lay automatically

**Spec:**
```
Type:       IoT system (egg counting)
Data model: EggEvent(id, nest_box, detected_at)
Features:   - Detect eggs rolling down the collection tray with an IR break-beam sensor
            - Count eggs per nest box per day
            - Show daily and weekly totals on a web page
            - Alert when the daily count drops by more than half
Storage:    SQLite
Tech stack: Raspberry Pi Zero W, Python, gpiozero, Flask
```

---

## Example 156

**Intent:**
coffee shipping containers humidity tracking across ocean

**Spec:**
```
Type:       IoT system (container monitoring)
Data model: Container(id, number, cargo, voyage)
            Reading(id, container_id -> Container, humidity_pct, temperature_c, lat, lon, recorded_at)
Features:   - Log humidity and temperature every 15 minutes inside the container
            - Buffer readings while out of coverage at sea
            - Upload buffered readings over satellite or cellular when available
            - Alert when humidity is above 70 percent for 6 hours (mould risk)
            - Show the voyage route with readings on a map
Storage:    TimescaleDB
Tech stack: Battery-powered tracker with nRF9160, Nordic nRF Cloud, Python, FastAPI, Leaflet
```

---

## Example 157

**Intent:**
fuel log app for our 15 trucks, drivers enter liters and km

**Spec:**
```
Type:       Mobile application with backend
Auth:       Driver login (employee number + PIN)
Data model: Truck(id, plate)
            FuelEntry(id, truck_id -> Truck, driver_id, litres, odometer_km, cost, station, filled_at, receipt_photo_url)
Features:   - Let drivers log a fill-up with a receipt photo
            - Calculate litres per 100 km per truck
            - Flag entries where consumption is far above normal
            - Show monthly fuel cost per truck
            - Export entries to Excel for accounting
API:        REST
            POST /fuel-entries
            GET  /trucks/{id}/consumption
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI, AWS S3
```

---

## Example 158

**Intent:**
tire pressure check for trailers sends alert to driver

**Spec:**
```
Type:       IoT system (tire pressure monitoring)
Features:   - Receive pressure and temperature from BLE valve-cap sensors on each tire
            - Show all tires on a cab display
            - Alert the driver when a tire is 15 percent below its target pressure
            - Alert on fast pressure loss
            - Upload readings to the fleet server when parked at the depot
Tech stack: BLE TPMS sensors, Raspberry Pi with touchscreen, Python, bleak, MQTT
```

---

## Example 159

**Intent:**
plan the best order to deliver 30 parcels a day from a csv of addresses

**Spec:**
```
Type:       Command-line tool (route optimization)
Features:   - Read delivery addresses from a CSV
            - Geocode addresses to coordinates
            - Build a travel time matrix with a routing engine
            - Solve the order with a vehicle routing solver
            - Output the ordered stop list and a Google Maps link
Input:      CSV of addresses, depot address, optional delivery time windows
Tech stack: Python, OR-Tools, OSRM, geopy
```

---

## Example 160

**Intent:**
pick to light system for warehouse shelves

**Spec:**
```
Type:       IoT system (pick-to-light)
Data model: Location(id, shelf, bin, led_index)
            PickTask(id, order_id, location_id -> Location, quantity, picked_at)
Features:   - Light the bin LED and show the quantity for each item in the current order
            - Confirm each pick with a button on the bin
            - Move to the next order when all lights are confirmed
            - Report pick rate and errors per picker
API:        MQTT
            ptl/{shelf}/command
            ptl/{shelf}/confirm
Storage:    PostgreSQL
Tech stack: ESP32 shelf controllers, WS2812 LED strips, Mosquitto, Python, FastAPI
```

---

## Example 161

**Intent:**
we are a small ngo and keep missing grant deadlines, i want to see all grants we applied or want to apply and get reminder before deadline

**Spec:**
```
Type:       Web application (grant tracker)
Auth:       Staff login (email + password)
Data model: Funder(id, name, website)
            Grant(id, funder_id -> Funder, title, amount, deadline, status, owner)
            Report(id, grant_id -> Grant, due_date, submitted)
Features:   - Track grants from idea to submitted, awarded or rejected
            - Show upcoming deadlines on a calendar
            - Email reminders 14, 7 and 2 days before deadlines
            - Track reporting deadlines for awarded grants
            - Show total requested and awarded per year
Storage:    PostgreSQL
Tech stack: Python, Django, Celery (scheduled reminders)
```

---

## Example 162

**Intent:**
raffle tickets for our charity gala sold on phones and pick winner

**Spec:**
```
Type:       Web application (raffle)
Auth:       Seller login for volunteers
Data model: Ticket(id, number, buyer_name, buyer_phone, sold_by, paid, sold_at)
            Prize(id, name, donor, winner_ticket_id -> Ticket)
Features:   - Sell numbered tickets on a phone and record the buyer
            - Text the buyer their ticket numbers
            - Show tickets sold and money raised live
            - Draw winners randomly for each prize
            - Display winners on the big screen
Storage:    PostgreSQL
Tech stack: Python, FastAPI, HTMX, Twilio SMS API
```

---

## Example 163

**Intent:**
council meeting agendas and minutes should be published online automatically

**Spec:**
```
Type:       Web application (document publishing)
Auth:       Clerk login (email + password)
Data model: Meeting(id, committee, date, location, status)
            Document(id, meeting_id -> Meeting, kind, file_url, published_at)
Features:   - Let the clerk create meetings and upload agendas and minutes as PDF
            - Publish documents on a public calendar page
            - Send email alerts to subscribers when a new agenda is published
            - Search past minutes by keyword
            - Keep an archive by committee and year
Storage:    PostgreSQL, S3 for PDFs
Tech stack: Python, Django, PostgreSQL full-text search
```

---

## Example 164

**Intent:**
residents parking permit online apply

**Spec:**
```
Type:       Web application (permit application)
Auth:       Resident login with email verification
Data model: Resident(id, name, address, email)
            Vehicle(id, resident_id -> Resident, plate)
            Permit(id, vehicle_id -> Vehicle, zone, valid_from, valid_to, status)
Features:   - Let residents apply for a zone permit with proof of address
            - Check the address is inside the permit zone
            - Take payment online
            - Issue a digital permit linked to the number plate
            - Let parking wardens look up a plate
Storage:    PostgreSQL
Tech stack: TypeScript, NestJS, React, Stripe
```

---

## Example 165

**Intent:**
bot that reminds me which bin to put out tonight

**Spec:**
```
Type:       Bot (waste collection reminder)
Features:   - Look up collection days for the user's address from the council's schedule
            - Send a reminder the evening before collection
            - Say which bins (general, recycling, garden) go out
            - Handle holiday schedule changes
Tech stack: Python, python-telegram-bot, BeautifulSoup (council website), APScheduler
```

---

## Example 166

**Intent:**
library chatbot that answers opening hours and if a book is available

**Spec:**
```
Type:       Chatbot (library help)
Features:   - Answer questions about opening hours for each branch
            - Search the catalogue and say if a title is available and where
            - Explain how to renew loans
            - Hand over to a librarian by email when it cannot answer
API:        I: REST
            POST /chat
Tech stack: Python, FastAPI, Koha REST API, small FAQ intent matcher
```

---

## Example 167

**Intent:**
scan tickets at the museum door on a phone

**Spec:**
```
Type:       Mobile application (ticket scanning)
Auth:       Staff login (email + password)
Data model: Ticket(id, qr_code, ticket_type, valid_date, scanned_at, scanned_by)
Features:   - Scan a ticket's QR code with the phone camera
            - Show a large green or red result
            - Reject tickets already scanned or for another date
            - Work offline with today's tickets downloaded
            - Show the count of visitors admitted
Storage:    On-device SQLite synced with the ticketing database
Tech stack: Flutter, mobile_scanner, Firebase
```

---

## Example 168

**Intent:**
sermon audio uploads automatically become a podcast

**Spec:**
```
Type:       Webhook service
Features:   - Watch a cloud folder for new sermon recordings
            - Convert recordings to MP3 and normalise volume
            - Read the speaker, title and date from the file name
            - Add an episode to the podcast RSS feed
            - Publish the feed so it updates in Apple Podcasts and Spotify
Tech stack: Python, Flask, ffmpeg, Dropbox webhooks, S3 static hosting
```

---

## Example 169

**Intent:**
ring the church bells automatically for services and weddings

**Spec:**
```
Type:       IoT system (bell automation)
Data model: RingEvent(id, pattern, start_at, repeat_weekly)
Features:   - Drive bell striker solenoids through relays
            - Store ringing patterns such as call to worship and wedding peal
            - Schedule ringing for services and special events
            - Keep accurate time with an RTC and NTP
            - Let the verger trigger a pattern manually from a phone
Storage:    SQLite
Tech stack: Raspberry Pi, Python, DS3231 RTC, Flask
```

---

## Example 170

**Intent:**
CO2 incubator in the cell culture lab, alert if CO2 or temp drifts

**Spec:**
```
Type:       IoT system (lab incubator monitoring)
Features:   - Read incubator CO2 and temperature from its analog outputs
            - Alert by email and SMS if CO2 leaves 4.5-5.5 percent
            - Alert if temperature leaves 36.5-37.5 C
            - Log readings for GLP audits
Tech stack: Raspberry Pi, ADS1115, Python, InfluxDB, Grafana alerting
```

---

## Example 171

**Intent:**
chemical inventory for our school lab with the safety data sheets

**Spec:**
```
Type:       Web application (chemical inventory)
Auth:       Teacher and technician login (email + password)
Data model: Chemical(id, name, cas_number, hazard_class, sds_url)
            Container(id, chemical_id -> Chemical, location, quantity, unit, expiry_date)
Features:   - Record each container with its location and quantity
            - Link the safety data sheet to each chemical
            - Show hazard pictograms and storage incompatibilities
            - Warn about expired or low stock items
            - Print an inventory list for fire service visits
Storage:    PostgreSQL
Tech stack: PHP, Laravel, Livewire
```

---

## Example 172

**Intent:**
battery monitor for my campervan leisure battery

**Spec:**
```
Type:       IoT system (12V battery monitoring)
Features:   - Read voltage, current and state of charge from a shunt monitor over Bluetooth
            - Show solar charge and battery status on a small dashboard
            - Warn when state of charge is below 40 percent
            - Log daily energy in and out
Tech stack: Victron SmartShunt, Raspberry Pi, Python, victron-ble, Grafana
```

---

## Example 173

**Intent:**
boat bilge alarm when im not on board

**Spec:**
```
Type:       IoT system (marine monitoring)
Features:   - Detect high bilge water with a float switch
            - Count bilge pump cycles
            - Send an SMS alert over 4G when water is high
            - Report battery voltage daily
Tech stack: ESP32, SIM7600 LTE module, Arduino (C++)
```

---

## Example 174

**Intent:**
Our neighbourhood wants a map of air pollution with cheap sensors on each house

**Spec:**
```
Type:       IoT system (citizen air quality network)
Data model: Station(id, owner_email, lat, lon)
            Reading(id, station_id -> Station, pm25, pm10, temperature_c, humidity_pct, recorded_at)
Features:   - Send PM2.5 and PM10 every 2.5 minutes from each home sensor
            - Correct particulate readings for high humidity
            - Show all stations on a public map with colour-coded AQI
            - Show 24-hour averages per station
            - Detect and hide stations reporting broken values
API:        REST
            POST /api/push
            GET  /api/stations
            GET  /api/stations/{id}/readings
Storage:    TimescaleDB
Tech stack: ESP8266 with SDS011 sensor (sensor.community firmware), Python, FastAPI, Leaflet
```

---

## Example 175

**Intent:**
radon level in my basement

**Spec:**
```
Type:       IoT system (radon monitoring)
Features:   - Read radon level from a BLE radon detector every hour
            - Show short-term and long-term averages
            - Alert when the 7-day average exceeds 100 Bq/m3
            - Turn on the extraction fan when it is high
Tech stack: Airthings Wave, Home Assistant, Bluetooth proxy (ESPHome)
```

---

## Example 176

**Intent:**
construction site noise monitor neighbours complained

**Spec:**
```
Type:       IoT system (noise monitoring)
Data model: NoiseReading(id, laeq_db, lmax_db, recorded_at)
            Exceedance(id, started_at, ended_at, max_db)
Features:   - Measure LAeq and LMax over 1-minute intervals with a calibrated microphone
            - Alert the site manager when levels exceed the permitted limit
            - Record exceedances with start, end and peak
            - Publish a daily report for the council
Storage:    InfluxDB
Tech stack: Raspberry Pi, USB measurement microphone, Python, NumPy, Grafana
```

---

## Example 177

**Intent:**
bike counter on the cycle path for the city

**Spec:**
```
Type:       IoT system (traffic counting)
Features:   - Detect bikes with an inductive loop or radar sensor
            - Count bikes per direction per 15 minutes
            - Show a public display with today's and this year's total
            - Send counts to the city open data portal every hour
API:        MQTT
            city/bikecounter/{location}/count
Storage:    TimescaleDB
Tech stack: ESP32, Arduino (C++), LED matrix display, Node-RED
```

---

## Example 178

**Intent:**
show free parking spaces at our small car park on a sign at the entrance

**Spec:**
```
Type:       IoT system (parking occupancy)
Data model: Space(id, number, occupied, changed_at)
Features:   - Detect a car in each space with a magnetic or ultrasonic sensor
            - Send status changes to a central controller
            - Show the number of free spaces on an LED sign at the entrance
            - Show a live map of spaces on a web page
API:        MQTT
            carpark/space/{id}
Tech stack: ESP32 nodes, ESP-NOW, Raspberry Pi controller, Python, P10 LED panel
```

---

## Example 179

**Intent:**
book the EV chargers in our office car park

**Spec:**
```
Type:       Web application (resource booking)
Auth:       Employee login with Microsoft SSO
Data model: Charger(id, name, power_kw)
            Booking(id, charger_id -> Charger, user_id -> User, starts_at, ends_at, checked_in)
            User(id, name, email)
Features:   - Book a charger in 2-hour slots
            - Release a booking if the user does not plug in within 15 minutes
            - Notify the user 15 minutes before their slot ends
            - Limit each user to 2 bookings per week
            - Show charger usage stats to facilities
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Blazor, Azure AD
```

---

## Example 180

**Intent:**
soo i want to like monitor my sourdough starter rising in the jar lol, how high it gets and when

**Spec:**
```
Type:       IoT system (fermentation monitoring)
Data model: Feed(id, fed_at)
            HeightReading(id, feed_id -> Feed, height_mm, temperature_c, read_at)
Features:   - Measure the starter height with a time-of-flight sensor in the jar lid
            - Record the room temperature
            - Mark a new feeding with a button press
            - Detect the peak rise time after each feeding
            - Show the rise curve on a phone page
Storage:    SQLite
Tech stack: ESP32, VL53L0X sensor, Arduino (C++), Flask
```

---

## Example 181

**Intent:**
hi i am from brazil, i want to make my coffee machine turn on alone at 6:30 everyday before i wake up

**Spec:**
```
Type:       IoT system (home automation)
Features:   - Switch the coffee machine on with a smart plug at 6:30 on weekdays
            - Use a different time on weekends
            - Turn it off after 45 minutes to save energy
            - Skip mornings when the alarm is disabled
Tech stack: Tasmota smart plug, Home Assistant, Home Assistant companion app (next alarm sensor)
```

---

## Example 182

**Intent:**
the river club needs to know the water temperature and flow before rowing sessions

**Spec:**
```
Type:       IoT system (water conditions monitoring)
Features:   - Measure water temperature with a submerged probe
            - Pull river flow from the national hydrology API
            - Show a go, caution or no-go status based on club rules
            - Send the status to the members' WhatsApp group each morning
Tech stack: ESP32, DS18B20, Python, Twilio WhatsApp API, cron
```

---

## Example 183

**Intent:**
water meter that tells me if a pipe is leaking

**Spec:**
```
Type:       IoT system (water usage monitoring)
Data model: FlowReading(id, litres, recorded_at)
            LeakAlert(id, started_at, litres_lost)
Features:   - Count pulses from a flow sensor on the main water pipe
            - Calculate litres per minute and daily usage
            - Flag a leak when water flows continuously for more than 2 hours
            - Close a motorised shut-off valve on a confirmed leak
            - Show usage per day on a dashboard
Storage:    InfluxDB
Tech stack: ESP32, YF-B10 flow sensor, ESPHome, Home Assistant
```

---

## Example 184

**Intent:**
my farm well water level going down in summer, want to watch it

**Spec:**
```
Type:       IoT system (groundwater level monitoring)
Features:   - Measure the water depth with a submersible pressure transducer
            - Convert pressure to metres of water above the sensor
            - Send a reading every hour over Wi-Fi
            - Chart the level over months
            - Alert when the level is within 2 metres of the pump intake
Tech stack: ESP32, 4-20 mA pressure transducer, ADS1115, MicroPython, ThingsBoard
```

---

## Example 185

**Intent:**
generator at our rural clinic, want to know when it starts and how much fuel is left

**Spec:**
```
Type:       IoT system (generator monitoring)
Data model: GeneratorRun(id, started_at, stopped_at, runtime_min)
            FuelReading(id, level_pct, read_at)
Features:   - Detect generator running from its output voltage
            - Log run times and total hours
            - Read the fuel tank level with an ultrasonic sensor
            - Send an SMS when fuel is below 25 percent
            - Remind staff when the 250-hour service is due
Storage:    SQLite
Tech stack: Arduino Mega, SIM800L GSM module, Arduino (C++)
```

---

## Example 186

**Intent:**
curtains open by themself when alarm goes in morning

**Spec:**
```
Type:       IoT system (home automation)
Features:   - Read the next alarm time from the phone
            - Open motorised curtains 10 minutes before the alarm
            - Open slowly over 5 minutes
            - Close the curtains at sunset
Tech stack: Home Assistant, Zigbee curtain motor, Home Assistant companion app
```

---

## Example 187

**Intent:**
build smart mirror with calendar, weather and news

**Spec:**
```
Type:       IoT system (smart mirror)
Features:   - Show the time, date and weather forecast
            - Show today's events from Google Calendar
            - Show news headlines that rotate every 10 seconds
            - Turn the display off when no one is in front of it using a PIR sensor
Tech stack: Raspberry Pi 4, MagicMirror² (Node.js), MMM-PIR-Sensor module, two-way mirror with monitor
```

---

## Example 188

**Intent:**
airbnb lockbox, new code for each guest automatically

**Spec:**
```
Type:       Webhook service (smart lock codes)
Data model: Reservation(id, guest_name, guest_phone, check_in, check_out, door_code)
Features:   - Receive new reservations from the booking platform calendar
            - Generate a unique 6-digit code per reservation
            - Program the code on the smart lock valid only from check-in to check-out
            - Send the code to the guest by SMS on the morning of arrival
            - Delete the code after check-out
Storage:    SQLite
Tech stack: Python, FastAPI, iCal feed parser, Z-Wave lock via Home Assistant API, Twilio
```

---

## Example 189

**Intent:**
noise sensor in airbnb to catch parties without cameras

**Spec:**
```
Type:       IoT system (privacy-safe occupancy monitoring)
Features:   - Measure sound level in decibels without recording audio
            - Count connected Wi-Fi devices as a crowd estimate
            - Alert the host when noise is above 75 dB for 10 minutes after 10 pm
            - Send a polite automatic message to the guest
Tech stack: ESP32, INMP441 I2S microphone, Arduino (C++), Twilio
```

---

## Example 190

**Intent:**
turn on lights when I sit at my desk, motion sensor doesnt work cause I sit still

**Spec:**
```
Type:       IoT system (presence detection)
Features:   - Detect a seated person with a 24 GHz mmWave presence sensor
            - Turn the desk lights on when presence is detected
            - Keep the lights on while the person is still
            - Turn off 2 minutes after presence ends
Tech stack: ESP32, LD2410 mmWave sensor, ESPHome, Home Assistant
```

---

## Example 191

**Intent:**
cat flap that only lets my cat in not the neighbours fat cat

**Spec:**
```
Type:       IoT system (pet access control)
Data model: Pet(id, name, chip_id)
            FlapEvent(id, pet_id -> Pet, direction, occurred_at)
Features:   - Read the cat's microchip with a 134.2 kHz RFID reader
            - Unlock the flap with a servo only for registered chips
            - Always allow cats to go out
            - Log comings and goings
            - Show whether the cat is in or out on a phone
Tech stack: ESP32, FDX-B RFID reader module, servo, ESPHome, Home Assistant
```

---

## Example 192

**Intent:**
pet feeder schedule, cat gets fat

**Spec:**
```
Type:       IoT system (pet feeder)
Features:   - Dispense a set portion with a servo-driven auger at scheduled times
            - Weigh each portion with a load cell
            - Log meals and grams per day
            - Let me change the schedule from my phone
Tech stack: ESP32, HX711 load cell, ESPHome, Home Assistant
```

---

## Example 193

**Intent:**
tortoise enclosure heat lamp and uv on timer, temp must be right

**Spec:**
```
Type:       IoT system (reptile habitat control)
Features:   - Read basking spot and cool end temperatures
            - Switch the UV lamp on a 12-hour day schedule
            - Switch the heat lamp to keep the basking spot at 32 C
            - Turn everything off at night with a night minimum of 15 C
            - Alert if any temperature is out of range
Tech stack: Arduino Uno, DS18B20 probes, relay module, Arduino (C++)
```

---

## Example 194

**Intent:**
count how far my hamster runs every night

**Spec:**
```
Type:       IoT system (activity tracking)
Data model: Rotation(id, counted_at)
            NightSummary(id, date, distance_m, top_speed_kmh)
Features:   - Count wheel rotations with a hall sensor and magnet
            - Convert rotations to distance using the wheel diameter
            - Calculate top speed per night
            - Post a nightly summary to a chat
Storage:    SQLite
Tech stack: Raspberry Pi Zero, Python, gpiozero, Discord webhook
```

---

## Example 195

**Intent:**
resin printer needs to be warm or prints fail in my cold garage

**Spec:**
```
Type:       IoT system (3D printer enclosure heating)
Features:   - Read the enclosure temperature
            - Run a small heater to keep 25 C
            - Cut the heater above 35 C as a safety limit
            - Show the temperature on a small display
Tech stack: Arduino Nano, DHT22, relay module, Arduino (C++)
```

---

## Example 196

**Intent:**
I have hundreds of resistors and chips in drawers and never know where anything is

**Spec:**
```
Type:       Web application (component inventory)
Data model: Location(id, cabinet, drawer)
            Part(id, name, category, value, package, quantity, location_id -> Location, datasheet_url)
Features:   - Add parts with category, value, package and quantity
            - Search parts by name or value
            - Show which drawer each part is in
            - Light an LED on the matching drawer when a part is found
            - Warn when stock falls below a minimum
Storage:    SQLite
Tech stack: Python, Flask, ESP8266 with addressable LEDs on the drawers
```

---

## Example 197

**Intent:**
hospital entrance touchscreen that shows you how to get to the department

**Spec:**
```
Type:       Web application (wayfinding kiosk)
Data model: Department(id, name, floor, building)
            Route(id, from_kiosk_id, department_id -> Department, steps, map_image_url)
Features:   - Let visitors search or pick a department
            - Show a floor map with the route highlighted
            - Show step-by-step directions
            - Send the directions to the visitor's phone with a QR code
            - Offer large text and multiple languages
Storage:    PostgreSQL
Tech stack: Vue.js, Node.js, SVG floor plans, Electron kiosk
```

---

## Example 198

**Intent:**
gym class schedule on TV at reception

**Spec:**
```
Type:       Web application (digital signage)
Features:   - Fetch today's classes from the gym booking system
            - Show the next classes with instructor and room
            - Show spaces left per class
            - Refresh every minute
Tech stack: JavaScript, Mindbody API, Raspberry Pi in Chromium kiosk mode
```

---

## Example 199

**Intent:**
screen at school pickup that shows which kids parents arrived for, like airport board

**Spec:**
```
Type:       Web application (school dismissal board)
Auth:       Staff login; parents use a family code
Data model: Student(id, name, class, family_code)
            PickupCall(id, student_id -> Student, called_at, released_at)
Features:   - Let parents tap "I'm here" on their phone or staff type the family code
            - Show called students on a large board grouped by class
            - Show called names on classroom screens
            - Mark students released when they leave
            - Clear the board at the end of pickup
Storage:    PostgreSQL
Tech stack: Node.js, Socket.IO, React
```

---

## Example 200

**Intent:**
barbershop walk in queue, customers see their place on phone

**Spec:**
```
Type:       Web application (walk-in queue)
Data model: Barber(id, name, is_working)
            QueueEntry(id, customer_name, phone, barber_id -> Barber, joined_at, served_at, status)
Features:   - Let customers join the queue by scanning a QR code
            - Let customers pick a barber or "any"
            - Show each customer their position and estimated wait
            - Text the customer when they are 2 places away
            - Show the queue on a TV in the shop
Storage:    Redis
Tech stack: Python, FastAPI, Twilio SMS API, HTMX
```

---

## Example 201

**Intent:**
Our festival wants cashless bars with wristbands that people top up

**Spec:**
```
Type:       Web application (cashless payments)
Auth:       Bar staff login on POS terminals; attendees register their wristband online
Data model: Wristband(id, nfc_uid, balance, owner_email)
            TopUp(id, wristband_id -> Wristband, amount, method, created_at)
            Purchase(id, wristband_id -> Wristband, bar_id, amount, items, created_at)
Features:   - Top up a wristband online or at a top-up booth
            - Charge purchases by tapping the wristband on an NFC reader
            - Work offline at bars and sync when the connection returns
            - Block lost wristbands and move the balance
            - Refund unused balances after the festival
API:        REST
            POST /topups
            POST /purchases
            POST /wristbands/{id}/block
Storage:    PostgreSQL
Tech stack: Android POS tablets with NFC, Kotlin, Go backend, Stripe
```

---

## Example 202

**Intent:**
vending machines tell me when snacks running low

**Spec:**
```
Type:       IoT system (vending telemetry)
Data model: Machine(id, location)
            Slot(id, machine_id -> Machine, product, capacity, sold_since_refill)
            Sale(id, slot_id -> Slot, amount, sold_at)
Features:   - Read sales from the vending controller over the MDB bus
            - Estimate remaining stock per slot
            - Send a restock list when slots are below 20 percent
            - Show sales per machine per day
            - Alert when a machine stops reporting
API:        MQTT
            vending/{machine_id}/sale
Storage:    PostgreSQL
Tech stack: Raspberry Pi with MDB interface board, Python, Mosquitto, Metabase
```

---

## Example 203

**Intent:**
my physio gave me exercises for my knee, i want an app that counts my reps with a sensor on my leg

**Spec:**
```
Type:       Mobile application (rehab tracking)
Data model: Exercise(id, name, target_reps, target_angle_deg)
            SessionLog(id, exercise_id -> Exercise, reps, max_angle_deg, done_at)
Features:   - Connect to a BLE motion sensor strapped to the leg
            - Count reps from the knee angle
            - Show the angle reached against the physio's target
            - Keep a log of each session
            - Share a weekly progress summary with the physiotherapist
Storage:    Local SQLite
Tech stack: Flutter, flutter_reactive_ble, Movesense or MetaMotion sensor
```

---

## Example 204

**Intent:**
analyze my cpap machine data from the sd card

**Spec:**
```
Type:       Data analysis script (sleep therapy)
Features:   - Read EDF files from the CPAP SD card
            - Extract nightly usage hours, AHI and mask leak rate
            - Plot AHI and usage over the last 90 days
            - Flag nights with usage under 4 hours or high leaks
            - Save a summary CSV
Input:      Path to the copied CPAP SD card folder
Tech stack: Python, pyedflib, pandas, matplotlib
```

---

## Example 205

**Intent:**
show my sons blood sugar from his dexcom on a little screen in the kitchen

**Spec:**
```
Type:       IoT system (glucose display)
Features:   - Fetch the latest glucose value from a Nightscout server every 5 minutes
            - Show the value and trend arrow in large digits
            - Turn the screen red for lows and yellow for highs
            - Beep for urgent low readings
            - Show "no data" if the reading is older than 15 minutes
Tech stack: ESP32 with TFT display (M5Stack), Arduino (C++), Nightscout API
```

---

## Example 206

**Intent:**
hand sanitizer dispensers count how many times used in each ward

**Spec:**
```
Type:       IoT system (hand hygiene compliance)
Data model: Dispenser(id, ward, location)
            Dispense(id, dispenser_id -> Dispenser, dispensed_at)
Features:   - Count each press of the dispenser with a micro switch
            - Send counts to the server in batches every 10 minutes
            - Show uses per ward per shift
            - Compare against patient contacts to estimate compliance
            - Alert facilities when a dispenser is likely empty
API:        MQTT
            hygiene/{ward}/{dispenser_id}/dispense
Storage:    TimescaleDB
Tech stack: ESP32-C3, Arduino (C++), Mosquitto, Grafana
```

---

## Example 207

**Intent:**
my mother lives alone, i want her to press a button every morning to say she is ok, if she doesnt i get a message

**Spec:**
```
Type:       IoT system (daily check-in)
Features:   - Light up a large button each morning at 9 am
            - Record the press and send "Mum checked in" to the family
            - Send a reminder beep at 10 am if not pressed
            - Alert family at 11 am if still not pressed
            - Allow a holiday mode
Tech stack: ESP32, big arcade button with LED, Arduino (C++), Telegram Bot API
```

---

## Example 208

**Intent:**
detect if the gas stove is left on and no one is in kitchen

**Spec:**
```
Type:       IoT system (kitchen safety)
Features:   - Detect a burner is on with a heat sensor above the stove
            - Detect presence in the kitchen with a motion sensor
            - Beep after 10 minutes of stove on with nobody in the kitchen
            - Close a gas shut-off valve after 20 minutes and notify family
Tech stack: Raspberry Pi, MLX90614 IR temperature sensor, PIR sensor, Python, motorised gas valve
```

---

## Example 209

**Intent:**
farmer wants to know the best hours to spray crops - no wind, no rain coming

**Spec:**
```
Type:       Web application (spray advisory)
Data model: Field(id, name, lat, lon, crop)
Features:   - Fetch hourly forecast for wind speed, rain and temperature per field
            - Mark each hour as good, marginal or bad for spraying
            - Detect temperature inversion risk at dawn
            - Show a 3-day spray window chart per field
            - Send a morning summary by email
Storage:    SQLite
Tech stack: Python, FastAPI, Open-Meteo API, Chart.js
```

---

## Example 210

**Intent:**
berry pickers bring crates to a scale and should get paid per kg

**Spec:**
```
Type:       Desktop application (harvest weighing)
Data model: Picker(id, name, badge_code)
            Weighing(id, picker_id -> Picker, crate_count, net_kg, weighed_at)
            PayRate(id, crop, rate_per_kg)
Features:   - Scan the picker's badge
            - Read the weight from a serial bench scale and subtract crate tare
            - Show the picker's total for the day
            - Print a receipt slip
            - Export weekly pay totals per picker
Storage:    SQLite
Tech stack: Python, PySide6, pyserial, ESC/POS receipt printer
```

---

## Example 211

**Intent:**
weigh sheep in race, read ear tag, store weight

**Spec:**
```
Type:       IoT system (livestock weighing)
Data model: Animal(id, eid_tag, mob, birth_date)
            Weighing(id, animal_id -> Animal, weight_kg, weighed_at)
Features:   - Read electronic ear tags with a Bluetooth EID reader
            - Read the stable weight from load bars
            - Save weight against the animal
            - Show weight gain since last weighing
            - Sort animals into draft groups by weight
Storage:    SQLite (on tablet), sync to cloud
Tech stack: Android tablet, Kotlin, Bluetooth serial, Tru-Test load bars
```

---

## Example 212

**Intent:**
customers want to track their parcel themselves

**Spec:**
```
Type:       Web application (shipment tracking)
Data model: Shipment(id, tracking_number, origin, destination, status, eta)
            TrackingEvent(id, shipment_id -> Shipment, status, location, occurred_at)
Features:   - Let customers look up a shipment by tracking number
            - Show a timeline of scan events
            - Show the van's position on a map on delivery day
            - Let customers subscribe to SMS updates
API:        REST
            GET  /track/{tracking_number}
            POST /track/{tracking_number}/subscribe
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, Mapbox, Twilio
```

---

## Example 213

**Intent:**
We need to prove our warehouse stays in temperature range in every corner for pharma storage

**Spec:**
```
Type:       IoT system (temperature mapping)
Data model: Logger(id, location_label, x_m, y_m, height_m)
            Reading(id, logger_id -> Logger, temperature_c, humidity_pct, recorded_at)
Features:   - Place loggers in a grid at three heights
            - Record temperature every 5 minutes for a 7-day mapping study
            - Find hot and cold spots and their maximum deviation
            - Generate a heat map of the floor
            - Produce a GDP mapping report as PDF
Storage:    PostgreSQL
Tech stack: BLE temperature loggers, Raspberry Pi gateway, Python, pandas, matplotlib
```

---

## Example 214

**Intent:**
volunteer drivers want to claim mileage back from charity

**Spec:**
```
Type:       Web application (expense claims)
Auth:       Volunteer login (email + password); finance approver role
Data model: Volunteer(id, name, bank_account)
            Trip(id, volunteer_id -> Volunteer, date, from_postcode, to_postcode, miles, purpose)
            Claim(id, volunteer_id -> Volunteer, month, total, status)
Features:   - Let volunteers log trips with start and end postcodes
            - Calculate miles with a mapping API
            - Group trips into a monthly claim at the set rate per mile
            - Let finance approve or query claims
            - Export approved claims for bank payment
Storage:    PostgreSQL
Tech stack: Python, Django, Google Distance Matrix API
```

---

## Example 215

**Intent:**
soup kitchen tablet to count meals served

**Spec:**
```
Type:       Mobile application (meal counting)
Features:   - Tap a large button for each meal served
            - Track separate counts for adults and children
            - Show the running total for today
            - Email the daily totals to the coordinator at closing
Storage:    On-device storage with Firebase sync
Tech stack: Flutter, Firebase Firestore
```

---

## Example 216

**Intent:**
Our county gets many Freedom of Information requests and needs to track the 20 day deadline

**Spec:**
```
Type:       Web application (FOI case tracking)
Auth:       Staff login with Microsoft SSO
Data model: Request(id, reference, requester_email, received_on, due_on, status, department)
            Response(id, request_id -> Request, sent_on, outcome, exemptions)
Features:   - Log requests with the received date
            - Calculate the statutory due date in working days
            - Assign requests to departments
            - Warn when a request is 5 days from due
            - Report on-time response rates
Storage:    PostgreSQL
Tech stack: C#, ASP.NET Core, Azure AD
```

---

## Example 217

**Intent:**
community hall bookings for birthday parties and clubs

**Spec:**
```
Type:       Web application (venue booking)
Auth:       Customer login (email + password); admin for the hall committee
Data model: Room(id, name, capacity, hourly_rate)
            Booking(id, room_id -> Room, customer_id -> Customer, starts_at, ends_at, purpose, status, deposit_paid)
            Customer(id, name, email, phone)
Features:   - Show availability on a calendar
            - Let customers request a booking
            - Let the committee approve bookings
            - Take a deposit online
            - Send the door code the day before
Storage:    PostgreSQL
Tech stack: PHP, Laravel, FullCalendar, Stripe
```

---

## Example 218

**Intent:**
residents ask the city to plant a tree in front of their house

**Spec:**
```
Type:       Web application (service request map)
Data model: TreeRequest(id, resident_email, address, lat, lon, preferred_species, status, created_at)
Features:   - Let residents pick a spot on a map and request a tree
            - Check the spot is on public land
            - Let staff approve and schedule planting
            - Show planted trees on a public map
            - Email residents when their tree is planted
Storage:    PostgreSQL with PostGIS
Tech stack: Python, GeoDjango, Leaflet
```

---

## Example 219

**Intent:**
show how long the queue is at each voting place

**Spec:**
```
Type:       Web application (wait time reporting)
Auth:       Poll worker login with a station code
Data model: PollingStation(id, name, address, lat, lon)
            WaitReport(id, station_id -> PollingStation, wait_minutes, reported_at)
Features:   - Let poll workers report the current wait time every 30 minutes
            - Show all stations on a map coloured by wait
            - Show the time of the last update
            - Suggest nearby stations with shorter waits where allowed
Storage:    PostgreSQL
Tech stack: Python, FastAPI, Leaflet, Redis cache
```

---

## Example 220

**Intent:**
research greenhouse, photograph plants each day and measure leaf area

**Spec:**
```
Type:       Data pipeline (plant phenotyping)
Data model: Plant(id, genotype, treatment, tray_position)
            Image(id, plant_id -> Plant, path, captured_at)
            Measurement(id, image_id -> Image, leaf_area_cm2, height_cm)
Features:   - Capture top and side images of each plant daily
            - Segment plant pixels from the background
            - Convert pixel area to cm2 using a reference marker
            - Store measurements per plant per day
            - Plot growth curves by treatment
Storage:    PostgreSQL, network file storage for images
Tech stack: Raspberry Pi HQ cameras, Python, OpenCV, PlantCV, pandas
```

---

## Example 221

**Intent:**
i got a raspberry shake seismometer, want to plot earthquakes it picks up

**Spec:**
```
Type:       Data analysis script (seismology)
Features:   - Download waveform data from the Raspberry Shake server
            - Filter the signal with a bandpass filter
            - Match signals to known earthquakes from the USGS feed
            - Plot the waveform and spectrogram for each event
            - Save a list of detected events
Input:      Station code, time range
Tech stack: Python, ObsPy, matplotlib
```

---

## Example 222

**Intent:**
observatory roof should close when clouds or rain come

**Spec:**
```
Type:       IoT system (observatory automation)
Features:   - Read sky temperature with an IR sensor to detect clouds
            - Detect rain with a rain sensor
            - Close the roll-off roof motor when it is cloudy or raining
            - Park the telescope before closing
            - Send a status to the astronomy software over ASCOM Alpaca
API:        REST
            GET  /api/v1/safetymonitor/0/issafe
            PUT  /api/v1/dome/0/closeshutter
Tech stack: Arduino Mega, MLX90614, Arduino (C++), ASCOM Alpaca, Python
```

---

## Example 223

**Intent:**
physics students measure pendulum period with a light gate and phone

**Spec:**
```
Type:       IoT system (school lab instrument)
Features:   - Detect each swing with an IR light gate
            - Time periods with microsecond precision
            - Send results to a phone over Bluetooth
            - Show period, average and standard deviation
            - Export the data as CSV
Tech stack: Arduino Nano 33 BLE, Arduino (C++), phyphox BLE library
```

---

## Example 224

**Intent:**
library study rooms - show which ones are free

**Spec:**
```
Type:       IoT system (room occupancy)
Data model: StudyRoom(id, name, capacity, occupied, updated_at)
Features:   - Detect occupancy in each room with a PIR and mmWave sensor
            - Mark a room free after 10 minutes of no presence
            - Show free rooms on a screen at the entrance
            - Show free rooms on the library website
API:        REST
            GET  /api/rooms
Storage:    Redis
Tech stack: ESP32, LD2410, MQTT, Python, FastAPI
```

---

## Example 225

**Intent:**
museum lends objects to other museums, track where they are and when they come back

**Spec:**
```
Type:       Web application (loan management)
Auth:       Registrar login (email + password)
Data model: Object(id, accession_number, title, value)
            Borrower(id, institution, contact)
            Loan(id, object_id -> Object, borrower_id -> Borrower, out_date, due_date, returned_date, insurance_ref, condition_out, condition_in)
Features:   - Record outgoing loans with insurance and condition reports
            - Show objects currently out and their location
            - Warn 60 days before loans end
            - Attach condition photos
            - Report loan history per object
Storage:    PostgreSQL
Tech stack: Python, Django
```

---

## Example 226

**Intent:**
count people coming to mass each sunday automatically

**Spec:**
```
Type:       IoT system (attendance counting)
Features:   - Count people through the doors with an overhead thermal sensor
            - Count only during service times
            - Record a total per service
            - Show attendance trends by month
Storage:    SQLite
Tech stack: Raspberry Pi, MLX90640 thermal camera, Python, OpenCV
```

---

## Example 227

**Intent:**
hindu temple, devotees book puja online and pay

**Spec:**
```
Type:       Web application (service booking)
Auth:       Devotee login (email or phone + OTP)
Data model: PujaType(id, name, price, duration_min)
            Booking(id, puja_type_id -> PujaType, devotee_id -> Devotee, date, time_slot, gotra, nakshatra, paid)
            Devotee(id, name, phone)
Features:   - List available pujas with prices
            - Book a date and time slot
            - Record family name, gotra and nakshatra for the priest
            - Take online payment
            - Show priests the day's booking list
Storage:    PostgreSQL
Tech stack: Python, Django, Razorpay
```

---

## Example 228

**Intent:**
my son is non verbal and needs a picture board app that speaks words when he taps

**Spec:**
```
Type:       Mobile application (AAC communication)
Data model: Board(id, name)
            Symbol(id, board_id -> Board, label, image_path, sound_path, position)
Features:   - Show grids of picture symbols
            - Speak the word aloud when a symbol is tapped
            - Build sentences from several symbols
            - Let parents add symbols with their own photos and recordings
            - Lock editing behind a parent PIN
Storage:    On-device SQLite
Tech stack: Flutter, flutter_tts
```

---

## Example 229

**Intent:**
colorblind dad cant tell red and green on charts, extension please

**Spec:**
```
Type:       Browser extension
Features:   - Apply colour-correction filters for protanopia, deuteranopia and tritanopia
            - Toggle the filter with a keyboard shortcut
            - Add patterns to colours on canvas charts
            - Remember the chosen mode
Tech stack: JavaScript, SVG colour matrix filters, Chrome Extension Manifest V3
```

---

## Example 230

**Intent:**
greenhouse windows open by themself when to hot

**Spec:**
```
Type:       IoT system (greenhouse ventilation)
Features:   - Read air temperature inside the greenhouse every minute
            - Open the roof vent with a linear actuator above 26 C
            - Close the vent below 22 C or when wind is strong
            - Close immediately when the rain sensor is wet
            - Show vent position and temperature on a web page
Tech stack: ESP32, SHT31, rain sensor, ESPHome, Home Assistant
```

---

## Example 231

**Intent:**
compost heap temperature, is it hot enough

**Spec:**
```
Type:       IoT system (compost monitoring)
Features:   - Read core temperature with a long stainless DS18B20 probe
            - Send readings every hour
            - Show a chart of temperature since the last turning
            - Remind me to turn the heap when temperature drops below 45 C
Tech stack: ESP8266, DS18B20, MicroPython, Adafruit IO
```

---

## Example 232

**Intent:**
rainwater tank feeds toilets, need pump to switch to mains when tank empty

**Spec:**
```
Type:       IoT system (water supply switching)
Features:   - Read the rainwater tank level
            - Run the pump for toilet supply from the tank
            - Switch a 3-way valve to mains water when the tank is below 10 percent
            - Switch back when the tank is above 25 percent
            - Log how many litres of mains water were saved
Tech stack: Arduino Uno, pressure level sensor, relay module, motorised 3-way valve, Arduino (C++)
```

---

## Example 233

**Intent:**
horses water trough freezes in winter, turn on heater when cold

**Spec:**
```
Type:       IoT system (stable automation)
Features:   - Read water temperature in the trough
            - Switch the trough heater on below 3 C
            - Switch it off above 6 C
            - Alert if the heater is on but the water keeps getting colder
Tech stack: Shelly Plus 1PM with temperature add-on, Shelly app, Home Assistant
```

---

## Example 234

**Intent:**
going on holiday 2 weeks, my 10 house plants need water, small pumps maybe?

**Spec:**
```
Type:       IoT system (plant watering)
Data model: Plant(id, name, pump_channel, min_moisture_pct, ml_per_watering)
            Watering(id, plant_id -> Plant, ml, watered_at)
Features:   - Read a soil moisture sensor per plant every hour
            - Run that plant's pump for the set amount when soil is dry
            - Stop if the water reservoir is empty
            - Send a daily report with photos to my phone
            - Limit watering to once per 12 hours per plant
Storage:    SQLite
Tech stack: Raspberry Pi, Python, ADS1115, 8-channel relay board, Telegram Bot API
```

---

## Example 235

**Intent:**
aquaponics, fish tank + grow bed, need to watch ammonia ph temp and pump

**Spec:**
```
Type:       IoT system (aquaponics monitoring)
Data model: Reading(id, ph, ammonia_ppm, water_temp_c, pump_running, read_at)
Features:   - Read pH and water temperature continuously
            - Read ammonia from a sensor or manual test entry
            - Cycle the grow bed pump 15 minutes on and 45 off
            - Alert if the pump stops or pH goes outside 6.8-7.2
            - Show trends for all values
API:        MQTT
            aquaponics/sensors
            aquaponics/pump
Storage:    InfluxDB
Tech stack: ESP32, Atlas Scientific probes, Node-RED, InfluxDB, Grafana
```

---

## Example 236

**Intent:**
homebrew beer fermentation keep at 19 degrees with old fridge and heat mat

**Spec:**
```
Type:       IoT system (fermentation control)
Data model: Batch(id, name, target_c, started_at)
            Reading(id, batch_id -> Batch, beer_temp_c, fridge_temp_c, gravity, read_at)
Features:   - Read beer temperature from a probe in the thermowell
            - Switch the fridge for cooling and a heat mat for heating with a PID controller
            - Ramp the temperature for a diacetyl rest
            - Read gravity from a floating hydrometer
            - Show a fermentation chart per batch
Storage:    SQLite
Tech stack: Raspberry Pi, BrewPi Remix/Fermentrack, Tilt hydrometer, DS18B20
```

---

## Example 237

**Intent:**
log coffee roast temps so i can repeat good roasts

**Spec:**
```
Type:       Desktop application (roast logging)
Features:   - Read bean and environment temperature from thermocouples over USB
            - Plot the roast curve live with rate of rise
            - Mark first crack and drop events
            - Save each roast profile and overlay a reference roast
            - Export profiles as CSV
Tech stack: Artisan roaster scope, Arduino with MAX31855 thermocouples (TC4 protocol)
```

---

## Example 238

**Intent:**
bbq smoker should hold 110 degrees all night with a fan

**Spec:**
```
Type:       IoT system (smoker temperature control)
Features:   - Read pit temperature and two meat probes
            - Control a blower fan with PID to hold the pit target
            - Alert on my phone when the meat reaches target temperature
            - Alert if the pit temperature falls (fire out)
            - Show the cook graph on a phone
Tech stack: ESP32, MAX31865 with PT1000 probes, HeaterMeter-style PID, Blynk
```

---

## Example 239

**Intent:**
sous vide stick DIY with arduino

**Spec:**
```
Type:       IoT system (cooking controller)
Features:   - Read water temperature with a waterproof DS18B20
            - Switch a heating element through a solid state relay with PID control
            - Set target temperature and timer with a rotary encoder
            - Show temperature and time left on an LCD
            - Beep when the timer ends
Tech stack: Arduino Uno, Arduino (C++), PID library, SSR-25DA, 16x2 I2C LCD
```

---

## Example 240

**Intent:**
front gate opens when it sees my car number plate

**Spec:**
```
Type:       IoT system (license plate gate access)
Data model: AllowedPlate(id, plate, owner_name, valid_until)
            GateEvent(id, plate, allowed, image_path, occurred_at)
Features:   - Capture frames from a camera facing the driveway
            - Read number plates with an ANPR model
            - Open the gate relay for allowed plates
            - Save a snapshot of every vehicle
            - Let me add guest plates for a set time
Storage:    SQLite
Tech stack: Raspberry Pi 5, Python, OpenCV, fast-alpr (plate recognition), relay HAT
```

---

## Example 241

**Intent:**
bathroom fan run when humidity high after shower

**Spec:**
```
Type:       IoT system (ventilation automation)
Features:   - Read bathroom humidity every 30 seconds
            - Turn the fan on when humidity rises 10 percent in 5 minutes
            - Turn the fan off when humidity returns near the baseline
            - Run at least 10 minutes each time
Tech stack: Sonoff THR320 with Tasmota, Tasmota rules
```

---

## Example 242

**Intent:**
night light for toddler, turns orange at bedtime and green when ok to get up

**Spec:**
```
Type:       IoT system (sleep trainer light)
Features:   - Glow orange at bedtime
            - Turn off the light during the night
            - Turn green at the set wake time
            - Let parents set times from a phone web page
            - Keep time with NTP
Tech stack: ESP8266, WS2812 LED ring, WLED firmware with presets and timers
```

---

## Example 243

**Intent:**
use my extra solar power to heat the hot water tank instead of sending to the grid

**Spec:**
```
Type:       IoT system (solar diversion)
Features:   - Measure grid import and export with a CT clamp
            - Increase power to the immersion heater with a triac when exporting
            - Keep grid export close to zero
            - Switch to boost mode on a timer if the water is not hot by evening
            - Log energy diverted per day
Storage:    InfluxDB
Tech stack: ESP32, SCT-013 CT clamp, AC dimmer module, ESPHome, Home Assistant
```

---

## Example 244

**Intent:**
read my smart meter p1 port and show live usage

**Spec:**
```
Type:       IoT system (smart meter reading)
Features:   - Read DSMR telegrams from the P1 port every second
            - Parse electricity and gas meter values
            - Publish them over MQTT
            - Show live and daily usage in Home Assistant
API:        MQTT
            dsmr/reading/electricity_currently_delivered
            dsmr/reading/extra_device_delivered
Tech stack: ESP8266, DSMR reader firmware, Mosquitto, Home Assistant
```

---

## Example 245

**Intent:**
school project: weather balloon with gps, send position so we can find it

**Spec:**
```
Type:       IoT system (high-altitude balloon tracking)
Features:   - Read GPS position and altitude every 10 seconds
            - Read outside temperature and pressure
            - Transmit telemetry over LoRa at long range
            - Show the flight on a live map at the ground station
            - Log all data to an SD card on the payload
Tech stack: Arduino Pro Mini, u-blox GPS, BME280, RFM95 LoRa, Raspberry Pi ground station, Python
```

---

## Example 246

**Intent:**
model railway trains controlled from tablet

**Spec:**
```
Type:       IoT system (model railway control)
Features:   - Control locomotive speed and direction over DCC
            - Switch points with servo motors
            - Show a track diagram with clickable points
            - Detect occupied track sections
            - Run simple automatic routes between stations
Tech stack: DCC-EX command station (Arduino Mega), JMRI, WiThrottle app
```

---

## Example 247

**Intent:**
rc car control with phone over wifi and camera

**Spec:**
```
Type:       IoT system (remote-controlled vehicle)
Features:   - Stream video from the car's camera to the phone
            - Drive the motors with a virtual joystick
            - Control steering with a servo
            - Stop the car if the connection drops
            - Show battery voltage
Tech stack: ESP32-CAM, Arduino (C++), L298N motor driver, WebSockets
```

---

## Example 248

**Intent:**
control my robot arm with sliders on computer

**Spec:**
```
Type:       Desktop application (robot arm control)
Features:   - Show a slider for each of the 6 servo joints
            - Send joint angles over serial to the controller
            - Record a sequence of poses
            - Play back recorded sequences
            - Add a home position button
Tech stack: Python, PySide6, pyserial, Arduino with PCA9685 servo driver
```

---

## Example 249

**Intent:**
scoreboard for table tennis at the club, press buttons for points

**Spec:**
```
Type:       IoT system (scoreboard)
Features:   - Add points with wireless buttons for each player
            - Show the score and games on an LED matrix
            - Switch serve indicator every 2 points
            - Detect game and match wins
            - Undo the last point
Tech stack: ESP32, 64x32 HUB75 LED matrix, ESP-NOW buttons, Arduino (C++)
```

---

## Example 250

**Intent:**
wedding photo booth with a button and prints the photo

**Spec:**
```
Type:       Desktop application (photo booth)
Features:   - Show a live camera preview on a screen
            - Count down and take 4 photos when the big button is pressed
            - Combine the photos into a strip with the couple's names
            - Print the strip on a dye-sub printer
            - Save all photos and show a QR code to download
Tech stack: Raspberry Pi 5, Python, pibooth, DSLR via gPhoto2, CUPS printer
```

---

## Example 251

**Intent:**
feedback buttons with smiley faces at our shop exit

**Spec:**
```
Type:       IoT system (customer feedback terminal)
Data model: Vote(id, terminal_id, score, voted_at)
Features:   - Read presses on 4 smiley buttons
            - Ignore repeated presses within 3 seconds
            - Send votes to the server with a timestamp
            - Show satisfaction by hour and day on a dashboard
API:        REST
            POST /api/votes
            GET  /api/votes/summary
Storage:    PostgreSQL
Tech stack: ESP32, Arduino (C++), Python, FastAPI, Chart.js
```

---

## Example 252

**Intent:**
song lyrics on projector for church worship, operator clicks through verses

**Spec:**
```
Type:       Desktop application (worship presentation)
Data model: Song(id, title, ccli_number, author)
            Section(id, song_id -> Song, label, lyrics)
            ServicePlan(id, date)
            PlanItem(id, plan_id -> ServicePlan, song_id -> Song, order)
Features:   - Store songs with verses and choruses
            - Build a service order
            - Show lyrics on the projector output and a preview on the operator screen
            - Jump to any section with one click
            - Log songs used for CCLI reporting
Storage:    SQLite
Tech stack: OpenLP (Python, Qt)
```

---

## Example 253

**Intent:**
football club scoreboard controlled from a phone

**Spec:**
```
Type:       IoT system (sports scoreboard)
Features:   - Update home and away scores from a phone web page
            - Run the match clock with start, pause and half-time
            - Show team names on the board
            - Keep the board state if power is lost briefly
Tech stack: ESP32, large 7-segment LED digits, Arduino (C++), ESPAsyncWebServer
```

---

## Example 254

**Intent:**
coffee shop loyalty, tap card to get a stamp, free coffee after 9

**Spec:**
```
Type:       Web application (loyalty program)
Data model: Customer(id, nfc_uid, name, email)
            Stamp(id, customer_id -> Customer, stamped_at)
            Reward(id, customer_id -> Customer, redeemed_at)
Features:   - Register a customer by tapping a new NFC card
            - Add a stamp when the card is tapped at the till
            - Show a free coffee when 9 stamps are collected
            - Reset stamps after redemption
            - Let customers check their stamps online
Storage:    PostgreSQL
Tech stack: Python, Flask, ACR122U NFC reader, nfcpy
```

---

## Example 255

**Intent:**
school canteen where kids pay with a card and parents top up online

**Spec:**
```
Type:       Web application (prepaid canteen)
Auth:       Parent login (email + password); canteen staff login
Data model: Student(id, name, rfid_uid, balance, daily_limit)
            Parent(id, email)
            TopUp(id, student_id -> Student, amount, paid_at)
            Purchase(id, student_id -> Student, items, total, bought_at)
Features:   - Let parents top up balances online
            - Charge purchases by scanning the student's card at the till
            - Enforce a daily spending limit set by parents
            - Block items for students with allergies
            - Show parents a purchase history
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Stripe, USB RFID readers
```

---

## Example 256

**Intent:**
patients fill in forms on a tablet in the waiting room instead of paper clipboard

**Spec:**
```
Type:       Web application (patient intake)
Data model: Patient(id, name, birth_date, phone)
            IntakeForm(id, patient_id -> Patient, medical_history, medications, allergies, consent_signed, submitted_at)
Features:   - Let patients fill in personal details, medical history and medications
            - Capture a consent signature on screen
            - Send the completed form to the practice management system
            - Clear all data from the tablet after submission
            - Offer the form in several languages
Storage:    PostgreSQL (encrypted at rest)
Tech stack: React, Node.js, signature_pad, HL7 FHIR API
```

---

## Example 257

**Intent:**
bed occupancy screen for hospital managers

**Spec:**
```
Type:       Data dashboard (bed management)
Data model: Ward(id, name, total_beds)
            Bed(id, ward_id -> Ward, number, status, patient_ref, status_changed_at)
Features:   - Show occupied, free and cleaning beds per ward
            - Show expected discharges for today
            - Show the emergency department waiting list for beds
            - Refresh every 2 minutes from the patient administration system
            - Highlight wards above 95 percent occupancy
Tech stack: Python, Dash (Plotly), HL7 ADT feed via Mirth Connect, PostgreSQL
```

---

## Example 258

**Intent:**
our dental clinic autoclave makes cycle printouts, we want them stored digital

**Spec:**
```
Type:       Data pipeline (sterilization records)
Data model: Autoclave(id, name, serial)
            Cycle(id, autoclave_id -> Autoclave, cycle_number, program, max_temp_c, hold_time_s, result, completed_at)
Features:   - Read the cycle report from the autoclave's USB or serial output
            - Parse cycle number, temperatures, pressures and pass or fail
            - Store each cycle in a database
            - Alert staff when a cycle fails
            - Export records for inspections
Storage:    PostgreSQL
Tech stack: Raspberry Pi, Python, pyserial
```

---

## Example 259

**Intent:**
is my mum eating? tell me if the fridge wasnt opened today

**Spec:**
```
Type:       IoT system (wellbeing monitoring)
Features:   - Count fridge door openings with a contact sensor
            - Send a gentle alert if there are no openings by 2 pm
            - Send a weekly summary of openings per day
Tech stack: Aqara door sensor, Zigbee2MQTT, Node-RED, Telegram
```

---

## Example 260

**Intent:**
rice field water level in many plots, we are farmers group in vietnam, want see on phone

**Spec:**
```
Type:       IoT system (paddy water monitoring)
Data model: Plot(id, owner_name, location)
            LevelReading(id, plot_id -> Plot, water_depth_cm, read_at)
Features:   - Measure water depth in each plot with an ultrasonic sensor in a pipe
            - Send readings every 30 minutes over LoRa
            - Show all plots and water depth on a phone app
            - Alert the plot owner when water is below 3 cm
            - Run on solar power
Storage:    InfluxDB
Tech stack: LoRa sensor nodes (RAK WisBlock), RAK gateway, ThingsBoard
```

---

## Example 261

**Intent:**
bicycle couriers, dispatcher assign jobs and see who is nearest

**Spec:**
```
Type:       Mobile application with backend
Auth:       Courier and dispatcher login (email + password)
Data model: Courier(id, name, status, lat, lon, updated_at)
            Job(id, pickup_address, dropoff_address, status, courier_id -> Courier, created_at)
Features:   - Share courier locations every 20 seconds while on shift
            - Show dispatchers all couriers and open jobs on a map
            - Suggest the nearest available courier for a job
            - Push the job to the courier's phone to accept
            - Track job status from pickup to delivered
API:        REST
            POST /couriers/location
            POST /jobs
            POST /jobs/{id}/assign
            PATCH /jobs/{id}/status
Storage:    PostgreSQL with PostGIS, Redis (live locations)
Tech stack: React Native, Node.js, Express, Socket.IO
```

---

## Example 262

**Intent:**
our mobile library van visits villages, want people to see when it comes and reserve books for pickup

**Spec:**
```
Type:       Web application (mobile library schedule)
Auth:       Library card number + PIN
Data model: Stop(id, village, location, day_of_week, arrive_time, depart_time)
            Hold(id, card_number, book_id, stop_id -> Stop, status)
Features:   - Show the van's route and stop times
            - Let patrons reserve books for collection at their stop
            - Show a live "van is running late" notice
            - Text patrons the day before the van comes
Storage:    PostgreSQL
Tech stack: Python, Django, Koha API, Twilio
```

---

## Example 263

**Intent:**
madrasa teacher want track each student quran memorize which surah and ayah, and send to parents

**Spec:**
```
Type:       Mobile application with backend
Auth:       Teacher login (email + password); parent login with code
Data model: Student(id, name, class)
            MemorizationLog(id, student_id -> Student, surah, from_ayah, to_ayah, quality, logged_at)
Features:   - Record new memorisation and revision for each student
            - Rate recitation quality
            - Show progress through the 114 surahs
            - Send weekly progress to parents
            - Show class leaderboard of juz completed
API:        REST
            GET  /students
            POST /students/{id}/logs
            GET  /students/{id}/progress
Storage:    PostgreSQL
Tech stack: Flutter, Firebase Auth, Node.js, Express
```

---

## Example 264

**Intent:**
walking cane for blind that buzzes when something is in front

**Spec:**
```
Type:       IoT system (assistive mobility)
Features:   - Measure distance ahead with an ultrasonic sensor
            - Vibrate faster as obstacles get closer
            - Detect head-height obstacles with a second upward sensor
            - Run on a rechargeable battery for a full day
Tech stack: Arduino Nano, HC-SR04 sensors, vibration motor, Arduino (C++)
```

---

## Example 265

**Intent:**
wheelchair user needs reminder to shift weight every 20 minutes to avoid pressure sores

**Spec:**
```
Type:       IoT system (pressure relief reminder)
Data model: SittingSession(id, started_at, ended_at, reliefs_done)
Features:   - Detect sitting with a pressure sensor under the cushion
            - Vibrate a reminder every 20 minutes of continuous sitting
            - Detect a completed weight shift from pressure change
            - Log compliance per day for the care team
Tech stack: ESP32, FSR pressure sensors, vibration motor, Arduino (C++), BLE to phone app
```

---

## Example 266

**Intent:**
sip and puff mouse for my friend with quadriplegia

**Spec:**
```
Type:       IoT system (assistive input device)
Features:   - Read breath pressure with a pressure sensor and mouthpiece
            - Map soft sip, hard sip, soft puff and hard puff to mouse clicks
            - Move the cursor with a small joystick operated by the lips
            - Act as a USB HID mouse with no drivers
            - Let sensitivity be calibrated
Tech stack: Arduino Pro Micro (ATmega32U4), Arduino (C++), Mouse library, MPX pressure sensor
```

---

## Example 267

**Intent:**
tell me the CO level in garage where i run the generator

**Spec:**
```
Type:       IoT system (gas safety)
Features:   - Read carbon monoxide with an MQ-7 sensor
            - Sound an alarm above 50 ppm
            - Turn on an exhaust fan
            - Send a phone alert
Tech stack: ESP32, MQ-7, ESPHome, Home Assistant
```

---

## Example 268

**Intent:**
worm farm too dry or too hot kill the worms

**Spec:**
```
Type:       IoT system (vermicompost monitoring)
Features:   - Read bedding moisture and temperature
            - Warn when temperature goes above 30 C
            - Warn when moisture is below 60 percent
            - Run a mister pump for 10 seconds when too dry
Tech stack: Raspberry Pi Pico W, MicroPython, capacitive moisture sensor, DS18B20
```

---

## Example 269

**Intent:**
goats feeder open at fixed times

**Spec:**
```
Type:       IoT system (livestock feeding)
Features:   - Open the hay feeder door with a linear actuator at set times
            - Close it after 1 hour
            - Allow manual open with a button
            - Keep the schedule during power cuts with an RTC
Tech stack: Arduino Uno, DS3231 RTC, linear actuator with relay, Arduino (C++)
```

---

## Example 270

**Intent:**
balcony herbs get automatic water from a bottle

**Spec:**
```
Type:       IoT system (balcony irrigation)
Features:   - Check soil moisture every 2 hours
            - Run a small 5V pump from a water bottle when dry
            - Run for 5 seconds at a time
            - Sleep between checks to run on a power bank
Tech stack: ESP32-C3, MicroPython, capacitive soil sensor, MOSFET pump driver
```

---

## Example 271

**Intent:**
arcade cabinet in our bar, count coins and plays per game

**Spec:**
```
Type:       IoT system (arcade usage tracking)
Data model: CoinEvent(id, cabinet_id, game, inserted_at)
Features:   - Count coin acceptor pulses
            - Record the currently selected game
            - Send counts to a dashboard
            - Show revenue per game per week
Storage:    SQLite
Tech stack: Raspberry Pi, RetroPie, Python, gpiozero, Flask
```

---

## Example 272

**Intent:**
hey so basically my nan's care home wants something where residents can request help from their room by pressing a button and staff get it on a pager, the old system is broken and costs a fortune to fix. maybe cheap zigbee buttons?

**Spec:**
```
Type:       IoT system (care call system)
Data model: Room(id, number, resident_name)
            CallRequest(id, room_id -> Room, pressed_at, acknowledged_at, completed_at)
Features:   - Receive button presses from Zigbee buttons in each room
            - Send the room number to staff phones as a high-priority notification
            - Escalate to all staff if not acknowledged within 3 minutes
            - Let staff mark the request completed
            - Report response times per day
Storage:    PostgreSQL
Tech stack: Zigbee buttons, Zigbee2MQTT, Node-RED, ntfy, PostgreSQL
```

---

## Example 273

**Intent:**
please i need the water heater in my house only work in morning and evening to save electric, i am not good with tecnology

**Spec:**
```
Type:       IoT system (water heater scheduling)
Features:   - Switch the water heater on from 5:30 to 7:00 and 18:00 to 20:00
            - Allow a one-hour boost with a single button press
            - Show the next on time on a small display
            - Keep the schedule after a power cut
Tech stack: Sonoff POWR320D with Tasmota, Tasmota timers
```

---

## Example 274

**Intent:**
lock front door automatically when we all left

**Spec:**
```
Type:       IoT system (home security automation)
Features:   - Detect when all household phones have left home
            - Lock the smart lock and confirm the lock state
            - Send a notification if the lock fails or a door is open
            - Unlock when a family member arrives and the phone is near
Tech stack: Home Assistant, Nuki smart lock, companion app presence
```

---

## Example 275

**Intent:**
know when my kids get home from school, they have a key ring tag

**Spec:**
```
Type:       IoT system (arrival notification)
Data model: Child(id, name, tag_uid)
            Arrival(id, child_id -> Child, arrived_at)
Features:   - Read the child's RFID key fob at the front door
            - Send a "Sam is home" message to parents
            - Alert parents if a child has not arrived by 4:30 pm on school days
            - Keep a log of arrival times
Storage:    SQLite
Tech stack: ESP8266, RC522 RFID reader, Arduino (C++), Telegram Bot API
```

---

## Example 276

**Intent:**
alert if windows left open and its starting to rain

**Spec:**
```
Type:       IoT system (home automation)
Features:   - Read window contact sensors around the house
            - Check the rain sensor and the forecast for rain in the next 30 minutes
            - Send a notification listing open windows
            - Repeat every 10 minutes until windows are closed
Tech stack: Zigbee contact sensors, Home Assistant, Met.no weather integration
```

---

## Example 277

**Intent:**
diy alarm system with door sensors, siren and phone app

**Spec:**
```
Type:       IoT system (home security)
Data model: Zone(id, name, sensor_id, type)
            AlarmEvent(id, zone_id -> Zone, event_type, occurred_at)
Features:   - Arm in away or home mode from the phone or a keypad
            - Trigger the siren when a door or motion sensor fires while armed
            - Give an entry delay of 30 seconds for the front door
            - Send push notifications with the zone that triggered
            - Log all arm, disarm and alarm events
Storage:    SQLite
Tech stack: Home Assistant, Alarmo integration, Zigbee sensors, Zigbee siren
```

---

## Example 278

**Intent:**
see power usage of every circuit in my fuse box

**Spec:**
```
Type:       IoT system (circuit-level energy monitoring)
Data model: Circuit(id, name, breaker_number)
            PowerReading(id, circuit_id -> Circuit, watts, recorded_at)
Features:   - Measure current on each circuit with CT clamps
            - Calculate power using the mains voltage
            - Send readings every 10 seconds
            - Show live power and daily kWh per circuit
            - Find circuits with constant standby load
API:        MQTT
            panel/circuit/{id}/power
Storage:    InfluxDB
Tech stack: ESP32 with ATM90E32 energy monitor boards, ESPHome, InfluxDB, Grafana
```

---

## Example 279

**Intent:**
heating oil tank level so we order before it runs out

**Spec:**
```
Type:       IoT system (tank level monitoring)
Features:   - Measure the oil level with an ultrasonic sensor on the tank top
            - Convert to litres using the tank shape
            - Estimate days left from recent usage
            - Email when the tank is below 300 litres
            - Show usage per month
Tech stack: ESP32, JSN-SR04T, MicroPython, InfluxDB Cloud
```

---

## Example 280

**Intent:**
pellet boiler hopper empty warning

**Spec:**
```
Type:       IoT system (pellet level monitoring)
Features:   - Measure pellet level with a time-of-flight sensor in the hopper
            - Estimate kilograms left
            - Notify when the hopper is below 20 percent
            - Show daily pellet use
Tech stack: ESP8266, VL53L1X, ESPHome, Home Assistant
```

---

## Example 281

**Intent:**
just a rain gauge that counts mm and shows on my phone

**Spec:**
```
Type:       IoT system (rain gauge)
Features:   - Count tipping bucket pulses with a reed switch
            - Convert tips to millimetres of rain
            - Report hourly and daily totals
            - Reset the daily total at midnight
Tech stack: ESP32, ESPHome pulse counter, Home Assistant
```

---

## Example 282

**Intent:**
electric fence voltage drops when grass touch it, i want know

**Spec:**
```
Type:       IoT system (electric fence monitoring)
Features:   - Measure fence pulse voltage through a high-voltage divider
            - Send the voltage every 15 minutes over LoRaWAN
            - Alert when voltage drops below 4 kV
            - Alert immediately when no pulses are detected
Tech stack: LoRaWAN fence monitor node, The Things Network, Node-RED, SMS gateway
```

---

## Example 283

**Intent:**
calving season, tell me when a cow starts calving at night so I can sleep

**Spec:**
```
Type:       IoT system (calving alert)
Data model: Cow(id, tag_number, due_date)
            CalvingAlert(id, cow_id -> Cow, triggered_at, acknowledged_at)
Features:   - Detect tail raising with a tilt sensor attached to the cow's tail
            - Alert when the tail stays raised for a set period
            - Call the farmer's phone and repeat until acknowledged
            - Show a camera feed of the calving pen on the phone
Storage:    SQLite
Tech stack: BLE tail sensors, Raspberry Pi gateway, Python, Twilio Voice, IP camera (RTSP)
```

---

## Example 284

**Intent:**
map where the tractor already sprayed in the field

**Spec:**
```
Type:       Mobile application (field coverage mapping)
Data model: Field(id, name, boundary_geojson)
            CoverageTrack(id, field_id -> Field, implement_width_m, started_at, path_geojson)
Features:   - Record GPS track from an external RTK receiver
            - Paint covered area using the implement width
            - Show missed and overlapped areas
            - Calculate hectares covered
            - Export coverage as a shapefile
Storage:    On-device SQLite
Tech stack: Kotlin (Android), OSMDroid, external Bluetooth GNSS receiver
```

---

## Example 285

**Intent:**
maple syrup tubing vacuum, need to find leaks in the lines

**Spec:**
```
Type:       IoT system (sugarbush vacuum monitoring)
Data model: Sensor(id, line_name, location)
            VacuumReading(id, sensor_id -> Sensor, vacuum_inhg, temperature_c, read_at)
Features:   - Read vacuum level at the end of each mainline
            - Send readings every 10 minutes over LoRaWAN
            - Show all lines on a map coloured by vacuum
            - Alert when a line drops more than 3 inHg below the pump vacuum
            - Pause alerts when temperatures are below freezing
Storage:    InfluxDB
Tech stack: LoRaWAN pressure sensors, ChirpStack, Python, Grafana
```

---

## Example 286

**Intent:**
gate at the farm road left open, cows get out, alert please

**Spec:**
```
Type:       IoT system (gate monitoring)
Features:   - Detect the gate position with a magnetic switch
            - Alert by SMS when the gate is open more than 15 minutes
            - Send a daily battery report
Tech stack: Arduino MKR WAN 1310, LoRaWAN, The Things Network, Twilio SMS API
```

---

## Example 287

**Intent:**
track harsh braking and speeding of our drivers

**Spec:**
```
Type:       IoT system (driver behaviour monitoring)
Data model: Driver(id, name)
            Trip(id, driver_id -> Driver, vehicle_id, started_at, ended_at)
            DrivingEvent(id, trip_id -> Trip, type, value, lat, lon, occurred_at)
Features:   - Detect harsh braking, acceleration and cornering from accelerometer data
            - Detect speeding by comparing GPS speed to road speed limits
            - Score each trip
            - Show a weekly ranking of drivers
            - Send coaching emails for trips with low scores
Storage:    PostgreSQL
Tech stack: Teltonika FMC130 trackers, Python, FastAPI, OSRM speed limits, React
```

---

## Example 288

**Intent:**
print shipping labels from a csv of orders

**Spec:**
```
Type:       Command-line script (shipping labels)
Features:   - Read orders from a CSV
            - Create shipments through the carrier API
            - Download labels as 4x6 PDFs
            - Print them on a thermal label printer
            - Write tracking numbers back to the CSV
Input:      CSV with name, address, weight and service level
Tech stack: Python, Shippo API, CUPS
```

---

## Example 289

**Intent:**
rfid tags on clothes in my shop to count stock quickly

**Spec:**
```
Type:       Mobile application with backend
Auth:       Staff login (email + password)
Data model: Product(id, sku, name, size, color)
            Tag(id, epc, product_id -> Product)
            StockCount(id, store_id, started_at, finished_at)
            CountedTag(id, count_id -> StockCount, epc)
Features:   - Encode an RFID tag for each item
            - Scan a whole rail of clothes with a handheld UHF reader
            - Compare counted items to expected stock
            - List missing and extra items
            - Save count history
API:        REST
            POST /counts
            POST /counts/{id}/tags
            GET  /counts/{id}/variance
Storage:    PostgreSQL
Tech stack: Zebra RFD40 handheld, Kotlin (Android), Zebra RFID SDK, Python, FastAPI
```

---

## Example 290

**Intent:**
button on each table to call the waiter

**Spec:**
```
Type:       IoT system (table call system)
Data model: Table(id, number)
            Call(id, table_id -> Table, type, called_at, answered_at)
Features:   - Press a button on the table to call the waiter or ask for the bill
            - Show calls with table numbers on a watch or screen for staff
            - Clear a call when the waiter taps it
            - Show average response time per shift
Tech stack: ESP32 table buttons, ESP-NOW, ESP32 receiver with display, Arduino (C++)
```

---

## Example 291

**Intent:**
screen facing customer at bakery shows what i rang up

**Spec:**
```
Type:       Web application (customer-facing display)
Features:   - Show items and prices as they are added at the till
            - Show the total and change due
            - Show a thank-you message with the shop's promos when idle
            - Update instantly over WebSockets
Tech stack: Node.js, Socket.IO, small HDMI monitor with Raspberry Pi
```

---

## Example 292

**Intent:**
tourist information touchscreen in the town square

**Spec:**
```
Type:       Web application (tourist info kiosk)
Data model: Attraction(id, name, category, description, lat, lon, opening_hours, image_url)
            Event(id, title, venue, starts_at)
Features:   - Show attractions, restaurants and events by category
            - Show a map with a walking route from the kiosk
            - Switch between 5 languages
            - Send details to a phone by QR code
            - Reset to the home screen after 90 seconds idle
Storage:    PostgreSQL
Tech stack: React, Node.js, Leaflet, weatherproof Android touchscreen in kiosk mode
```

---

## Example 293

**Intent:**
library print station, users pay with card before printing

**Spec:**
```
Type:       Web application (print release kiosk)
Auth:       Library card number + PIN
Data model: PrintJob(id, card_number, file_name, pages, color, cost, status, submitted_at)
Features:   - Receive print jobs from public computers and patrons' phones
            - Hold jobs until the patron releases them at the station
            - Show page count and cost
            - Charge the patron's card or account balance
            - Delete unreleased jobs after 24 hours
Storage:    PostgreSQL
Tech stack: Python, Flask, CUPS, Stripe Terminal
```

---

## Example 294

**Intent:**
emergency department screen with current wait times

**Spec:**
```
Type:       Web application (digital signage)
Features:   - Fetch the current average wait time per triage level every 5 minutes
            - Show it in large text in the waiting room
            - Explain that the most urgent patients are seen first
            - Show translations in the top 3 local languages
Tech stack: Python, Flask, HL7 feed via Mirth Connect, Raspberry Pi kiosk
```

---

## Example 295

**Intent:**
split flap style departure board for my hallway with my train times

**Spec:**
```
Type:       IoT system (departure board display)
Features:   - Fetch live departures for my station from the rail API
            - Show the next 3 trains with destination and expected time
            - Animate changes like a split flap board
            - Show "delayed" in amber
Tech stack: ESP32, 256x64 SSD1322 OLED, Arduino (C++), National Rail Darwin API
```

---

## Example 296

**Intent:**
how do visitors move through our museum, which rooms are popular

**Spec:**
```
Type:       Data dashboard (visitor flow)
Data model: Zone(id, name)
            Visit(id, device_hash, zone_id -> Zone, entered_at, left_at)
Features:   - Count anonymous Wi-Fi and Bluetooth probes per zone with hashed device IDs
            - Estimate dwell time per room
            - Show a heat map of the museum floor plan
            - Show common paths between rooms
            - Compare busy hours per weekday
Storage:    TimescaleDB
Tech stack: Raspberry Pi sensors, Python, Kismet, Grafana
```

---

## Example 297

**Intent:**
kids quiz with big buttons in our science museum

**Spec:**
```
Type:       IoT system (interactive exhibit)
Data model: Question(id, text, answers, correct_index, image_url)
Features:   - Show a question and four answers on a screen
            - Read answers from 4 large arcade buttons
            - Light the button green or red
            - Keep a score for a round of 5 questions
            - Return to an attract loop when idle
Storage:    JSON file of questions
Tech stack: Raspberry Pi, Python, Pygame, gpiozero
```

---

## Example 298

**Intent:**
library reminders, email people 3 days before books are due

**Spec:**
```
Type:       Scheduled script (library reminders)
Features:   - Query the library system for loans due in 3 days
            - Send a reminder email with titles and due dates
            - Send an overdue notice on day 1 and day 7 after the due date
            - Skip patrons who opted out
Tech stack: Python, Koha REST API, smtplib, cron
```

---

## Example 299

**Intent:**
our library has a seed library, people take seeds and bring back seeds, need catalogue

**Spec:**
```
Type:       Web application (seed library catalogue)
Auth:       Library staff login
Data model: Variety(id, crop, name, description, days_to_harvest, stock_packets)
            Checkout(id, variety_id -> Variety, patron_card, packets, taken_at)
            Return(id, variety_id -> Variety, patron_card, packets, grow_notes, returned_at)
Features:   - Browse seed varieties with growing notes
            - Record seeds taken and returned
            - Show stock levels and varieties running low
            - Collect grower notes on returned seeds
            - Print packet labels
Storage:    SQLite
Tech stack: Python, Flask, Bootstrap
```

---

## Example 300

**Intent:**
church volunteers rota for coffee, welcome team, sound desk

**Spec:**
```
Type:       Web application (volunteer rota)
Auth:       Volunteer login (magic link email)
Data model: Team(id, name)
            Volunteer(id, name, email)
            RotaSlot(id, team_id -> Team, service_date, volunteer_id -> Volunteer)
            Unavailability(id, volunteer_id -> Volunteer, date)
Features:   - Generate a monthly rota per team respecting unavailability
            - Let volunteers mark dates they cannot serve
            - Let volunteers swap slots with each other
            - Email reminders the week before
            - Print the rota for the noticeboard
Storage:    PostgreSQL
Tech stack: Python, Django, HTMX
```

---

## Example 301

**Intent:**
control the church camera for livestream from a phone, pan zoom to pulpit or choir

**Spec:**
```
Type:       Web application (camera control)
Auth:       Shared PIN for the media team
Data model: Preset(id, name, pan, tilt, zoom)
Features:   - Pan, tilt and zoom the PTZ camera with on-screen controls
            - Save presets such as pulpit, choir and baptistry
            - Recall a preset with one tap
            - Start and stop the YouTube livestream in OBS
Tech stack: Node.js, VISCA over IP, obs-websocket, Vue.js
```

---

## Example 302

**Intent:**
disaster relief warehouse, track tents water and food boxes going to camps

**Spec:**
```
Type:       Web application (relief supply tracking)
Auth:       Staff login (email + password) with offline support on tablets
Data model: Item(id, name, unit)
            Warehouse(id, name)
            Camp(id, name, population)
            StockMovement(id, item_id -> Item, from_warehouse_id -> Warehouse, to_camp_id -> Camp, quantity, sent_at, received_at)
Features:   - Record incoming supplies at the warehouse
            - Create dispatches to camps and print waybills
            - Confirm receipt at the camp
            - Show stock levels and needs per camp
            - Work offline and sync when connected
Storage:    PostgreSQL, IndexedDB on device
Tech stack: TypeScript, React (PWA), Node.js, NestJS
```

---

## Example 303

**Intent:**
blood donation drive, people book a time slot

**Spec:**
```
Type:       Web application (appointment booking)
Data model: Drive(id, location, date)
            Slot(id, drive_id -> Drive, starts_at, capacity)
            Donor(id, name, email, phone, blood_type)
            Appointment(id, slot_id -> Slot, donor_id -> Donor, status)
Features:   - Show upcoming drives and free slots
            - Ask eligibility questions before booking
            - Book and cancel appointments
            - Send reminders by SMS
            - Show the day's list to staff
Storage:    PostgreSQL
Tech stack: Python, Django, Twilio SMS API
```

---

## Example 304

**Intent:**
youth club attendance with membership cards, need numbers for council funding

**Spec:**
```
Type:       Web application (attendance tracking)
Auth:       Youth worker login
Data model: Member(id, name, birth_year, postcode, card_code)
            Session(id, activity, date)
            Attendance(id, session_id -> Session, member_id -> Member)
Features:   - Scan member cards at the door
            - Register new members quickly
            - Show attendance per session
            - Report attendance by age group and postcode area for funders
Storage:    SQLite
Tech stack: Python, Flask, USB barcode scanner
```

---

## Example 305

**Intent:**
track the snow plows on a map so people know which roads are cleared

**Spec:**
```
Type:       Web application (public vehicle tracking)
Data model: Plow(id, name)
            Position(id, plow_id -> Plow, lat, lon, blade_down, recorded_at)
            Road(id, name, geom, last_cleared_at)
Features:   - Receive GPS and blade status from each plow every 15 seconds
            - Match plow paths to road segments
            - Mark roads as cleared with the time
            - Show a public map coloured by hours since clearing
            - Hide live plow positions while keeping cleared roads public
Storage:    PostgreSQL with PostGIS
Tech stack: Python, FastAPI, Mapbox GL JS, Teltonika trackers
```

---

## Example 306

**Intent:**
public toilets, people rate if clean with a button and cleaners get notified

**Spec:**
```
Type:       IoT system (facility feedback)
Data model: Facility(id, name, location)
            Rating(id, facility_id -> Facility, score, rated_at)
            CleaningVisit(id, facility_id -> Facility, cleaner_badge, visited_at)
Features:   - Collect ratings from 3 buttons at the exit
            - Send a cleaning request when 3 bad ratings arrive in 30 minutes
            - Let cleaners check in with an NFC tag
            - Show cleanliness scores per facility
API:        MQTT
            facilities/{id}/rating
Storage:    PostgreSQL
Tech stack: ESP32, NFC reader, Mosquitto, Python, Grafana
```

---

## Example 307

**Intent:**
on election night, polling stations enter vote counts and we show results live

**Spec:**
```
Type:       Web application (results reporting)
Auth:       Station officer login with one-time codes
Data model: Station(id, name, ward)
            Candidate(id, name, party)
            Result(id, station_id -> Station, candidate_id -> Candidate, votes, submitted_at, verified)
Features:   - Let officers enter counts per candidate for their station
            - Require a second officer to verify before publishing
            - Show live totals by ward and overall
            - Show stations still to report
            - Keep an audit log of every change
Storage:    PostgreSQL
Tech stack: Python, Django, Django Channels, Redis
```

---

## Example 308

**Intent:**
fume hood airflow low alarm

**Spec:**
```
Type:       IoT system (lab safety monitoring)
Features:   - Measure face velocity with an airflow sensor
            - Show a green or red light on the hood
            - Sound an alarm when velocity is below 0.4 m/s
            - Log readings for annual inspection
Tech stack: Arduino Nano, Sensirion SDP810, Arduino (C++), SD card logger
```

---

## Example 309

**Intent:**
liquid nitrogen dewar level, someone forgot to fill and lost samples

**Spec:**
```
Type:       IoT system (cryogenic storage monitoring)
Data model: Dewar(id, name, lab, min_level_cm)
            LevelReading(id, dewar_id -> Dewar, level_cm, temperature_c, read_at)
Features:   - Measure LN2 level with a capacitive level sensor
            - Read the temperature at the top of the sample rack
            - Alert lab members when the level is below minimum
            - Escalate to the lab manager after 1 hour
            - Show fill history
Storage:    PostgreSQL
Tech stack: Raspberry Pi, Python, Django, Slack API
```

---

## Example 310

**Intent:**
health kiosk where people measure weight blood pressure and oxygen and doctor sees it

**Spec:**
```
Type:       Web application (telehealth kiosk)
Auth:       Patient login by ID card scan; clinician login with 2FA
Data model: Patient(id, national_id, name)
            Vitals(id, patient_id -> Patient, weight_kg, systolic, diastolic, spo2, pulse, measured_at)
Features:   - Identify the patient by scanning an ID card
            - Read weight, blood pressure and SpO2 from connected devices
            - Show readings with simple explanations
            - Send the vitals to the patient's record
            - Let a clinician start a video consultation
Storage:    PostgreSQL
Tech stack: React, Node.js, Bluetooth LE medical devices, HL7 FHIR, WebRTC
```

---

## Example 311

**Intent:**
hearing test app with headphones, beep at different frequencies

**Spec:**
```
Type:       Mobile application (hearing screening)
Data model: TestResult(id, ear, frequency_hz, threshold_db, tested_at)
Features:   - Play pure tones at 250 to 8000 Hz in each ear
            - Increase and decrease volume to find the hearing threshold
            - Show an audiogram chart
            - Warn when results suggest hearing loss and suggest seeing a professional
            - Calibrate for the user's headphones
Storage:    Local storage
Tech stack: Swift, AVAudioEngine, Swift Charts
```

---

## Example 312

**Intent:**
refreshable braille display shows text from my computer, i want to build cheap one

**Spec:**
```
Type:       IoT system (braille display)
Features:   - Receive text from a computer over USB serial
            - Convert characters to 6-dot braille patterns
            - Drive solenoid pins for 8 braille cells
            - Scroll text with two buttons
            - Work with the NVDA screen reader through a simple driver
Tech stack: Arduino Mega, Arduino (C++), solenoid pin array, Python NVDA add-on
```

---

## Example 313

**Intent:**
visual timer for my adhd daughter so she sees time going

**Spec:**
```
Type:       IoT system (visual timer)
Features:   - Show remaining time as a shrinking ring of LEDs
            - Set the duration by turning a knob
            - Change colour in the last 2 minutes
            - Play a gentle chime at the end
Tech stack: Arduino Nano, 24 LED NeoPixel ring, rotary encoder, piezo buzzer, Arduino (C++)
```

---

## Example 314

**Intent:**
zigbee buttons for my grandad so he can turn lamps on without getting up

**Spec:**
```
Type:       IoT system (home automation)
Features:   - Pair large Zigbee buttons with the lamps
            - Toggle the lamp with a single press
            - Dim the lamp with a long press
            - Turn all living room lamps off with a double press
Tech stack: IKEA TRÅDFRI buttons and bulbs, Zigbee2MQTT, Home Assistant
```

---

## Example 315

**Intent:**
using micropython on esp8266, i want to read a light sensor and turn on the porch light when dark

**Spec:**
```
Type:       IoT system (lighting automation)
Features:   - Read light level from a BH1750 sensor every minute
            - Switch the porch light relay on below 10 lux
            - Switch it off at midnight to save power
            - Use hysteresis so the light does not flicker at dusk
Tech stack: ESP8266, MicroPython, BH1750 driver, relay module
```

---

## Example 316

**Intent:**
my shop fridge drinks cooler is breaking down a lot i want to see if compressor runs all the time

**Spec:**
```
Type:       IoT system (refrigeration diagnostics)
Data model: CompressorCycle(id, started_at, ended_at, avg_watts)
            CabinetReading(id, temperature_c, read_at)
Features:   - Measure compressor power with a smart plug
            - Detect compressor start and stop cycles
            - Calculate duty cycle per hour
            - Warn when the duty cycle is above 80 percent for a day
            - Chart cabinet temperature against compressor runtime
Storage:    InfluxDB
Tech stack: Shelly Plug S, Shelly H&T sensor, Node-RED, InfluxDB, Grafana
```

---

## Example 317

**Intent:**
Hi, I volunteer at a wildlife rescue centre and we have lots of hedgehogs in boxes with heat pads. Some pads overheat. Could we watch the temperature in each box?

**Spec:**
```
Type:       IoT system (animal care monitoring)
Data model: Enclosure(id, label, animal_name, min_c, max_c)
            Reading(id, enclosure_id -> Enclosure, temperature_c, read_at)
Features:   - Read a temperature probe in each hospital box every 2 minutes
            - Switch the heat pad off through a relay above the maximum
            - Alert volunteers on their phones when a box is out of range
            - Show all boxes on a tablet grid with colour status
            - Let volunteers rename boxes when animals change
Storage:    SQLite
Tech stack: Raspberry Pi, DS18B20 probes on 1-Wire, Python, Flask, ntfy
```

---

## Example 318

**Intent:**
count cars into our church car park on sundays so we know when to open the overflow field

**Spec:**
```
Type:       IoT system (car park counting)
Features:   - Detect cars entering and leaving with two IR beams to know direction
            - Keep a running count of parked cars
            - Light an "overflow open" sign when 90 percent full
            - Reset the count at 5 am every day
Tech stack: Arduino Uno, E18-D80NK IR sensors, Arduino (C++), relay for LED sign
```

---

## Example 319

**Intent:**
esp32 + home assistant to know if my washing machine finished

**Spec:**
```
Type:       IoT system (appliance notification)
Features:   - Measure washing machine power with a current sensor
            - Detect the end of a cycle when power stays below 3 W for 2 minutes
            - Send a phone notification
            - Remind again after 30 minutes if the door was not opened
Tech stack: ESP32, SCT-013 CT clamp, ESPHome, Home Assistant
```

---

## Example 320

**Intent:**
wanna see my 3d printer camera and temps on my phone from anywhere

**Spec:**
```
Type:       Infrastructure setup (remote printer access)
Features:   - Run OctoPrint with a webcam stream on a Raspberry Pi
            - Expose it securely without opening router ports
            - Show hotend and bed temperatures and the camera on a phone
            - Require login with two-factor authentication
Tech stack: Raspberry Pi, OctoPrint, Tailscale, OctoApp mobile app
```

---

## Example 321

**Intent:**
klipper printer, want a button that runs a macro to load filament

**Spec:**
```
Type:       Plugin (printer firmware macro)
Features:   - Add a physical button on a spare MCU pin
            - Heat the nozzle to the filament's temperature when pressed
            - Push filament through the extruder slowly
            - Beep when loading is complete
Tech stack: Klipper, gcode_button config, gcode_macro, Moonraker
```

---

## Example 322

**Intent:**
check fertilizer tank level in irrigation of 5 farms in one website

**Spec:**
```
Type:       Data dashboard (farm tank monitoring)
Data model: Farm(id, name)
            Tank(id, farm_id -> Farm, product, capacity_l)
            LevelReading(id, tank_id -> Tank, level_l, read_at)
Features:   - Collect tank levels from sensors on each farm
            - Show all tanks on one page grouped by farm
            - Estimate days until each tank is empty
            - Email the agronomist when a tank is below 15 percent
            - Show usage per week per product
Storage:    PostgreSQL
Tech stack: Cellular level sensors (4G), Python, FastAPI, Metabase
```

---

## Example 323

**Intent:**
humidity in our church organ loft must stay safe for the pipes

**Spec:**
```
Type:       IoT system (instrument climate monitoring)
Features:   - Read humidity and temperature in the organ loft every 10 minutes
            - Run a humidifier below 45 percent
            - Warn the organist when humidity goes outside 40-65 percent
            - Show a yearly chart for the organ builder
Tech stack: ESP32, SHT41, ESPHome, Home Assistant
```

---

## Example 324

**Intent:**
digital sign in our town square with council news, events, and air quality

**Spec:**
```
Type:       Web application (public digital signage)
Auth:       Council staff login with Microsoft SSO
Data model: Notice(id, title, body, starts_at, ends_at, priority)
            Event(id, title, venue, starts_at)
Features:   - Rotate council notices and upcoming events
            - Show live air quality from the city sensor network
            - Push emergency notices that override everything
            - Dim the screen brightness at night
            - Report screen uptime
Storage:    PostgreSQL
Tech stack: TypeScript, Next.js, outdoor LED screen with BrightSign player, OpenAQ API
```

---

## Example 325

**Intent:**
weather station data to wunderground and my own site

**Spec:**
```
Type:       Data pipeline (weather data upload)
Features:   - Receive data from a consumer weather station over its local custom upload
            - Convert units to metric
            - Forward readings to Weather Underground and Windy
            - Store a copy in my own database
            - Publish a simple current conditions page
Storage:    InfluxDB
Tech stack: Python, FastAPI, Ecowitt custom server protocol, Weather Underground upload API
```

---

## Example 326

**Intent:**
bee hive inside temperature and sound to know if queen is lost

**Spec:**
```
Type:       IoT system (hive health monitoring)
Data model: Hive(id, name)
            Reading(id, hive_id -> Hive, brood_temp_c, humidity_pct, sound_peak_hz, sound_level_db, recorded_at)
Features:   - Measure brood temperature and humidity inside the hive
            - Record a short audio sample every hour
            - Compute the dominant frequency of the hive hum
            - Flag possible queenlessness from a sustained shift in hum frequency
            - Show trends per hive
Storage:    InfluxDB
Tech stack: ESP32, I2S microphone, SHT31, Python, NumPy (FFT), Grafana
```

---

## Example 327

**Intent:**
show the electricity my museum uses each month per building, the boss wants to cut costs

**Spec:**
```
Type:       Data dashboard (energy reporting)
Data model: Building(id, name, floor_area_m2)
            MeterReading(id, building_id -> Building, kwh, reading_date)
Features:   - Import half-hourly meter data from the energy supplier
            - Show monthly kWh and cost per building
            - Compare against the same month last year
            - Show kWh per square metre
            - Highlight night-time base load that could be cut
Storage:    PostgreSQL
Tech stack: Python, pandas, Streamlit
```

---

## Example 328

**Intent:**
send me a message every day at 8 with yesterday's min and max temp in my greenhouse

**Spec:**
```
Type:       Scheduled script (daily sensor summary)
Features:   - Query yesterday's greenhouse readings from the database
            - Calculate minimum, maximum and average temperature
            - Send the summary to a Telegram chat at 8 am
            - Add a warning if the minimum was below 5 C
Tech stack: Python, InfluxDB client, python-telegram-bot, cron
```

---

## Example 329

**Intent:**
my old dad keep forgetting his walking frame by bed and fall, can something warn when he stand up at night

**Spec:**
```
Type:       IoT system (bed exit alert)
Features:   - Detect when he gets out of bed with a pressure mat
            - Turn on a soft floor light at night
            - Play a spoken reminder "use your frame"
            - Alert the carer's phone if he has been out of bed for 15 minutes
Tech stack: Raspberry Pi Zero 2 W, bed pressure mat, Python, Philips Hue, Pushover
```

---

## Example 330

**Intent:**
tracking our shipping containers in the yard, which slot each one is

**Spec:**
```
Type:       Web application (yard management)
Auth:       Yard staff login (email + password)
Data model: Container(id, number, size, status, owner)
            Slot(id, row, bay, tier)
            Placement(id, container_id -> Container, slot_id -> Slot, placed_at, removed_at)
Features:   - Record container arrival and assign a slot
            - Scan container numbers with phone OCR
            - Show the yard as a grid with occupied slots
            - Search where a container is
            - Log gate-out with truck plate
Storage:    PostgreSQL
Tech stack: Python, Django, Google ML Kit text recognition (Android)
```

---

## Example 331

**Intent:**
arduino measure distance a person sits from tv and beep if too close kids

**Spec:**
```
Type:       IoT system (viewing distance alert)
Features:   - Measure the distance in front of the TV with an ultrasonic sensor
            - Beep when someone is closer than 1.5 metres for 10 seconds
            - Ignore short passes in front of the TV
            - Turn on with the TV via a USB port
Tech stack: Arduino Nano, HC-SR04, piezo buzzer, Arduino (C++)
```

---

## Example 332

**Intent:**
food delivery for elderly that cannot cook, they order with very simple tablet

**Spec:**
```
Type:       Mobile application with backend
Auth:       Tablet is pre-registered to the senior; kitchen staff login (email + password)
Data model: Senior(id, name, address, diet_restrictions)
            Meal(id, name, photo_url, allergens, available_date)
            Order(id, senior_id -> Senior, meal_id -> Meal, delivery_date, status)
Features:   - Show tomorrow's meals as big photos
            - Order with one tap and a spoken confirmation
            - Hide meals that clash with diet restrictions
            - Show the kitchen a list of orders by route
            - Let family view and change orders
API:        REST
            GET  /meals?date={date}
            POST /orders
            GET  /kitchen/orders?date={date}
Storage:    PostgreSQL
Tech stack: Flutter (Android tablet kiosk mode), Python, FastAPI
```

---

## Example 333

**Intent:**
cheap gps on donated bikes we lend out so they dont get stolen

**Spec:**
```
Type:       IoT system (bike share tracking)
Data model: Bike(id, name, tracker_id, status)
            Location(id, bike_id -> Bike, lat, lon, recorded_at)
Features:   - Report each bike's location every 30 minutes while parked and every 2 minutes while moving
            - Alert when a bike leaves the town area
            - Show all bikes on a map for staff
            - Track battery level of each tracker
Storage:    PostgreSQL
Tech stack: Teltonika TMT250 trackers, Traccar server, Traccar web UI
```

---

## Example 334

**Intent:**
lab balance readings go into the electronic lab notebook automatically

**Spec:**
```
Type:       Desktop application (instrument data capture)
Features:   - Read the weight from a lab balance over RS-232 when the print key is pressed
            - Attach the sample ID typed or scanned by the user
            - Save weight, unit, sample ID and timestamp
            - Send the record to the electronic lab notebook API
            - Keep a local CSV backup
Tech stack: Python, pyserial, Tkinter, eLabFTW API
```

---

## Example 335

**Intent:**
plant room in the hospital basement - pumps and boilers - show alarms on one screen

**Spec:**
```
Type:       Data dashboard (building management)
Data model: Equipment(id, name, type, location)
            Alarm(id, equipment_id -> Equipment, message, severity, raised_at, cleared_at)
Features:   - Read status and alarms from boilers and pumps over BACnet
            - Show all equipment states on a plant room diagram
            - List active alarms by severity
            - Send critical alarms to the estates on-call phone
            - Keep an alarm history
Storage:    PostgreSQL
Tech stack: Python, BAC0 (BACnet), FastAPI, React
```

---

## Example 336

**Intent:**
vineyard, measure leaf wetness for disease risk

**Spec:**
```
Type:       IoT system (crop disease risk)
Data model: Reading(id, leaf_wetness_pct, temperature_c, humidity_pct, recorded_at)
            RiskDay(id, date, wet_hours, mildew_risk)
Features:   - Read leaf wetness, temperature and humidity every 15 minutes
            - Count hours of leaf wetness per day
            - Calculate downy mildew infection risk with a weather model
            - Notify the grower on high-risk days
            - Show a risk calendar for the season
Storage:    TimescaleDB
Tech stack: LoRaWAN leaf wetness sensors, The Things Network, Python, Grafana
```

---

## Example 337

**Intent:**
show bus arrival at the stop for people who can't read small text, big letters

**Spec:**
```
Type:       Web application (accessible transit display)
Features:   - Fetch arrivals for one stop from the transit API every 30 seconds
            - Show route and minutes until arrival in very large high-contrast text
            - Announce arrivals by audio when a button is pressed
            - Work full-screen on an outdoor display
Tech stack: JavaScript, GTFS-Realtime, Web Speech API, Raspberry Pi kiosk
```

---

## Example 338

**Intent:**
hey i manage 4 apartment buildings and boiler failures always happen on weekends. i want to watch the boiler flow temp in each and get a text if it drops, im not techy but my nephew can install stuff

**Spec:**
```
Type:       IoT system (remote boiler monitoring)
Data model: Building(id, address)
            Boiler(id, building_id -> Building, min_flow_c)
            Reading(id, boiler_id -> Boiler, flow_temp_c, return_temp_c, read_at)
Features:   - Clamp temperature sensors on flow and return pipes
            - Send readings every 5 minutes over Wi-Fi
            - Send an SMS when flow temperature stays below the minimum for 20 minutes
            - Show all buildings on one page
            - Send a weekly health summary by email
Storage:    InfluxDB Cloud
Tech stack: ESP32, DS18B20 pipe clamps, ESPHome, Home Assistant Cloud, Twilio
```

---

## Example 339

**Intent:**
noise box for our recording studio door: red light when recording

**Spec:**
```
Type:       IoT system (on-air indicator)
Features:   - Detect recording state from the DAW over MIDI or OSC
            - Turn the "on air" sign red while recording
            - Turn it off when recording stops
            - Allow a manual override switch
Tech stack: ESP32, OSC over Wi-Fi, Reaper OSC, relay module
```

---

## Example 340

**Intent:**
sensor that says if school classroom needs to open window (co2)

**Spec:**
```
Type:       IoT system (classroom ventilation)
Features:   - Measure CO2 with an NDIR sensor every 30 seconds
            - Show green below 800 ppm, amber up to 1200 and red above
            - Beep softly when red for 5 minutes
            - Log values for the facilities team
Tech stack: Arduino Nano, Sensirion SCD41, WS2812 LEDs, Arduino (C++)
```

---

## Example 341

**Intent:**
Garage workshop dust collector should start when I turn on the table saw

**Spec:**
```
Type:       IoT system (workshop automation)
Features:   - Sense the table saw current with a current sensor
            - Start the dust collector relay when a tool is running
            - Keep the collector running 10 seconds after the tool stops
            - Open the right blast gate with a servo
Tech stack: Arduino Nano, ACS712 current sensor, relay module, servo blast gates, Arduino (C++)
```

---

## Example 342

**Intent:**
kiosk in the lobby of our nonprofit for visitors to make a quick donation by tapping phone

**Spec:**
```
Type:       Web application (contactless donation kiosk)
Data model: Donation(id, amount, payment_id, donated_at)
Features:   - Show three preset amounts and a custom amount
            - Accept tap-to-pay with phones and cards
            - Show a thank-you animation and impact message
            - Show the day's total on the staff page
Storage:    PostgreSQL
Tech stack: React, Stripe Terminal (Tap to Pay on Android), Node.js
```

---

## Example 343

**Intent:**
the temple wants a screen in the hall showing today's events and the panchang

**Spec:**
```
Type:       Web application (digital signage)
Auth:       Admin login for temple committee
Data model: Event(id, title, starts_at, description)
Features:   - Show today's tithi, nakshatra and sunrise and sunset
            - Show the day's pujas and events
            - Rotate festival announcements
            - Update automatically every day at midnight
Storage:    SQLite
Tech stack: Python, Flask, Swiss Ephemeris (pyswisseph), Raspberry Pi kiosk
```

---

## Example 344

**Intent:**
i run an escape room and want puzzles with sensors that unlock the next door

**Spec:**
```
Type:       IoT system (escape room control)
Data model: Puzzle(id, name, room, solved)
            GameSession(id, team_name, started_at, ended_at)
Features:   - Read puzzle sensors such as RFID props, buttons and magnetic switches
            - Release maglocks when a puzzle is solved
            - Show game masters the state of every puzzle on a dashboard
            - Let the game master trigger hints and reset all props
            - Time each game session
API:        MQTT
            escape/{room}/{puzzle}/state
            escape/{room}/{puzzle}/command
Storage:    SQLite
Tech stack: ESP32 props, Mosquitto, Node-RED dashboard
```

---

## Example 345

**Intent:**
sentry for pharmacy fridge, vaccines must stay 2-8, and we need records for 2 years

**Spec:**
```
Type:       IoT system (vaccine fridge monitoring)
Data model: Fridge(id, name, location)
            Reading(id, fridge_id -> Fridge, temperature_c, recorded_at)
            Excursion(id, fridge_id -> Fridge, started_at, ended_at, max_c, min_c, action_taken)
Features:   - Read a glycol-buffered probe every 5 minutes
            - Alert pharmacy staff on any excursion outside 2-8 C
            - Require staff to record an action for each excursion
            - Show daily min and max for twice-daily checks
            - Keep records for 2 years with export to PDF
Storage:    PostgreSQL
Tech stack: ESP32, DS18B20 in glycol bottle, Python, Django, Twilio
```

---

## Example 346

**Intent:**
parent teacher association raffle and bake sale till on a tablet

**Spec:**
```
Type:       Mobile application (point of sale)
Features:   - Show bake sale items as big buttons with prices
            - Take cash or card through a card reader
            - Track how many of each item sold
            - Show the total raised at the end
Storage:    Local storage
Tech stack: Flutter, SumUp SDK
```

---

## Example 347

**Intent:**
Pi-based internet radio for my blind grandma with only big buttons

**Spec:**
```
Type:       IoT system (accessible radio)
Features:   - Play internet radio stations from a list
            - Change station with one big button and speak the station name
            - Change volume with a large knob
            - Resume the last station on power-up
Tech stack: Raspberry Pi 3, Python, mpv, gpiozero, espeak-ng
```

---

## Example 348

**Intent:**
forklift battery charging room hydrogen sensor

**Spec:**
```
Type:       IoT system (gas detection)
Features:   - Read hydrogen concentration with a gas sensor near the ceiling
            - Start the extraction fan at 1 percent LEL
            - Sound an alarm and cut chargers at 2 percent LEL
            - Log readings and events
Tech stack: Industrial gas detector with 4-20 mA output, Arduino Opta PLC, Arduino (C++)
```

---

## Example 349

**Intent:**
science olympiad team wants to log acceleration from a model rocket

**Spec:**
```
Type:       IoT system (flight data logger)
Features:   - Sample a high-g accelerometer and barometer at 100 Hz
            - Detect launch, apogee and landing
            - Store data on a microSD card
            - Fire a parachute ejection charge at apogee
            - Beep landing location with a buzzer
Tech stack: Teensy 4.0, ADXL375, BMP388, Arduino (C++), SdFat
```

---

## Example 350

**Intent:**
we lend pulse oximeters to covid patients at home and need them back and readings each day

**Spec:**
```
Type:       Web application (remote patient monitoring)
Auth:       Clinician login with hospital SSO; patients use a text link
Data model: Patient(id, name, phone, device_serial, enrolled_on)
            Reading(id, patient_id -> Patient, spo2, pulse, submitted_at)
            DeviceLoan(id, patient_id -> Patient, device_serial, issued_on, returned_on)
Features:   - Text patients twice a day with a link to submit readings
            - Flag readings below 94 percent SpO2 for review
            - Escalate readings below 92 percent to the on-call clinician
            - Track loaned devices and returns
            - Discharge patients after 14 days
Storage:    PostgreSQL
Tech stack: Python, Django, Twilio SMS API
```

---

## Example 351

**Intent:**
I need to know which of my 300 sheep are in which paddock, they have EID tags

**Spec:**
```
Type:       Web application (flock management)
Auth:       Farmer login (email + password)
Data model: Sheep(id, eid, breed, sex, birth_year)
            Paddock(id, name, area_ha)
            Movement(id, sheep_id -> Sheep, paddock_id -> Paddock, moved_at)
Features:   - Import EID scans from a stick reader after moving a mob
            - Record which paddock the mob moved into
            - Show the count of sheep in each paddock
            - Show grazing days per paddock
            - Search an individual sheep's history
Storage:    PostgreSQL
Tech stack: Python, Django, Bluetooth EID stick reader CSV import
```

---

## Example 352

**Intent:**
ramadan iftar meal sign up at the mosque so we know how much food

**Spec:**
```
Type:       Web application (meal registration)
Data model: Night(id, date, capacity)
            Registration(id, night_id -> Night, name, phone, adults, children)
Features:   - Show each night of Ramadan with places left
            - Let families register adults and children
            - Close registration at noon each day
            - Show the kitchen a headcount per night
            - Let volunteers sign up to sponsor a night
Storage:    PostgreSQL
Tech stack: Python, Flask, Bootstrap
```

---

## Example 353

**Intent:**
track library ebook reader devices we loan, battery and which books on them

**Spec:**
```
Type:       Web application (device lending)
Auth:       Staff login
Data model: Device(id, serial, model, battery_pct, last_synced_at)
            DeviceLoan(id, device_id -> Device, patron_card, out_at, due_at, returned_at)
            LoadedBook(id, device_id -> Device, title)
Features:   - Check devices in and out with patron cards
            - Record which titles are loaded on each device
            - Remind staff to charge devices after return
            - Show devices due back and overdue
            - Wipe patron data on return
Storage:    PostgreSQL
Tech stack: Ruby on Rails, Hotwire
```

---

## Example 354

**Intent:**
robot that moves around the museum and tells visitors about things

**Spec:**
```
Type:       IoT system (tour guide robot)
Features:   - Navigate between exhibits on a saved map with lidar
            - Stop and speak a description at each exhibit
            - Show text and images on a front tablet
            - Detect people blocking the path and wait
            - Return to the charging dock when the battery is low
Tech stack: ROS 2, TurtleBot 4, Nav2, Python, Piper TTS
```

---

## Example 355

**Intent:**
monitor printer ink and paper on 30 office printers via snmp

**Spec:**
```
Type:       Scheduled script (printer supply monitoring)
Features:   - Query each printer's supply levels over SNMP every hour
            - Detect paper tray empty and jam states
            - Email the office manager when toner is below 10 percent
            - Write a daily status table to an HTML page
Input:      List of printer IP addresses and SNMP community string
Tech stack: Python, pysnmp, Jinja2, cron
```

---

## Example 356

**Intent:**
freezer in garage died and i lost all the meat, never again

**Spec:**
```
Type:       IoT system (freezer alarm)
Features:   - Read freezer temperature with a probe every 2 minutes
            - Send an alert when it rises above -12 C
            - Send an alert if the device loses power or Wi-Fi
            - Send a daily "all OK" message
Tech stack: ESP8266, DS18B20, ESPHome, Home Assistant, Uptime Kuma
```

---

## Example 357

**Intent:**
led strip under kitchen cabinets on with motion

**Spec:**
```
Type:       IoT system (lighting automation)
Features:   - Detect motion in the kitchen with a PIR sensor
            - Fade the LED strip on to 80 percent
            - Use 10 percent brightness at night
            - Fade off after 3 minutes without motion
Tech stack: ESP32, WLED firmware, PIR sensor, Home Assistant
```

---

## Example 358

**Intent:**
gps tracker on my motorbike if someone steals it

**Spec:**
```
Type:       IoT system (anti-theft tracker)
Features:   - Detect movement with an accelerometer while the bike is parked
            - Send an SMS with a map link when moved
            - Report location every minute after an alarm
            - Run from the bike battery with low sleep current
Tech stack: ESP32, SIM7000G (LTE-M + GPS), Arduino (C++), TinyGSM
```

---

## Example 359

**Intent:**
smart plug turn off tv at midnight kids

**Spec:**
```
Type:       IoT system (home automation)
Features:   - Turn off the TV smart plug at midnight on school nights
            - Allow until 1 am on weekends
            - Block turning it back on until 7 am
            - Let parents override from their phones
Tech stack: Tasmota smart plug, Home Assistant automations
```

---

## Example 360

**Intent:**
greenhouse tomatoes, want temp humidity light in grafana

**Spec:**
```
Type:       Data pipeline (greenhouse telemetry)
Features:   - Read temperature, humidity and light level every minute
            - Publish readings over MQTT
            - Write readings to a time-series database
            - Show dashboards and daily light integral in Grafana
API:        MQTT
            greenhouse/tomatoes/sensors
Storage:    InfluxDB
Tech stack: ESP32, BME280, TSL2591, Mosquitto, Telegraf, Grafana
```

---

## Example 361

**Intent:**
thermal camera to find heat leaks in my house walls

**Spec:**
```
Type:       Desktop application (thermal imaging)
Features:   - Read 32x24 thermal frames from an MLX90640
            - Show a colour heat map with min and max markers
            - Overlay temperatures on a normal camera image
            - Save snapshots with timestamps
            - Compare indoor and outdoor temperature for each snapshot
Tech stack: Raspberry Pi, MLX90640, Python, OpenCV, Tkinter
```

---

## Example 362

**Intent:**
cheap sensor to know if my elderly neighbour's lights come on each evening

**Spec:**
```
Type:       IoT system (wellbeing check)
Features:   - Detect light in the living room with a light sensor
            - Record when lights turn on each evening
            - Alert the neighbour's family if no light by 9 pm
            - Send a weekly summary
Tech stack: ESP8266, BH1750, MicroPython, Telegram Bot API
```

---

## Example 363

**Intent:**
my van carrying medicines, temp must be logged for each delivery, driver uses phone

**Spec:**
```
Type:       Mobile application with backend
Auth:       Driver login (email + password)
Data model: Delivery(id, pharmacy_name, address, status, delivered_at)
            TempLog(id, delivery_id -> Delivery, min_c, max_c, avg_c)
Features:   - Read the cargo area temperature from a Bluetooth logger
            - Attach the temperature range to each delivery when it is completed
            - Warn the driver if temperature leaves 15-25 C
            - Capture a signature at the pharmacy
            - Upload records to the office
API:        REST
            GET  /deliveries/today
            POST /deliveries/{id}/complete
Storage:    PostgreSQL
Tech stack: React Native, react-native-ble-plx, Node.js, Express
```

---

## Example 364

**Intent:**
alexa tell me plants need water

**Spec:**
```
Type:       Bot (voice assistant skill)
Features:   - Read latest soil moisture values from the garden sensors
            - Answer "which plants need water" with a spoken list
            - Send a proactive notification when a plant is dry
            - Say when each plant was last watered
API:        I: REST
            GET  /api/plants/status
Tech stack: Alexa Skills Kit, AWS Lambda (Python), MQTT bridge to the garden sensors
```

---

## Example 365

**Intent:**
I would like to see energy consumption from our school's buildings so children can learn and compete to save power

**Spec:**
```
Type:       Data dashboard (school energy competition)
Data model: Building(id, name, class_group)
            Reading(id, building_id -> Building, kwh, period_start)
Features:   - Collect half-hourly energy readings from each building's meter
            - Show a big-screen leaderboard of percent saved against last month
            - Show live power with a friendly gauge
            - Give badges to the class with the best weekly saving
            - Show tips on how to save energy
Storage:    InfluxDB
Tech stack: Python, FastAPI, Svelte, Modbus energy meters
```

---

## Example 366

**Intent:**
hello, me and my friend have small farm in nigeria, want know soil ph and npk to know what fertilizer to buy

**Spec:**
```
Type:       IoT system (soil nutrient testing)
Data model: Sample(id, field_name, ph, nitrogen_mgkg, phosphorus_mgkg, potassium_mgkg, moisture_pct, taken_at)
Features:   - Read pH, NPK and moisture from an RS485 soil probe
            - Save each reading with the field name
            - Show the readings on a phone over Bluetooth
            - Suggest a fertilizer type based on low values
            - Export samples as CSV
Storage:    On-device SQLite
Tech stack: ESP32, RS485 7-in-1 soil sensor (Modbus), MIT App Inventor app
```

---

## Example 367

**Intent:**
museum gift shop till

**Spec:**
```
Type:       Desktop application (point of sale)
Data model: Product(id, sku, name, price, stock_qty)
            Sale(id, total, vat, payment_method, sold_at)
            SaleLine(id, sale_id -> Sale, product_id -> Product, quantity)
Features:   - Scan product barcodes
            - Apply member discounts
            - Take card payments through an integrated terminal
            - Print receipts
            - Show low stock reports
Storage:    SQLite
Tech stack: Odoo Point of Sale, USB barcode scanner, Epson receipt printer
```

---

## Example 368

**Intent:**
Our local council wants to measure footfall on the high street to show shops are recovering

**Spec:**
```
Type:       Data dashboard (footfall analytics)
Features:   - Count pedestrians with privacy-safe sensors on lamp posts
            - Aggregate counts per hour and per day
            - Compare footfall with the same week last year
            - Show market days and events on the chart
            - Publish weekly summaries as open data
Storage:    TimescaleDB
Tech stack: Raspberry Pi with Hailo AI camera (counts only, no images stored), Python, Grafana
```

---

## Example 369

**Intent:**
tablet in each ambulance to see the nearest hospital with free emergency beds

**Spec:**
```
Type:       Mobile application with backend
Auth:       Crew login with service ID
Data model: Hospital(id, name, lat, lon, specialties)
            Capacity(id, hospital_id -> Hospital, ed_beds_free, diverting, updated_at)
Features:   - Show hospitals ranked by travel time from the ambulance
            - Show free emergency beds and diversion status
            - Filter by specialty such as stroke or trauma
            - Send a pre-arrival notice to the chosen hospital
API:        REST
            GET  /hospitals/nearby?lat={lat}&lon={lon}
            POST /hospitals/{id}/prealert
Storage:    PostgreSQL
Tech stack: Kotlin (Android), Python, FastAPI, OSRM
```

---

## Example 370

**Intent:**
pick up litter project, volunteers log bags collected on a map

**Spec:**
```
Type:       Mobile application with backend
Auth:       Volunteer sign-in with Google
Data model: Cleanup(id, user_id, lat, lon, bags, photo_url, created_at)
Features:   - Log a cleanup with location, number of bags and a photo
            - Show all cleanups on a community map
            - Show totals per volunteer and per month
            - Highlight litter hotspots
API:        REST
            POST /cleanups
            GET  /cleanups?bbox={bbox}
Storage:    Firebase Firestore, Firebase Storage
Tech stack: Flutter, Firebase, Google Maps SDK
```

---

## Example 371

**Intent:**
water quality testing in the creek by school kids, upload results

**Spec:**
```
Type:       Web application (citizen science data entry)
Auth:       Teacher creates class accounts
Data model: Site(id, name, lat, lon)
            Sample(id, site_id -> Site, class_id, ph, turbidity_ntu, nitrate_mgl, temperature_c, sampled_at)
Features:   - Let students enter test results per site
            - Validate values against realistic ranges
            - Show trends at each site on charts
            - Compare sites on a map
            - Download data as CSV for lessons
Storage:    PostgreSQL
Tech stack: Python, Django, Chart.js, Leaflet
```

---

## Example 372

**Intent:**
i want the light outside my front door green if the bins collected

**Spec:**
```
Type:       IoT system (status indicator)
Features:   - Check the council collection schedule
            - Light a smart bulb blue on bin night evening
            - Turn it off at midnight
Tech stack: Home Assistant, waste_collection_schedule integration, smart bulb
```

---

## Example 373

**Intent:**
help me build a machine that sorts lego by colour

**Spec:**
```
Type:       IoT system (sorting machine)
Features:   - Feed bricks one at a time with a vibrating chute
            - Read each brick's colour with a colour sensor
            - Rotate a chute with a servo to the matching bin
            - Count bricks per colour
Tech stack: Arduino Uno, TCS3200 colour sensor, servo motors, Arduino (C++)
```

---

## Example 374

**Intent:**
alarm for when freezer in the church kitchen is open

**Spec:**
```
Type:       IoT system (door alarm)
Features:   - Detect the freezer door open with a reed switch
            - Beep after 1 minute open
            - Send a message to the kitchen volunteers after 5 minutes
Tech stack: ESP8266, reed switch, ESPHome, Telegram
```

---

## Example 375

**Intent:**
smart garden for my school with sensors that kids can see on website

**Spec:**
```
Type:       Web application (school garden dashboard)
Data model: Bed(id, name, crop)
            Reading(id, bed_id -> Bed, soil_moisture_pct, soil_temp_c, read_at)
Features:   - Show live moisture and temperature per garden bed
            - Show which beds need watering today
            - Show a growth photo diary uploaded by students
            - Explain each reading with kid-friendly text
Storage:    SQLite
Tech stack: Raspberry Pi Pico W sensors, MicroPython, Python, Flask
```

---

## Example 376

**Intent:**
dementia friendly clock that says the day and if it's morning or night

**Spec:**
```
Type:       IoT system (assistive clock)
Features:   - Show the day of the week in large letters
            - Show "morning", "afternoon", "evening" or "night"
            - Show the full date below
            - Dim the screen at night
            - Keep time from NTP
Tech stack: Raspberry Pi Zero 2 W, 10 inch HDMI display, Python, Pygame
```

---

## Example 377

**Intent:**
a wall touchscreen in the house to control all the lights and see cameras

**Spec:**
```
Type:       Web application (smart home control panel)
Features:   - Show buttons for every room's lights
            - Show live camera feeds
            - Show the alarm state and allow arming with a PIN
            - Show the weather and calendar
            - Wake the screen on approach
Tech stack: Home Assistant, custom Lovelace dashboard, Fully Kiosk Browser on a wall tablet
```

---

## Example 378

**Intent:**
tell me the bus is 5 minutes away so i can leave house

**Spec:**
```
Type:       Scheduled script (transit alert)
Features:   - Check live arrival predictions for my stop every minute between 7 and 9 am
            - Send a phone notification when the bus is 5 minutes away
            - Only alert on weekdays
Tech stack: Python, transit agency GTFS-Realtime feed, ntfy, systemd timer
```

---

## Example 379

**Intent:**
Arduino data logger for my bicycle speed and distance

**Spec:**
```
Type:       IoT system (bike computer)
Features:   - Count wheel rotations with a hall sensor
            - Calculate speed and distance from wheel circumference
            - Show speed and trip distance on an OLED
            - Save each ride to an SD card
Tech stack: Arduino Nano, hall sensor, SSD1306, SD card module, Arduino (C++)
```

---

## Example 380

**Intent:**
alerts if the youth hostel showers run out of hot water

**Spec:**
```
Type:       IoT system (hot water monitoring)
Features:   - Read the hot water cylinder temperature at the top
            - Warn staff when it drops below 45 C
            - Turn on the immersion booster below 40 C
            - Show the temperature on the reception screen
Tech stack: ESP32, DS18B20, Shelly Pro relay, ESPHome, Home Assistant
```

---

## Example 381

**Intent:**
track library visitors with door counter and show on website monthly

**Spec:**
```
Type:       Data pipeline (visitor statistics)
Features:   - Read hourly counts from the door counter API
            - Store counts per branch
            - Publish a monthly visits chart on the library website
            - Compare branches year on year
Storage:    PostgreSQL
Tech stack: Python, pandas, Plotly (static HTML export), cron
```

---

## Example 382

**Intent:**
my church old people can't hear the sermon, stream audio to their phones in the hall

**Spec:**
```
Type:       Web application (assistive audio streaming)
Features:   - Capture audio from the sound desk
            - Stream it with low latency over the local Wi-Fi
            - Let listeners join by scanning a QR code with no app
            - Let listeners adjust their own volume
Tech stack: Raspberry Pi, USB audio interface, Icecast, Liquidsoap, HTML5 audio
```

---

## Example 383

**Intent:**
Can you help me plan a node-red flow that reads modbus from my solar inverter

**Spec:**
```
Type:       IoT system (inverter data collection)
Features:   - Poll inverter Modbus TCP registers every 10 seconds
            - Convert raw registers to watts, volts and kWh
            - Publish values to MQTT topics
            - Write values to InfluxDB
            - Alert when the inverter reports a fault code
API:        MQTT
            solar/inverter/power
            solar/inverter/fault
Storage:    InfluxDB
Tech stack: Node-RED, node-red-contrib-modbus, Mosquitto, InfluxDB
```

---

## Example 384

**Intent:**
animal shelter kennels temperature in summer, dogs overheat

**Spec:**
```
Type:       IoT system (kennel climate monitoring)
Features:   - Read temperature in each kennel block
            - Turn on cooling fans above 27 C
            - Alert staff above 30 C
            - Show a summer history
Tech stack: Raspberry Pi Pico W, MicroPython, SHT31 sensors, Adafruit IO
```

---

## Example 385

**Intent:**
Can I use a raspberry pi as a cash register for my food stall with a little printer?

**Spec:**
```
Type:       Desktop application (point of sale)
Data model: Item(id, name, price)
            Sale(id, total, paid_cash, sold_at)
            SaleLine(id, sale_id -> Sale, item_id -> Item, quantity)
Features:   - Show items as touch buttons
            - Calculate total and change
            - Print a receipt
            - Open the cash drawer through the printer
            - Show daily totals
Storage:    SQLite
Tech stack: Raspberry Pi, 7 inch touchscreen, Python, Kivy, python-escpos
```

---

## Example 386

**Intent:**
kids library: book return box that counts returns and tweets thank you

**Spec:**
```
Type:       IoT system (book drop counter)
Features:   - Detect books dropping through the chute with an IR beam
            - Count returns per day
            - Post a daily thank-you message with the count on social media
            - Light a smiley face when a book is returned
Tech stack: ESP32, IR break beam, Arduino (C++), Mastodon API
```

---

## Example 387

**Intent:**
humidity sensor in the archive room of the parish records

**Spec:**
```
Type:       IoT system (archive climate monitoring)
Features:   - Read humidity and temperature every 15 minutes
            - Warn the archivist when humidity is above 60 percent
            - Run a dehumidifier plug automatically
            - Keep a yearly log for the diocese
Tech stack: ESP32, SHT41, ESPHome, Home Assistant
```

---

## Example 388

**Intent:**
In our village there is no gas station so we share diesel tank, want to record who takes how much

**Spec:**
```
Type:       Web application (shared fuel tracking)
Auth:       Member PIN at the pump
Data model: Member(id, name, pin_hash, balance)
            Dispense(id, member_id -> Member, litres, price_per_litre, dispensed_at)
            Delivery(id, litres, cost, delivered_at)
Features:   - Unlock the pump after a member enters their PIN
            - Measure litres dispensed with a flow meter
            - Charge the member at the current average price
            - Show tank level and member balances
            - Record fuel deliveries
Storage:    PostgreSQL
Tech stack: ESP32 with keypad and flow meter, Python, Django
```

---

## Example 389

**Intent:**
smart scale under cat litter box so I know cat is peeing normally

**Spec:**
```
Type:       IoT system (pet health monitoring)
Data model: Visit(id, cat_weight_kg, duration_s, visited_at)
Features:   - Detect cat visits from weight changes on load cells under the litter box
            - Record the cat's weight and visit duration
            - Show visits per day
            - Alert when visits rise sharply (possible urinary problem)
Storage:    InfluxDB
Tech stack: ESP32, HX711 with 4 load cells, ESPHome, Home Assistant
```

---

## Example 390

**Intent:**
plant nursery wants plant labels with QR codes linking to care info

**Spec:**
```
Type:       Web application (plant info labels)
Auth:       Staff login
Data model: Plant(id, name, latin_name, light, watering, hardiness_zone, photo_url)
Features:   - Create plant care pages
            - Generate a printable label with a QR code per plant
            - Show a mobile-friendly care page when scanned
            - Count scans per plant
Storage:    PostgreSQL
Tech stack: Python, Django, qrcode, WeasyPrint
```

---

## Example 391

**Intent:**
Need a dashboard that shows all our ESP32 sensors and if they are online

**Spec:**
```
Type:       Data dashboard (device health)
Data model: Device(id, name, firmware_version, last_seen_at, rssi, uptime_s)
Features:   - Receive heartbeat messages over MQTT
            - Show each device with last seen time, signal strength and firmware
            - Mark devices offline after 10 minutes
            - Allow an OTA firmware update from the dashboard
API:        MQTT
            devices/{id}/heartbeat
            devices/{id}/ota
Tech stack: Node-RED dashboard, Mosquitto, ESP32 with ArduinoOTA
```

---

## Example 392

**Intent:**
track ventilator and oxygen concentrator hours for maintenance in rural clinics

**Spec:**
```
Type:       Web application (medical equipment maintenance)
Auth:       Technician login (email + password)
Data model: Clinic(id, name, region)
            Device(id, clinic_id -> Clinic, type, serial, hours)
            MaintenanceRecord(id, device_id -> Device, done_at, hours_at_service, notes)
Features:   - Record running hours reported by clinic staff by SMS
            - Show devices due for filter changes and service
            - Schedule technician visits by region
            - Log completed maintenance
            - Show devices out of service
Storage:    PostgreSQL
Tech stack: Python, Django, Africa's Talking SMS API
```

---

## Example 393

**Intent:**
tiny house off grid show battery solar and water tank on one screen

**Spec:**
```
Type:       Data dashboard (off-grid monitoring)
Features:   - Read battery state of charge and solar power from the charge controller
            - Read the water tank level
            - Show everything on a wall tablet
            - Warn when battery is below 30 percent
Tech stack: Victron Cerbo GX, Node-RED on Venus OS, Home Assistant
```

---

## Example 394

**Intent:**
barcode scanner for library inventory, find books on wrong shelf

**Spec:**
```
Type:       Mobile application (shelf reading)
Features:   - Scan book barcodes along a shelf in order
            - Compare call numbers to the expected order
            - Flag books that are misplaced
            - Flag books marked lost or checked out
            - Save a report of problems per shelf
Tech stack: Kotlin (Android), ML Kit barcode scanning, Koha REST API
```

---

## Example 395

**Intent:**
lone worker safety app for our care staff visiting homes

**Spec:**
```
Type:       Mobile application with backend
Auth:       Staff login (email + password)
Data model: Visit(id, staff_id, client_address, check_in_at, expected_end_at, check_out_at)
            Alarm(id, staff_id, lat, lon, raised_at)
Features:   - Check in at the start of a home visit with expected duration
            - Raise an alarm automatically if the worker does not check out in time
            - Send an SOS with location by pressing a button
            - Alert the office duty manager
API:        REST
            POST /visits
            POST /visits/{id}/checkout
            POST /alarms
Storage:    PostgreSQL
Tech stack: Flutter, Python, FastAPI, Firebase Cloud Messaging
```

---

## Example 396

**Intent:**
chicken incubator for eggs temp humidity and turning

**Spec:**
```
Type:       IoT system (egg incubator)
Features:   - Hold temperature at 37.5 C with a heater and PID
            - Keep humidity at 50-55 percent
            - Turn the eggs every 2 hours with a motor
            - Stop turning 3 days before hatch
            - Show day count and readings on an LCD
Tech stack: Arduino Uno, DHT22, relay, servo turner, Arduino (C++)
```

---

## Example 397

**Intent:**
sensor in my car telling if i left kid or dog inside and it's hot

**Spec:**
```
Type:       IoT system (vehicle occupant safety)
Features:   - Detect presence in the back seat with a mmWave radar
            - Read cabin temperature
            - Send an urgent alert when presence is detected and the car is locked
            - Escalate if temperature rises above 30 C
Tech stack: ESP32, LD2410, SIM7600 LTE module, Arduino (C++)
```

---

## Example 398

**Intent:**
soil moisture sensors in a park so the city waters only dry areas

**Spec:**
```
Type:       IoT system (smart park irrigation)
Data model: Zone(id, name, valve_id)
            Reading(id, zone_id -> Zone, moisture_pct, read_at)
Features:   - Collect soil moisture per irrigation zone over LoRaWAN
            - Skip watering zones above the moisture target
            - Adjust run time with evapotranspiration from weather data
            - Report water saved per month
Storage:    TimescaleDB
Tech stack: LoRaWAN soil sensors, ChirpStack, Python, Rain Bird controller API
```

---

## Example 399

**Intent:**
track cleaning rounds in the hospital by nfc tags in each room

**Spec:**
```
Type:       Mobile application with backend
Auth:       Cleaner login with badge
Data model: Room(id, name, nfc_tag)
            CleaningLog(id, room_id -> Room, cleaner_id, cleaned_at, type)
Features:   - Tap the room's NFC tag to log cleaning
            - Choose routine or deep clean
            - Show supervisors rooms not cleaned in the last 24 hours
            - Report cleaning frequency per ward
API:        REST
            POST /cleaning-logs
            GET  /rooms/overdue
Storage:    PostgreSQL
Tech stack: Kotlin (Android) NFC, Python, FastAPI
```

---

## Example 400

**Intent:**
stair lift battery check for my grandad

**Spec:**
```
Type:       IoT system (mobility aid monitoring)
Features:   - Measure the stair lift battery voltage
            - Warn when the lift is not parked on its charging point
            - Alert family when voltage falls below a safe level
            - Send a weekly status message
Tech stack: ESP32, voltage divider, ESPHome, Home Assistant
```

---

## Example 401

**Intent:**
wifi doorbell for deaf person vibrates a wristband

**Spec:**
```
Type:       IoT system (accessible doorbell)
Features:   - Detect a doorbell press
            - Send the event to a wristband over ESP-NOW
            - Vibrate in a pattern unique to the doorbell
            - Light an LED on the wristband until acknowledged
Tech stack: ESP32-C3 doorbell and wristband, ESP-NOW, Arduino (C++), vibration motor
```

---

## Example 402

**Intent:**
track the honey harvested from each of our 40 hives and sell jars with batch labels

**Spec:**
```
Type:       Web application (honey traceability)
Auth:       Beekeeper login (email + password)
Data model: Hive(id, name, apiary)
            Harvest(id, hive_id -> Hive, kg, harvested_on)
            Batch(id, harvest_ids, jar_count, best_before, label_code)
Features:   - Record harvests per hive
            - Combine harvests into jarring batches
            - Print jar labels with batch code and best-before date
            - Show yield per hive per season
            - Trace a jar back to its hives
Storage:    PostgreSQL
Tech stack: Python, Django, Zebra label printer
```

---

## Example 403

**Intent:**
weekly email of which church members birthdays and anniversaries

**Spec:**
```
Type:       Scheduled script (member reminders)
Features:   - Read member birthdays and anniversaries from the church database export
            - Find those falling in the coming week
            - Email the list to the pastor every Monday
            - Include phone numbers for a call
Input:      CSV export of members
Tech stack: Python, pandas, smtplib, cron
```

---

## Example 404

**Intent:**
i make jewelry and want my laser engraver jobs queued from a web page

**Spec:**
```
Type:       Web application (machine job queue)
Features:   - Upload SVG designs and set power and speed
            - Convert designs to G-code
            - Queue jobs and send them to the engraver over serial
            - Show progress and allow pause
            - Keep a history of settings per material
Tech stack: Python, Flask, svg2gcode, pyserial, GRBL
```

---

## Example 405

**Intent:**
elderly day centre bus pickups, driver sees list and families get text when bus is near

**Spec:**
```
Type:       Mobile application with backend
Auth:       Driver login; staff login
Data model: Client(id, name, address, phone_family)
            Run(id, date, driver_id)
            RunStop(id, run_id -> Run, client_id -> Client, order, picked_up_at)
Features:   - Show the driver the pickup list in order
            - Text families when the bus is 10 minutes away
            - Mark clients as picked up or absent
            - Show the centre who is on the bus
API:        REST
            GET  /runs/today
            POST /runs/{id}/stops/{stop_id}/pickup
Storage:    PostgreSQL
Tech stack: React Native, Node.js, Twilio SMS API
```

---

## Example 406

**Intent:**
museum: display case vibration and opened alarm

**Spec:**
```
Type:       IoT system (exhibit security)
Features:   - Detect vibration on the glass with an accelerometer
            - Detect case opening with a hidden reed switch
            - Alert security staff instantly
            - Allow authorised opening with a key switch that disables the alarm
Tech stack: ESP32, ADXL345, Arduino (C++), MQTT to the security console
```

---

## Example 407

**Intent:**
lab students should sign out and sign in the multimeters and oscilloscopes

**Spec:**
```
Type:       Web application (equipment checkout)
Auth:       Student login with university SSO
Data model: Equipment(id, type, asset_tag, status)
            Checkout(id, equipment_id -> Equipment, student_id, out_at, returned_at)
Features:   - Scan the equipment QR code and student card to sign out
            - Sign items back in
            - Show items still out at the end of the lab
            - Email students with overdue items
Storage:    PostgreSQL
Tech stack: Python, Flask, html5-qrcode
```

---

## Example 408

**Intent:**
build a weather station for my school with arduino and show on lcd

**Spec:**
```
Type:       IoT system (weather station)
Features:   - Read temperature, humidity and pressure from a BME280
            - Show values on a 20x4 LCD
            - Show the pressure trend as rising, steady or falling
            - Log values to an SD card every 10 minutes
Tech stack: Arduino Uno, BME280, 20x4 I2C LCD, SD card module, Arduino (C++)
```

---

## Example 409

**Intent:**
hey can u make something where my garage freezer, chest freezer and fridge all show on one screen with temps

**Spec:**
```
Type:       Data dashboard (appliance temperatures)
Features:   - Read temperatures from wireless probes in each appliance
            - Show all three on one dashboard tile
            - Colour values outside safe ranges red
            - Send an alert when any appliance is out of range for 30 minutes
Tech stack: Govee BLE thermometers, Theengs Gateway, Home Assistant
```

---

## Example 410

**Intent:**
our charity shop gets donated electronics and needs PAT testing records

**Spec:**
```
Type:       Web application (safety test records)
Auth:       Volunteer login
Data model: Item(id, description, donated_on, barcode)
            PatTest(id, item_id -> Item, tester, result, insulation_mohm, tested_on)
Features:   - Register donated electrical items with a barcode label
            - Record PAT test results
            - Block items that failed from going on sale
            - Show items awaiting testing
            - Print a pass label
Storage:    SQLite
Tech stack: Python, Flask, Brother label printer
```

---

## Example 411

**Intent:**
water bottle filling station counts bottles saved

**Spec:**
```
Type:       IoT system (usage counter display)
Features:   - Measure water dispensed with a flow sensor
            - Convert litres to 500 ml bottles saved
            - Show the running total on an LED display
            - Send daily totals to the sustainability dashboard
Tech stack: ESP32, flow sensor, MAX7219 LED display, Arduino (C++)
```

---

## Example 412

**Intent:**
sensors in the beehive apiary to know if someone steals hive

**Spec:**
```
Type:       IoT system (hive theft alert)
Features:   - Detect hive movement with an accelerometer
            - Send an alert with GPS location when moved
            - Report location every 10 minutes after theft
            - Run on battery for a year
Tech stack: LoRaWAN GPS tracker, The Things Network, Node-RED
```

---

## Example 413

**Intent:**
i got sensors from aliexpress modbus rs485 for temperature, want read them with python

**Spec:**
```
Type:       Command-line script (Modbus data logging)
Features:   - Poll each RS485 sensor by its Modbus address
            - Read holding registers for temperature and humidity
            - Scale raw values to real units
            - Write readings to a CSV every minute
            - Report sensors that do not answer
Input:      Serial port, list of Modbus addresses, poll interval
Tech stack: Python, pymodbus, USB to RS485 adapter
```

---

## Example 414

**Intent:**
shelter for women needs to know how many beds free without showing location publicly

**Spec:**
```
Type:       Web application (confidential bed availability)
Auth:       Verified referrer login with 2FA
Data model: Refuge(id, code_name, region, accepts_children)
            Availability(id, refuge_id -> Refuge, spaces, updated_at)
Features:   - Let refuge staff update free spaces
            - Show availability by region without addresses
            - Restrict access to verified referral agencies
            - Log every view for security audits
Storage:    PostgreSQL (encrypted)
Tech stack: Python, Django, django-otp
```

---

## Example 415

**Intent:**
blinds and lights in conference room to presentation mode with one button

**Spec:**
```
Type:       IoT system (room automation)
Features:   - Lower the blinds
            - Dim the room lights to 20 percent
            - Turn on the projector over RS-232
            - Restore everything with a second press
Tech stack: Home Assistant, KNX integration, ESP32 RS-232 bridge
```

---

## Example 416

**Intent:**
monitor weight of our propane tank for the farm kitchen

**Spec:**
```
Type:       IoT system (gas tank level)
Features:   - Weigh the propane cylinder on a load cell platform
            - Calculate kilograms of gas left
            - Warn when below 20 percent
            - Estimate days left from usage
Tech stack: ESP32, HX711, ESPHome, Home Assistant
```

---

## Example 417

**Intent:**
we train guide dogs and want to record each dog's training sessions on a phone

**Spec:**
```
Type:       Mobile application with backend
Auth:       Trainer login (email + password)
Data model: Dog(id, name, birth_date, trainer_id)
            Session(id, dog_id -> Dog, skill, score, notes, trained_at)
Features:   - Log training sessions with skill and score
            - Show progress per skill
            - Flag dogs behind schedule
            - Share progress reports with the puppy raisers
API:        REST
            GET  /dogs
            POST /dogs/{id}/sessions
Storage:    PostgreSQL
Tech stack: Flutter, Supabase
```

---

## Example 418

**Intent:**
the temperature of the server cupboard at our charity office

**Spec:**
```
Type:       IoT system (temperature alerting)
Features:   - Read temperature every minute
            - Email the IT volunteer above 30 C
            - Show a 7-day chart
Tech stack: Raspberry Pi Pico W, MicroPython, DHT22, ThingSpeak
```

---

## Example 419

**Intent:**
pharmacy robot dispenser? no, just tell pharmacist which drawer the medicine is in by lighting it

**Spec:**
```
Type:       IoT system (put-to-light)
Data model: Drawer(id, cabinet, led_index)
            Medicine(id, name, drawer_id -> Drawer)
Features:   - Search a medicine by name or barcode
            - Light the LED on its drawer
            - Turn the light off when the drawer is closed
            - Show which drawer on screen too
Storage:    SQLite
Tech stack: Raspberry Pi, Python, Flask, WS2812 LED strips
```

---

## Example 420

**Intent:**
please make automatic watering for my strawberry in greenhouse using arduino uno

**Spec:**
```
Type:       IoT system (drip irrigation)
Features:   - Read 2 soil moisture sensors
            - Open a 12 V solenoid valve when soil is dry
            - Water for 2 minutes then wait 30 minutes before checking again
            - Do not water at night
Tech stack: Arduino Uno, capacitive soil sensors, DS3231 RTC, relay, Arduino (C++)
```

---

## Example 421

**Intent:**
count the visitors at our charity shop door and compare with sales

**Spec:**
```
Type:       Data analysis script (conversion rate)
Features:   - Load hourly visitor counts from the door counter export
            - Load hourly transactions from the till export
            - Calculate conversion rate per hour and day
            - Plot busy hours with low conversion
Input:      Door counter CSV, till transactions CSV
Tech stack: Python, pandas, matplotlib
```

---

## Example 422

**Intent:**
smoke detectors in our museum all connected and tell the guard

**Spec:**
```
Type:       IoT system (fire alarm integration)
Features:   - Receive alarm states from wireless smoke detectors
            - Show the triggered room on the guard's floor plan screen
            - Send alerts to guards' radios via a gateway
            - Log tests and alarms
Tech stack: Zigbee smoke detectors, Zigbee2MQTT, Node-RED dashboard
```

---

## Example 423

**Intent:**
fleet of e-scooters for campus, check battery and where they are

**Spec:**
```
Type:       Web application (scooter fleet management)
Auth:       Operations staff login
Data model: Scooter(id, code, battery_pct, lat, lon, status, updated_at)
Features:   - Receive battery and GPS from each scooter every minute
            - Show scooters on a campus map
            - List scooters below 20 percent battery for charging rounds
            - Lock scooters remotely
API:        MQTT
            scooters/{id}/telemetry
            scooters/{id}/command
Storage:    PostgreSQL
Tech stack: Python, FastAPI, EMQX, Leaflet
```

---

## Example 424

**Intent:**
library makerspace sewing machine and 3d printer booking with training needed

**Spec:**
```
Type:       Web application (makerspace booking)
Auth:       Library card login
Data model: Machine(id, name, requires_induction)
            Induction(id, card_number, machine_id -> Machine, passed_on)
            Booking(id, machine_id -> Machine, card_number, starts_at, ends_at)
Features:   - Show machines and free slots
            - Allow booking only after induction
            - Let staff record inductions
            - Limit bookings to 2 hours per day
Storage:    PostgreSQL
Tech stack: Ruby on Rails, FullCalendar
```

---
