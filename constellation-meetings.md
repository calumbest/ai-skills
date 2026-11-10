---
name: constellation-meetings
description: Book a Constellation meeting room in Robin for each of today's meetings, then tidy the calendar so each meeting is one event with the room noted on it. Use for /constellation-meetings, "book my rooms for today", or "book Constellation rooms".
---

# /constellation-meetings — Book Constellation Rooms for Today's Meetings

> **What I use it for:** My morning routine on office days. It reads my calendar, books a call booth in Robin for each meeting (and a bigger room for group lunches), then removes the duplicate calendar events Robin creates and notes the room on the real meeting instead.

Run in the morning on an office day. Books a room in [Robin](https://dashboard.robinpowered.com) for each of today's meetings that needs one, then tidies the calendar so each meeting is one event with the room noted in its description.

**Argument:** none for today. Optional: a date (`tomorrow`, `2026-11-12`), or notes for the day ("in from 10", "skip the 2pm", "lunch is 6 people").

## Setup (once)

- **Claude in Chrome**, with the user logged in to Robin in that browser. Robin has no API access here, so the booking is done by clicking through the site. If an organization policy blocks `dashboard.robinpowered.com` for Claude in Chrome, an admin has to allow it.
- **Google Calendar access** that can list, patch and delete events. The commands below use the `gws` CLI; a Calendar connector works too.
- **Slack search** (optional), used to tell a lunch from a call.
- **Room table and preferences**, built on the first run (see Rooms): the rooms with their IDs and capacities, the user's first-choice room and fallback order, and any meetings that should get extra time.

## How Robin behaves

- Booking a room makes Robin's scheduler account create a **second calendar event**, organized by the room's resource calendar, with the user invited as `needsAction`. It reaches the calendar within about 20 seconds. Its `location` is the room's long name. Make one booking on the first run and note the event's `creator` address: that address is how the skill recognizes Robin's events (called "the Robin scheduler" below).
- Deleting that event from the user's calendar records them as "declined" on it, but **the Robin booking stays**. Robin then shows "You declined, 0 of 1 going".
- Robin shows "Check in starts 10 minutes before" on bookings. This skill ignores check-in.
- Navigation in Claude in Chrome can fail intermittently with "blocked by your organization's policy". Retry once or twice before giving up.

## Rooms

The room list isn't published here. Build it on the first run and save it in this file (or a private notes file) as a table of room, Robin space ID, capacity and notes:

1. Open Robin's **Meeting spaces** page in Chrome and note the `locationId` in the URL.
2. Expand each floor and list the rooms. Each room name links to `.../locations/<locationId>/spaces/<id>/details`, which gives its ID.
3. Open each room's details page for its type, capacity ("Fits N"), amenities (whether it has video) and any note about broken equipment.
4. Ask the user for their first-choice room and fallback order, and mark rooms that should never be booked (nap rooms, for example).

Booking grid for a date: `https://dashboard.robinpowered.com/constellation/schedule/meeting-rooms?currentDate=YYYY-MM-DD&locationId=<locationId>`.

Re-check the table against the grid if a room is missing or new.

## Procedure

### 1. Read today's calendar

`gws calendar events list --params '{"calendarId":"primary","timeMin":"<today 00:00 local>","timeMax":"<tomorrow 00:00 local>","singleEvents":true,"orderBy":"startTime"}' 2>/dev/null`

Sort events into three groups:

- **Already-booked rooms:** events created by the Robin scheduler (organizer is a `@resource.calendar.google.com` address). These are existing Robin bookings; match each to the meeting it overlaps.
- **Meetings that need a room:** see the rules below.
- **Everything else:** ignored.

### 2. Decide which meetings need a room

Needs a room:
- A call or meeting with at least one other person, starting from now on (never book the past), that the user has accepted or organizes.
- That includes meetings they sit in on and phone calls.

No room:
- Events with only the user on them.
- **Lunch with one other person:** they go and eat, so no room. Lunch with a larger group does get a room (step 3).
- Declined events, all-day events, and anything with a real-world location outside Constellation (a restaurant, another office).
- Meetings that already have an overlapping Robin booking (go straight to step 5 for those if the calendar still has the duplicate).
- Meetings outside the hours the user is in the office, **when they give those hours** in the invocation ("in from 10", "leaving at 4"). There is no default cutoff. If they say nothing, cover every remaining meeting today, and list the early or late ones in the report so they can cancel any they'll take from home.

**Telling a lunch from a call.** Titles rarely say "lunch". Treat a meeting as a possible lunch when it falls in a plausible lunch window (roughly 11:30 am–1:30 pm) and nothing on the event points to a call (no video link, no phone number, the other people are colleagues who could be in the office). Then check Slack for the plan: search the user's recent DMs and threads with the attendees for words like "lunch", "eat", "grab food". If it's still unclear after that, book the room and say so in the report.

### 3. Pick a room and a time for each

**Size.** Count the people who will be in the room, not on the invite: for a video call that is the user alone, so a booth. Use the attendee count only for in-person meetings and lunches.
- 1–2 people in the room: the first-choice booth; if taken, the other 2-person booths and rooms in the order listed, then a free 4-person room on the user's floor.
- Lunch or in-person meeting with 3+ people: the smallest free room that fits everyone, preferring the user's floor. For lunch, attendees who have declined don't count.
- Needs video and more than one person in the room: skip the rooms marked "No video".

**Time.** Round the end up to the next 15 minutes (20-minute meeting → 30, 30 → 30). Meetings the user has listed as running over get an extra 15 minutes (mine: 1:1s with my manager). If the padding collides with the user's next booking in the same room, end at that booking's start.

**Back-to-back meetings** in the same room are booked as separate bookings, one per meeting, so each maps to one calendar event.

### 4. Book

Book straight away, with no approval step, and report afterwards. Running the command is the go-ahead for the bookings and the calendar tidy-up in step 5. (If you'd rather approve a plan first, add that step here.)

For each booking, in Chrome:
1. Open the grid URL for the date. One floor is expanded by default; other floors need a click on the floor name.
2. Click the room's row at the start time. A "Create event" panel opens with the room filled in.
3. Set Title to the calendar meeting's title, set the start and end times (the default is 30 minutes), leave "Mark as private" ticked, and Save.
4. Confirm the new block appears in the room's row. If Robin refuses (room taken in the meantime, booking limit), fall back to the next room and say so in the report.

### 5. Tidy the calendar

For each new booking, wait for Robin's event to arrive (poll `events list` for an event created by the Robin scheduler at that time; it takes about 20 seconds), then:

1. **Add the room to the real meeting's description.** Append one line to the original event's `description`: `<Name>: Use <room> in Constellation`. Keep the existing description and add the line after it, separated by `<br><br>` (descriptions are HTML); if the description is empty, the line is the whole description. Don't touch the title or location. Skip the patch if the line is already there. On a recurring meeting, patch the instance ID for that day, not the series. Always pass `sendUpdates: none` so no attendee is emailed; on events the user organizes, attendees can still see the line if they open the event, which is why it's addressed to the user by name.
2. **Accept** Robin's event (patch the user's `responseStatus` to `accepted`, `sendUpdates: none`).
3. **Delete** Robin's event from the user's calendar (`events delete`, `sendUpdates: none`).

Never delete anything that isn't a Robin scheduler event, and never edit anything on a real meeting beyond that one description line. Before deleting, check the event's creator is the Robin scheduler.

### 6. Verify and report

Re-read the calendar and the Robin grid. Report one line per meeting: room booked, or why not (e.g. "no room: lunch for two"). Say which calls were judgment calls, such as a room booked for a meeting that might have been a lunch, and any meeting where no suitable room was free. Call out anything that failed part-way (room booked but calendar not tidied, or the reverse) so the user can fix it by hand.

## Don'ts

- Don't cancel or change a booking the user made themselves unless they ask.
- Don't book for other people, add other people to a Robin booking, or message anyone.
- Don't book more than one room for the same time slot.
- Don't sign in for the user: if Robin shows a sign-in page, stop and ask them to log in.
