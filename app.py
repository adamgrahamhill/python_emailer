import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())
import file_reader
import weather
import mailer


def main():
    emails = file_reader.get_emails()

    schedule = file_reader.get_schedule()

    forecast = weather.get_weather_forecast()

    mailer.send_emails(emails, schedule, forecast)

main()

