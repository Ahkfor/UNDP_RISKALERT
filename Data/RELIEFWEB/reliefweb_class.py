from helper import *


class ReliefWebClass:
    APP_IDENTIFIER = "DESKTOP-06R1BSH"
    LIMIT = 500

    def __init__(self, country=None):
        self.event_data = None
        self.country = country
        self.report_data = None
        self.get_report_data()
        self.report_text = []

    def get_report_data(self):
        """
        Retrieves the reports
        """
        theme = "reports"
        base_url = construct_url(self.APP_IDENTIFIER, theme, self.LIMIT, self.country)
        self.report_data = fetch_data(base_url)

    def get_passage(self, num):
        url = self.report_data['href'].iloc[num]
        text = read_report(url)
        return text


one = ReliefWebClass(country="AFG")
text = one.get_passage(2)
print(text)
file_path = "body_text.txt"
# Save the text to the file
with open(file_path, "w", encoding="utf-8") as file:
    file.write(text)
print(f"Text has been saved to {file_path}")