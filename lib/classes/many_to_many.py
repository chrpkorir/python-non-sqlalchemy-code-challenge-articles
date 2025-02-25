class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        if not isinstance(author, Author):
            raise TypeError("Author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be of type magazine")
        if not hasattr(title, "__str__"):
            raise TypeError("Title must be of type str")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
    
    @property
    def title(self):
        return self._title
    
    @property
    def magazine(self):
        return self._magazine
    
    @property
    def author(self):
        return self._author

class Author:

    def __init__(self, name):
        self.name = name
        self._articles = [] # A list to store the articles that are written by author
        if not hasattr(name,"__str__"):
            raise TypeError("Names must be of type str")
        if len(name) == 0:
            raise ValueError("Names must be longer tha 0 characters")
        
    
    @property
    def name(self):
        return self._name # 
    
    @name.setter
    def name(self, value):
        return ("Name cannot be changed after it is set")
    
    # Returns a list of all articles the author has written
    def articles(self):
        return self._articles

    # Return a unique list of magazines the aothor has contributed tpo
    # we use set() to get the unique magazines by removing any duplicates
    def magazines(self):
        return list(set(article.magazine for article in self._articles))
        

    def add_article(self, magazine, title):
        # Creates and returns a new Article instance and associates it with that author, the magazine provided
        if not isinstance(magazine, Magazine):
            raise TypeError("Should be of type magazine")
        article = Article(self,magazine,title)
        return article
    # Returns a unique list of strings with the categories of the magazines the author has contributed to
    def topic_areas(self):
        categories = list(set(Magazine.category for magazine in self.magazines))
        # Returns None if the author has no articles
        return categories if categories else None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = [] # List to store articles published in magazine

        if not hasattr(name, "__str__"):
            raise TypeError("Name must be of type str")
        if len(name) >= 2 and len(name) <= 16:
            raise ValueError("Names must between 2 and 16 characters")
    
    # Returns the magazine's category
    # Categories must be of type str
    # Categories must be longer than 0 characters
    # Should be able to change after the magazine is instantiated.
    @property
    def category(self):
        return self.category
    
    @category.setter
    def category(self, new_category:str):
        if not isinstance(new_category, str):
            raise TypeError("Category must be of type str")
        if len(new_category) == 0:
            raise ValueError("Categories must be longer than 0 characters")
        self._category = new_category

    # Returns a list of all the articles the magazine has published
    def articles(self):
        return self._articles

    # Returns a unique list of authors who have written for this magazine
    def contributors(self):
        return list(set(article.author for article in self.articles))

        
    # Returns a list of the titles strings of all articles written for that magazine
    # Returns None if the magazine has no articles
    def article_titles(self):
        titles = [article.title for article in self.articles]
        return titles if titles else None
    
    # Returns a list of authors who have written more than 2 articles for the magazine
    # Authors must be of type Author
    # Returns None if the magazine has no authors with more than 2 publications
    def contributing_authors(self):
        number_of_authors = {}
        for article in self.articles:
            number_of_authors[article.author] = number_of_authors.get(article.author,0) + 1

        contributing_authors = [author for author, count in number_of_authors.items() if count > 2]

        return contributing_authors if contributing_authors else None



authora = Author("Bill")
magazine1 = Magazine("Seeds of Gold", "Agriculture")
article1 = authora.add_article(magazine1, "Business Daily")
ticle1 = authora.add_article(magazine1, "Technology Today")

print(f"{authora.name} has written articles: {[article.title for articl in authora.articles()]}")
