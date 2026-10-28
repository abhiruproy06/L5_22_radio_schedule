"""Manage a simple in-memory radio station programme schedule."""

import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    """
    CREATE TABLE slots (
        id INTEGER PRIMARY KEY,
        show TEXT,
        host TEXT,
        start_hour INTEGER,
        minutes INTEGER
    )
    """
)
schedule_state = {"booked_minutes": 0}


def add_slot(show, host, start_hour, minutes):
    """Add a programme slot and update the total booked minutes."""
    conn.execute(
        """
        INSERT INTO slots (show, host, start_hour, minutes)
        VALUES (?, ?, ?, ?)
        """,
        (show, host, start_hour, minutes),
    )
    schedule_state["booked_minutes"] += minutes


def slot_label(show, host):
    """Return a readable label for a programme and its host."""
    return f"{show} hosted by {host}"


def overlap_free(start_hour, duration, next_start_hour):
    """Return whether a programme finishes before the next one starts."""
    return start_hour + duration <= next_start_hour


def morning_shows():
    """Return programme names scheduled before noon."""
    if schedule_state["booked_minutes"] <= 0:
        return []

    return [
        row[0]
        for row in conn.execute(
            "SELECT show FROM slots WHERE start_hour < ?",
            (12,),
        )
    ]


def remove_slot(slot_id):
    """Remove a programme slot using its ID."""
    conn.execute("DELETE FROM slots WHERE id = ?", (slot_id,))


def main():
    """Demonstrate the radio schedule operations."""
    add_slot("Sunrise Beats", "Vik", 7, 60)
    add_slot("Midday Talk", "Anu", 13, 45)
    print(slot_label("Sunrise Beats", "Vik"))
    print(overlap_free(7, 1, 13), morning_shows())
    remove_slot(2)


if __name__ == "__main__":
    main()
