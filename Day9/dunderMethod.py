class Books():
    def __init__(self, title, pages, content):
        self.title = title
        self.pages = int(pages)
        self.content = content

    def __str__(self):
        return self.title
    
    def __len__(self):
        words = self.content.split()
        return len(words)
    
harry_potter = Books("Harry Potter", 900 , "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
print(harry_potter.__str__())
print(harry_potter.__len__())
print(harry_potter.__dict__)