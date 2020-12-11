#users = UserNet.objects.prefetch_related('posts')
#for user in users:
#        for post in user.posts.all():
#            print(post)

#user = UserNet.objects.filter(username='kekw').prefetch_related('followers')
#user[0].owner.all()[0].user.username




# users = UserNet.objects.all().prefetch_related("posts").filter(posts__user__in=Follower.objects.filter(user__id=2).values('subscriber'))

# users = UserNet.objects.all().prefetch_related( Prefetch("posts", Post.objects.filter(user__in=Follower.objects.filter(user__id=2).values('subscriber'))))


# posts = Post.objects.filter(user__in=Follower.objects.filter(user__id=2).values('subscriber'))

# Post.objects.filter(user__in=Follower.objects.filter(subscriber_id=1).values('user')) примерно такое


# Post.objects.filter(user_id__in=Follower.objects.filter(subscriber_id=1).values('user')).values('text', 'user_id', 'user__username')
# или
# Post.objects.filter(user_id__in=Follower.objects.filter(subscriber_id=1).values('user')).select_related('user')



# Post.objects.filter(user_id__in=Follower.objects.filter(subscriber_id=1).values('user'), create_date__hour__gte=10).values('text', 'user_id','user__username', 'create_date')

# Post.objects.filter(user_id__in=Follower.objects.filter(subscriber_id=1).values('user'), create_date__hour__gte=5).values('text', 'user_id','user__username', 'create_date').order_by('-create_date')[:10]
# Post.objects.filter(user__owner__subscriber_id=1).select_related('user').prefetch_related('comments')[:10]