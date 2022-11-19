import os

from .base_interface import BaseInterface


class SendGridAPIClient(BaseInterface):
    """The Twilio SendGrid API Client.
    Use this object to interact with the v3 API. For example:
        mail_client = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        ...
        mail = Mail(from_email, subject, to_email, content)
        response = mail_client.send(mail)
    For examples and detailed use instructions, see
        https://github.com/sendgrid/sendgrid-python
    """

    def __init__(
            self,
            api_key=None,
            host='https://api.sendgrid.com',
            impersonate_subuser=None):
        """
        Construct the Twilio SendGrid v3 API object.
        Note that the underlying client is being set up during initialization,
        therefore changing attributes in runtime will not affect HTTP client
        behaviour.
        :param api_key: Twilio SendGrid API key to use. If not provided, value
                        will be read from environment variable "SENDGRID_API_KEY"
        :type api_key: string
        :param impersonate_subuser: the subuser to impersonate. Will be passed
                                    by "On-Behalf-Of" header by underlying
                                    client. See
                                    https://sendgrid.com/docs/User_Guide/Settings/subusers.html
                                    for more details
        :type impersonate_subuser: string
        :param host: base URL for API calls
        :type host: string
        """
        self.api_key = api_key or os.environ.get('SENDGRID_API_KEY')
        auth = 'Bearer {}'.format(self.api_key)

        super(SendGridAPIClient, self).__init__(auth, host, impersonate_subuser)