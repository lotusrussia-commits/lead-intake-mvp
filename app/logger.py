import logging


logging.basicConfig(
    filename="events.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def log_lead_created(lead_id: int):
    logging.info(f"New lead saved: {lead_id}")


def log_error(error):
    logging.error(f"ERROR: {error}")