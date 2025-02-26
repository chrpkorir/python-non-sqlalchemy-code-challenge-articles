class Article:
    def __init__(self, author, magazine, title):
        # We use _ to store the values as private attributes
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

    # To access the title since it is a private attribute N.B title cannot be changed
    @property
    def title(self):
        return self._title
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise TypeError("magazine must be of type magazine")
        self._magazine = new_magazine
    
    @property
    def author(self):
        return self._author

    # Since author can be changed we will use a setter to implement that
    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise TypeError("Author must be of type Author")
        self._author = new_author
class Author:

    def __init__(self, name):
        self._name = name # To store a name as a private attribute which means it cannot be modified directly
        self._articles = [] # A list to store the articles that are written by author
        if not hasattr(name,"__str__"):
            raise TypeError("Names must be of type str")
        if len(name) == 0:
            raise ValueError("Names must be longer tha 0 characters")
        
    #Here we define a property name to be able to access the _name but not modify it; just read only
    @property
    def name(self):
        return self._name # 
    
    #@name.setter
    #def name(self, value):
    #    return ("Name cannot be changed after it is set")
    
    # Returns a list of all articles the author has written
    def articles(self):
        return self._articles

    # Return a unique list of magazines the aothor has contributed tpo
    # we use set() to get the unique magazines by removing any duplicates
    def magazines(self):
        return list(set(article.magazine for article in self._articles))
        
    """
     Another way we can get a unique list is by usning the for loop
    def magazines(self):
        unique_listmag = []
        for article in self._articles:
            if article.magazine not in unique_listmag:
                unique_listmag.append(article.magazine)
        return unique_listmag
        """
    def add_article(self, magazine, title):
        # Creates and returns a new Article instance and associates it with that author, the magazine provided
        if not isinstance(magazine, Magazine):
            raise TypeError("Should be of type magazine")
        article = Article(self,magazine,title)
        self._articles.append(article) # This add an article to the authors list of articles
        magazine._articles.append(article) # This add an article to the magazine's list of articles
        return article

    # Returns a unique list of strings with the categories of the magazines the author has contributed to
    def topic_areas(self):
        categories = list(set(magazine.category for magazine in self.magazines))
        # Returns None if the author has no articles
        return categories if categories else None

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = [] # List to store articles published in magazine

        
    
    # Here we use property to get the name as it is a private attribute
    @property
    def name(self):
        return self._name
    
    # To be able to change the name after instantiation we shall use a setter
    @name.setter
    def name(self, new_name):
        if not hasattr(new_name, "__str__"):
            raise TypeError("Name must be of type str")
        if not len(new_name) >= 2 and len(new_name) <= 16:
            raise ValueError("Names must between 2 and 16 characters")
        self._name = new_name

    # We use property to access category
    @property
    def category(self):
        return self._category
    
    # To be able to change the category after instantiation we shall use a setter
    @category.setter
    def category(self, new_category):
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
        return list(set(article.author for article in self._articles))

        
    # Returns a list of the titles strings of all articles written for that magazine
    # Returns None if the magazine has no articles
    def article_titles(self):
        titles = [article.title for article in self._articles]
        return titles if titles else None
    
    # Returns a list of authors who have written more than 2 articles for the magazine
    # Authors must be of type Author
    # Returns None if the magazine has no authors with more than 2 publications
    def contributing_authors(self):
        number_of_authors = {} # This initiializes an empty dictionary that stores authors as keys and the number of articles written as values
        for article in self._articles:
            # Loops through articles in _article list and .get gives the current count of the author article
            # so if the author does not exist in number_of_authors .get() returns 0
            # we initialize it by 1 on first occurence else increment 
            # the existing author by 1
            number_of_authors[article.author] = number_of_authors.get(article.author,0) + 1

        contributing_authors = [author for author, count in number_of_authors.items() if count > 2]

        return contributing_authors if contributing_authors else None


# Create authors
author1 = Author("Agatha Christie")
author2 = Author("James Patterson")
author3 = Author("Ngugu wa Thiong'o")

# create magazines
magazine1 = Magazine("Readers Digest", "Emerging Issues")
magazine2 = Magazine("Vogue", "Fashion")
magazine3 = Magazine("Business Today", "Business")

# The authors adding articles on magazines
article1 = author1.add_article(magazine1, "Fitness")
article2 = author1.add_article(magazine1, "Dieting")
article3 = author1.add_article(magazine1, "Yoga and Mindfulness")

article4 = author2.add_article(magazine3, "Stock analysis")
article5 = author3.add_article(magazine2, "Fashionista")

print(f"{author1.name} has written articles:")
for article in author1.articles():
    print(f" {article.title} (Magazine:{article.magazine.name})")

print(f"Magazines {author1.name} has written for:")
for maga in author1.magazines():
    print(f" {maga.name} ({maga.category})")
print(f" Articles published in {magazine1.name}")
for article in magazine1.articles():
    print(f" {article.title} (Author:{article.author.name})")