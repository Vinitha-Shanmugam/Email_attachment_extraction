import imaplib
import email
from email.header import decode_header


def extract_attachments(email_user, email_password, mail_server, save_path, email_ids):
    # Connect to the mail server
    mail = imaplib.IMAP4_SSL(mail_server)
    mail.login(email_user, email_password)

    # Loop through the specified email IDs and fetch the attachments
    for email_id in email_ids:
        _, msg_data = mail.fetch(email_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Check if the email has attachments
        if msg.get_content_maintype() == "multipart":
            for part in msg.walk():
                if part.get_content_maintype() == "multipart" or part.get("Content-Disposition") is None:
                    continue
                filename = part.get_filename()
                if filename:
                    # Decode the filename if it is encoded
                    filename, encoding = decode_header(filename)[0]
                    if isinstance(filename, bytes):
                        filename = filename.decode(encoding or "utf-8")

                    # Save the attachment
                    with open(save_path + filename, "wb") as attachment:
                        attachment.write(part.get_payload(decode=True))

    # Logout from the mail server
    mail.logout()


def check_subject_and_download(email_user, email_password, mail_server, keyword):
    # Connect to the mail server
    mail = imaplib.IMAP4_SSL(mail_server)
    mail.login(email_user, email_password)

    # Select the mailbox (inbox in this case)
    mail.select("inbox")

    # Search for all unread emails
    status, messages = mail.search(None, "(UNSEEN)")

    # Get the list of email IDs
    email_ids = messages[0].split()

    # Loop through the email IDs and check the subject
    matching_email_ids = []
    for email_id in email_ids:
        _, msg_data = mail.fetch(email_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Check the subject of the email
        subject = decode_header(msg["Subject"])[0][0]
        if isinstance(subject, bytes):
            subject = subject.decode("utf-8")

        # Check if the keyword is present in the subject
        if keyword.lower() in subject.lower():
            print(f"Email with subject containing '{keyword}' found.")
            matching_email_ids.append(email_id)

    # Extract attachments if matching emails are found
    if matching_email_ids:
        extract_attachments(email_user, email_password, mail_server, "C:\\Users\\Vrdella\\attachments\\",
                            matching_email_ids)

    # Logout from the mail server
    mail.logout()


# Example usage:
check_subject_and_download('vinitha.s@vrdella.com', 'udbb zntf hhwe fbxl', 'imap.gmail.com', "attachment")
