from django.test import TestCase
from . models import Post

# We are also using the coverage library to test this program
# Coverage monitors the program, noting which parts of the code have been executed

# In command line -> coverage run manage.py test -> coverage report
# This produces a table within cmd line that suggests which files need testing
# Can create a more friendly version of this table by running -> coverage html -> and opening the index.html file in the newly created folder
# Coverage suggests what should be tested -> can then make tests here to run

# Run this test with python3 manage.py test

class ModelTesting(TestCase):

    # Creating a new instance of the Post model that is defined in models.py (to be tested)
    def setUp(self):
        
        self.blog = Post.objects.create(title='Test Post', author='Matt M', content='Test content', intro='Test intro', slug='test')

    # Creating a test to make sure the instance has been successfully made and the __str__ == self.title
    def test_post_model(self):
        # If the test post has been successfully created (i.e. a new post/model instance has been added to the Post database, then 'd' will return true)
        d = self.blog
        self.assertTrue(isinstance(d, Post))

        self.assertEqual(str(d), 'Test Post')



# Now we can run coverage again to confirm that this has been tested for, and the coverage % should be higher