from django.shortcuts import render
from .models import Post  # Import the Model!

# This is a View function. It takes a request and a post_id from the URL.
def post_detail(request, post_id):
    # 1. Get the data from the Model
    #    This gets the ONE post from the database that has the matching id
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        # Handle the case where the post isn't found
        # (This is "business logic")
        return render(request, '404_error.html') 

    # 2. Prepare the "context" dictionary to send to the template
    #    The template will call this 'post_object'
    context = {
        'post_object': post,
    }

    # 3. Render the template with the context and return it
    #    It combines 'post_detail.html' with the 'context' data
    return render(request, 'post_detail.html', context)
