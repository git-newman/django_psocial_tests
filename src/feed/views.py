#users = UserNet.objects.prefetch_related('posts')
#for user in users:
#        for post in user.posts.all():
#            print(post)

#user = UserNet.objects.filter(username='kekw').prefetch_related('followers')
#user[0].owner.all()[0].user.username




# users = UserNet.objects.all().prefetch_related("posts").filter(posts__user__in=Follower.objects.filter(user__id=2).values('subscriber'))

# users = UserNet.objects.all().prefetch_related( Prefetch("posts", Post.objects.filter(user__in=Follower.objects.filter(user__id=2).values('subscriber'))))


# posts = Post.objects.filter(user__in=Follower.objects.filter(user__id=2).values('subscriber'))