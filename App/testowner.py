from datetime import datetime, timedelta
from app import create_app, db
from app.models import Program, Booking, BookedSeat

# Create the Flask app context
app = create_app()

# Define the function to add programs and bookings
def add_programs_and_bookings():
    user_id = 1
    today = datetime.now()

    # Define past and upcoming programs
    programs = [
        # Past Programs
        {"name": "Past AI Conference", "datetime": today - timedelta(days=10), "base_price": 100.00, "description": "An AI conference held last week."},
        {"name": "Past Blockchain Summit", "datetime": today - timedelta(days=5), "base_price": 150.00, "description": "A blockchain summit held earlier this month."},
        # Upcoming Programs
        {"name": "Upcoming Python Workshop", "datetime": today + timedelta(days=5), "base_price": 50.00, "description": "A beginner-friendly Python workshop."},
        {"name": "Upcoming AI for Good", "datetime": today + timedelta(days=10), "base_price": 200.00, "description": "Explore AI for social good."}
    ]

    # Test booking data (common for all programs)
    test_seats = [
        {"category": "Stalls", "row": "A", "number": 5, "full_name": "John Doe", "age": 30},
        {"category": "Stalls", "row": "A", "number": 6, "full_name": "Jane Smith", "age": 28},
        {"category": "Circle", "row": "B", "number": 12, "full_name": "Alice Johnson", "age": 35},
        {"category": "Circle", "row": "B", "number": 13, "full_name": "Bob Brown", "age": 40},
    ]

    with app.app_context():  # Use the app context to interact with the database
        for program_data in programs:
            # Create and add the program
            program = Program(
                name=program_data["name"],
                datetime=program_data["datetime"],
                base_price=program_data["base_price"],
                sale_start_datetime=program_data["datetime"] - timedelta(days=15),  # Sales start 15 days before the event
                description=program_data["description"],
                is_cancelled=False  # Set default as not cancelled
            )
            db.session.add(program)
            db.session.flush()  # Flush to get the program ID

            # Create a booking for this program
            booking = Booking(
                user_id=user_id,
                program_id=program.id,
                price=program.base_price * len(test_seats)  # Total price based on seats
            )
            db.session.add(booking)
            db.session.flush()  # Flush to get the booking ID

            # Add booked seats for this booking
            for seat_data in test_seats:
                booked_seat = BookedSeat(
                    booking_id=booking.id,
                    category=seat_data["category"],
                    row=seat_data["row"],
                    number=seat_data["number"],
                    full_name=seat_data["full_name"],
                    age=seat_data["age"]
                )
                db.session.add(booked_seat)

        # Commit all changes to the database
        db.session.commit()

    print("Programs and bookings added successfully!")

if __name__ == '__main__':
    add_programs_and_bookings()
