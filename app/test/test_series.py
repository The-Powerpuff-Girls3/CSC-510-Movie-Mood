import unittest
from bs4 import BeautifulSoup
import os

class TestHTMLRendering(unittest.TestCase):

    def setUp(self):
        # 加载 HTML 文件
        base_path = os.path.abspath("src/templates/new_series.html")
        with open(base_path, 'r', encoding='utf-8') as f:
            html_doc = f.read()
        # 使用 BeautifulSoup 解析 HTML 文件内容
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    # 1. 检查container div是否存在并且包含正确的class
    def test_container_div_exists(self):
        container = self.soup.find('div', class_='container')
        self.assertIsNotNone(container, "Container div with class 'container' not found")

    # 2. 检查container的margin-top样式
    def test_container_margin_top(self):
        container = self.soup.find('div', class_='container')
        self.assertIn('margin-top: 60px;', container.get('style', ''), "Container does not have correct margin-top style")

    # 3. 检查heading1 div是否存在
    def test_heading1_div_exists(self):
        heading1 = self.soup.find('div', class_='heading1')
        self.assertIsNotNone(heading1, "Heading1 div not found")

    # 4. 检查<h2>标签是否存在并包含文本
    def test_h2_heading_exists(self):
        h2_heading = self.soup.find('h2')
        self.assertIsNotNone(h2_heading, "Heading h2 not found")
        self.assertIn("Today's Series Coming Soon!", h2_heading.text, "Incorrect h2 heading text")

    # 5. 检查<h6>标签是否存在并包含类tipHeader
    def test_h6_tip_header_exists(self):
        h6 = self.soup.find('h6', class_='tipHeader')
        self.assertIsNotNone(h6, "Tip header h6 not found")
        self.assertIn("Tip: Stay tuned for TODAY's series releases!", h6.text, "Incorrect tip header text")

    # 6. 检查alert的div是否存在
    def test_alert_div_exists(self):
        alert_div = self.soup.find('div', class_='alert alert-danger')
        self.assertIsNotNone(alert_div, "Alert div with class 'alert alert-danger' not found")

    # 7. 检查alert div的role属性
    def test_alert_role(self):
        alert_div = self.soup.find('div', class_='alert alert-danger')
        self.assertEqual(alert_div.get('role'), 'alert', "Alert div does not have role='alert'")

    # 8. 检查row类div是否存在
    def test_row_div_exists(self):
        row_div = self.soup.find('div', class_='row')
        self.assertIsNotNone(row_div, "Row div with class 'row' not found")

    # 9. 检查row div的margin-top样式
    def test_row_margin_top(self):
        row_div = self.soup.find('div', class_='row')
        self.assertIn('margin-top: 25px;', row_div.get('style', ''), "Row div does not have correct margin-top style")

    # 10. 检查col-md-12类的div是否存在
    def test_col_md_12_div_exists(self):
        col_div = self.soup.find('div', class_='col-md-12')
        self.assertIsNotNone(col_div, "Col-md-12 div not found")

    # 11. 检查Today Releases标题<h2>是否存在
    def test_today_releases_heading_exists(self):
        releases_heading = self.soup.find('h2', text="Today Releases:")
        self.assertIsNotNone(releases_heading, "Today Releases heading not found")

    # 12. 检查newSeriesList的ul是否存在
    def test_new_series_list_exists(self):
        new_series_list = self.soup.find('ul', id='newSeriesList')
        self.assertIsNotNone(new_series_list, "newSeriesList ID not found in the HTML document")

    # 13. 检查list-group类的li标签是否存在
    def test_list_group_item_exists(self):
        list_group_item = self.soup.find('li', class_='list-group-item')
        self.assertIsNotNone(list_group_item, "List group item not found")

    # 14. 检查<h3>标签是否在li项中
    def test_h3_in_list_item(self):
        list_item = self.soup.find('li', class_='list-group-item')
        h3 = list_item.find('h3') if list_item else None
        self.assertIsNotNone(h3, "h3 tag not found in list item")

    # 15. 检查<p>标签是否在li项中
    def test_p_in_list_item(self):
        list_item = self.soup.find('li', class_='list-group-item')
        p = list_item.find('p') if list_item else None
        self.assertIsNotNone(p, "p tag not found in list item")

    # 16. 检查alert消息内容
    def test_alert_message_content(self):
        alert_div = self.soup.find('div', class_='alert alert-danger')
        if alert_div:
            self.assertIn("Could not fetch new series", alert_div.text, "Alert message content mismatch")

    # 17. 检查list-group的id是否为newSeriesList
    def test_list_group_id(self):
        new_series_list = self.soup.find('ul', class_='list-group')
        self.assertEqual(new_series_list.get('id'), 'newSeriesList', "List group does not have ID 'newSeriesList'")

    # 18. 检查heading1的内容
    def test_heading1_content(self):
        heading = self.soup.find('div', class_='heading1')
        self.assertIn("Today's Series Coming Soon!", heading.text if heading else '', "Heading1 content mismatch")

    # 19. 检查tipHeader的内容
    def test_tip_header_content(self):
        tip_header = self.soup.find('h6', class_='tipHeader')
        self.assertEqual(tip_header.text.strip(), "✨Tip: Stay tuned for TODAY's series releases! ✨", "Tip header content mismatch")

    # 20. 检查container的类名
    def test_container_class(self):
        container = self.soup.find('div', class_='container')
        self.assertEqual(container.get('class'), ['container'], "Container div does not have correct class")

if __name__ == "__main__":
    unittest.main()
