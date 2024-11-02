import unittest
from bs4 import BeautifulSoup
import os

class TestHTMLRendering(unittest.TestCase):

    def setUp(self):
        # Load the HTML file
        base_path = os.path.abspath("src/templates/new_series.html")
        with open(base_path, 'r', encoding='utf-8') as f:
            html_doc = f.read()
        # Parse the HTML file content using BeautifulSoup
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    # 1. Check if the container div exists and contains the correct class
    def test_container_div_exists(self):
        container = self.soup.find('div', class_='container')
        self.assertIsNotNone(container, "Container div with class 'container' not found")

    # 2. Check the margin-top style of the container
    def test_container_margin_top(self):
        container = self.soup.find('div', class_='container')
        self.assertIn('margin-top: 60px;', container.get('style', ''), "Container does not have correct margin-top style")

    # 3. Check if the heading1 div exists
    def test_heading1_div_exists(self):
        heading1 = self.soup.find('div', class_='heading1')
        self.assertIsNotNone(heading1, "Heading1 div not found")

    # 4. Check if the <h2> tag exists and contains the correct text
    def test_h2_heading_exists(self):
        h2_heading = self.soup.find('h2')
        self.assertIsNotNone(h2_heading, "Heading h2 not found")
        self.assertIn("Today's Series Coming Soon!", h2_heading.text, "Incorrect h2 heading text")

    # 5. Check if the <h6> tag exists and contains the class tipHeader
    def test_h6_tip_header_exists(self):
        h6 = self.soup.find('h6', class_='tipHeader')
        self.assertIsNotNone(h6, "Tip header h6 not found")
        self.assertIn("Tip: Stay tuned for TODAY's series releases!", h6.text, "Incorrect tip header text")

    # 6. Check if the alert div exists
    def test_alert_div_exists(self):
        alert_div = self.soup.find('div', class_='alert alert-danger')
        self.assertIsNotNone(alert_div, "Alert div with class 'alert alert-danger' not found")

    # 7. Check the role attribute of the alert div
    def test_alert_role(self):
        alert_div = self.soup.find('div', class_='alert alert-danger')
        self.assertEqual(alert_div.get('role'), 'alert', "Alert div does not have role='alert'")

    # 8. Check if the row class div exists
    def test_row_div_exists(self):
        row_div = self.soup.find('div', class_='row')
        self.assertIsNotNone(row_div, "Row div with class 'row' not found")

    # 9. Check the margin-top style of the row div
    def test_row_margin_top(self):
        row_div = self.soup.find('div', class_='row')
        self.assertIn('margin-top: 25px;', row_div.get('style', ''), "Row div does not have correct margin-top style")

    # 10. Check if the col-md-12 class div exists
    def test_col_md_12_div_exists(self):
        col_div = self.soup.find('div', class_='col-md-12')
        self.assertIsNotNone(col_div, "Col-md-12 div not found")

    # 11. Check if the Today Releases <h2> heading exists
    def test_today_releases_heading_exists(self):
        releases_heading = self.soup.find('h2', text="Today Releases:")
        self.assertIsNotNone(releases_heading, "Today Releases heading not found")

    # 12. Check if the ul with id newSeriesList exists
    def test_new_series_list_exists(self):
        new_series_list = self.soup.find('ul', id='newSeriesList')
        self.assertIsNotNone(new_series_list, "newSeriesList ID not found in the HTML document")

    # 13. Check if the li with class list-group-item exists
    def test_list_group_item_exists(self):
        list_group_item = self.soup.find('li', class_='list-group-item')
        self.assertIsNotNone(list_group_item, "List group item not found")

    # 14. Check if the <h3> tag exists within the li item
    def test_h3_in_list_item(self):
        list_item = self.soup.find('li', class_='list-group-item')
        h3 = list_item.find('h3') if list_item else None
        self.assertIsNotNone(h3, "h3 tag not found in list item")

    # 15. Check if the <p> tag exists within the li item
    def test_p_in_list_item(self):
        list_item = self.soup.find('li', class_='list-group-item')
        p = list_item.find('p') if list_item else None
        self.assertIsNotNone(p, "p tag not found in list item")

    # 16. Check the content of the alert message
    def test_alert_message_content(self):
        alert_div = self.soup.find('div', class_='alert alert-danger')
        if alert_div:
            self.assertIn("Could not fetch new series", alert_div.text, "Alert message content mismatch")

    # 17. Check if the list-group has the id newSeriesList
    def test_list_group_id(self):
        new_series_list = self.soup.find('ul', class_='list-group')
        self.assertEqual(new_series_list.get('id'), 'newSeriesList', "List group does not have ID 'newSeriesList'")

    # 18. Check the content of the heading1
    def test_heading1_content(self):
        heading = self.soup.find('div', class_='heading1')
        self.assertIn("Today's Series Coming Soon!", heading.text if heading else '', "Heading1 content mismatch")

    # 19. Check the content of the tipHeader
    def test_tip_header_content(self):
        tip_header = self.soup.find('h6', class_='tipHeader')
        self.assertEqual(tip_header.text.strip(), "✨Tip: Stay tuned for TODAY's series releases! ✨", "Tip header content mismatch")

    # 20. Check the class name of the container
    def test_container_class(self):
        container = self.soup.find('div', class_='container')
        self.assertEqual(container.get('class'), ['container'], "Container div does not have correct class")

if __name__ == "__main__":
    unittest.main()