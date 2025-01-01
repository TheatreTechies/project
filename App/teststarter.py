from datetime import datetime, timedelta
from app import create_app, db
from app.models import Program

# Create the Flask app context
app = create_app()

# Define the function to add example programs
def add_example_programs():
    # Get yesterday's date and time
    sale_start_datetime = datetime.now() - timedelta(days=1)
    
    # List of example programs
    programs = [
        {"name": "AI Industry Network", "datetime": datetime(2025, 12, 10, 9, 0), "base_price": 100.00, "description": "A conference for AI enthusiasts."},
        {"name": "Digital Currency Event", "datetime": datetime(2025, 12, 12, 10, 0), "base_price": 150.00, "description": "Exploring the future of digital currency."},
        {"name": "Python for Everybody", "datetime": datetime(2025, 12, 13, 11, 0), "base_price": 50.00, "description": "A beginner-friendly Python programming workshop."},
        {"name": "Workwise Summit", "datetime": datetime(2025, 12, 14, 9, 0), "base_price": 200.00, "description": "The ultimate summit on career development."},
        {"name": "Brand Development Workshop", "datetime": datetime(2025, 12, 15, 10, 0), "base_price": 120.00, "description": "Learn how to develop your brand."},
        {"name": "Look Development Course", "datetime": datetime(2025, 12, 16, 14, 0), "base_price": 180.00, "description": "Master look development for animation and VFX."},
        {"name": "Capital Investment Seminar", "datetime": datetime(2025, 12, 17, 11, 0), "base_price": 250.00, "description": "An advanced seminar on investment strategies."},
        {"name": "Entrepreneurship Training", "datetime": datetime(2025, 12, 18, 15, 0), "base_price": 130.00, "description": "A workshop to kickstart your entrepreneurial journey."},
        {"name": "Blockchain Conference", "datetime": datetime(2025, 12, 19, 9, 30), "base_price": 300.00, "description": "Discuss the latest trends in blockchain technology."},
        {"name": "AI for Good Summit", "datetime": datetime(2025, 12, 20, 10, 30), "base_price": 220.00, "description": "Explore how AI can be used for good causes."},
    ]
    
    # Add each program to the database
    with app.app_context():  # Use the app context to interact with the database
        for program_data in programs:
            program = Program(
                name=program_data["name"],
                datetime=program_data["datetime"],
                base_price=program_data["base_price"],
                sale_start_datetime=sale_start_datetime,  # Sale start date is yesterday
                description=program_data["description"],
                is_cancelled=False  # Set default as not cancelled
            )
            
            # Add to the session
            db.session.add(program)
        
        # Commit to save in the database
        db.session.commit()

    print("Example programs added successfully!")


if __name__ == '__main__':
    add_example_programs()
