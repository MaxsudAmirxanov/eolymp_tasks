class Section:
    def __init__(self, name):
        self.name = name
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)

    def remove_page(self, page):
        if page in self.pages:
            self.pages.remove(page)

    def list_pages(self):
        return self.pages

class Page:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}"

# Пример использования
section = Section("Mathematics")
page1 = Page("Algebra", "Content of Algebra")
page2 = Page("Geometry", "Content of Geometry")

section.add_page(page1)
section.add_page(page2)

for page in section.list_pages():
    print(page)
