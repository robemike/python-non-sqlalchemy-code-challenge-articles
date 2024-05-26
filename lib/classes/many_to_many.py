class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)

    @property
    def title (self):
        return self._title
    
    @title.setter 
    def title (self, new_title):
        if hasattr(self, 'title'):
            AttributeError('Title cannot be changed')
        else:
            if isinstance(new_title, str):
                if 5 <= len(new_title) <= 50:
                    self._title = new_title
                else: 
                    ValueError('title not chnageabe')
            else:
                ValueError('title must be string')

    @property
    def author (self):
        return self._author
    
    @author.setter 
    def author (self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            TypeError("Must be an Author")

    @property
    def magazine (self):
        return self._magazine
    
    @magazine.setter 
    def magazine (self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            TypeError("Must be a Magazine")
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name (self, new_name):

        if hasattr(self, "name"):
            AttributeError("Name not changeable")

        else:
            if isinstance(new_name, str):

                if len(new_name):
                    self._name = new_name
                else:
                    ValueError("Name cannot be empty")
            else:
                TypeError("Name must be a string")

    def articles(self):
        return [article for article in Article.all if self == article.author]
        pass

    def magazines(self):
        return list({article.magazine for article in self.articles()})
        pass

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
        pass

    def topic_areas(self):
        areas = list({magazine.category for magazine in self.magazines()})
        if areas:
            return areas
        else:
            return None
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter 
    def name(Self, new_name):

        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self_name = new_name
            else:
                ValueError("Name must be between 2 and 16 characters")
        else:
            TypeError("Name must be a string")

    @property
    def category(self):
        return self._category
    
    @category.setter 
    def category (self, new_category):
        if isinstance(new_category, str):
            if len(new_category):
                self._category = new_category
            else:
                ValueError("Category cannot be empty")
        else:
            TypeError("Category must be a string")

    def articles(self):
        return [article for article in Article.all if self == article.magazine]
        pass

    def contributors(self):
        return list({article.author for article in self.articles()})
        pass

    def article_titles(self):
        article_titles = [magazine.title for magazine in self.articles()]
        # check if article_titles list is not empty.
        if article_titles:
            return article_titles
        else:
            # when empty 
            return None

    def contributing_authors(self):
        authors = {}
        list_of_authors = []
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1  
        
        for author in authors:
            if authors[author] >= 2:
                list_of_authors.append(author) 
                  
        if (list_of_authors):
            return list_of_authors
        else:
            return None