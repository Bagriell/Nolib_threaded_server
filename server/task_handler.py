"""Module defining class that saves data into several formats"""

import json
import smtplib
import threading
from email import message

from config import cfg
from database import SqliteHandler
from logger import file_logger, logger
from model import CustomerEvent


class TaskHandler:
    """Class that saves data into logfile, sqlite db, mail."""

    def __init__(self):
        self.thread = threading.current_thread().name
        self.database = SqliteHandler()

    def save_event(self, event: CustomerEvent):
        """Save an event to logfile, db, mail.

        Args:
            event (CustomerEvent): The event to be saved.
        """
        self._write_log(event)
        self._write_to_db(event)
        self._send_mail(event)

    def _write_log(self, event: CustomerEvent):
        """Save event to logfile.

        Args:
            event (CustomerEvent): The event to be saved.
        """
        file_logger.info(event)
        logger.info(f"{self.thread}: data added to logfile.")

    def _write_to_db(self, event: CustomerEvent):
        """Save event to sqlite db.
        Db table must be created or call 'self.database.create_table' before.

        Args:
            event (CustomerEvent): The event to be saved.
        """
        self.database.insert_data(event)
        logger.info(f"{self.thread}: data added to sqlite.")

    def _send_mail(self, event: CustomerEvent):
        """Send an email notification with the event details.
        Only handle sender gmail account properly configured.

        Args:
            event (CustomerEvent): The event to be included in the email notification.
        """
        mail_sender = cfg.SMTP_SENDER
        mail_receiver = cfg.SMTP_RECEIVER
        mail_subject = "event notification"
        mail_body = json.dumps(event.to_dict())
        sender_pwd = cfg.SMTP_SENDER_PWD

        try:
            msg = message.Message()
            msg.add_header("from", mail_sender)
            msg.add_header("to", mail_receiver)
            msg.add_header("subject", mail_subject)
            msg.set_payload(mail_body)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(mail_sender, sender_pwd)
            server.sendmail(mail_sender, mail_receiver, msg.as_string())
        except Exception as error:
            logger.error(f"{self.thread}: data not sent by mail: {error}.")
            return
        logger.info(f"{self.thread}: data sent by mail.")
