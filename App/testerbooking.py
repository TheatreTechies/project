from datetime import datetime
from app import create_app, db
from app.models import Booking, BookedSeat

# Create the Flask app context
app = create_app()

# Define the function to book test seats
def book_test_seats():
    # Specify the test data
    user_id = 1
    program_id = 1
    test_seats = [
        {"category": "Stalls", "row": "A", "number": 5, "full_name": "John Doe", "age": 30},
        {"category": "Stalls", "row": "A", "number": 6, "full_name": "Jane Smith", "age": 28},
        {"category": "Circle", "row": "B", "number": 12, "full_name": "Alice Johnson", "age": 35},
        {"category": "Circle", "row": "B", "number": 13, "full_name": "Bob Brown", "age": 40},
    ]
    booking_price = 150.00  # Example price for the booking

    # Add the test data to the database
    with app.app_context():  # Use the app context to interact with the database
        # Create a new booking
        booking = Booking(
            user_id=user_id,
            program_id=program_id,
            price=booking_price,
        )
        
        # Add the booking to the session
        db.session.add(booking)
        db.session.flush()  # Flush to get the booking ID
        
        # Add booked seats for this booking
        for seat_data in test_seats:
            booked_seat = BookedSeat(
                booking_id=booking.id,  # Use the ID of the new booking
                category=seat_data["category"],
                row=seat_data["row"],
                number=seat_data["number"],
                full_name=seat_data["full_name"],
                age=seat_data["age"],
            )
            db.session.add(booked_seat)
        
        # Commit the session to save in the database
        db.session.commit()

    print("Test seats booked successfully!")


if __name__ == '__main__':
    book_test_seats()
