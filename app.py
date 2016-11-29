# Dotenv imported and used to load nessecary IDs/PWs into environment for OpenWeatherAPI and sending emails via GMAIL
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())

# Module imports
import file_reader
import weather
import mailer


def main():
	# Collect nessecary data for sending out emails
    email_addresses = file_reader.get_emails()

    schedule = file_reader.get_schedule()

    forecast = weather.get_weather_forecast()

    # Send emails
    mailer.send_emails(email_addresses, schedule, forecast)

main()

