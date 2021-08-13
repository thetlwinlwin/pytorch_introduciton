class BlogPost:
    def __init__(self,title, author, created_timestamp, update_timestamp, content):
        self.title = title
        self.author = author
        self.created_timestamp = created_timestamp
        self.update_timestamp = update_timestamp
        self.content = content
        
blog_post1 = BlogPost(title='One Act of Random Kindness', author='ThetLwin', created_timestamp='12 October 2010', update_timestamp='7 December 2020', content='Just do one act to random kindness will make you happy.')

def render_blogpost(blogpost):
    print(f'The Title of the book is {blogpost.title}')
    print(f'That book was created by {blogpost.author} in {blogpost.created_timestamp}')

render_blogpost(blog_post1)
    