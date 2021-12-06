from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from base.models import Topic
from .serializers import TopicSerializer
from base.api import serializers
from rest_framework import status


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def getTopics(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def getTopic(request, pk):
    topic = Topic.objects.get(id=pk)
    if request.method == 'GET':
        serializer = TopicSerializer(topic, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(("GET",))
def external_api_view(request):
    MAX_RETRIES = 2
    clist_response = None
    if request.method == "GET":
        attempt_num = 0  # keep track of how many times we've retried
        while attempt_num < MAX_RETRIES:
            url = "https://dev.to/api/articles"
            payload = {
                "per_page": "5",
                "tag": tagg,  # this is requesting contest list
            }
            r = requests.get(url, payload)
            # print(r)
            if r.status_code == 200:
                data = r.json()
                clist_response = r.json()
                # clist_response = json.load(clist_response)
                for cur_contest in clist_response["objects"]:
                    cur_id = int(cur_contest["id"])
                    cheese_blog = Contest.objects.filter(id=cur_id)

                    if len(cheese_blog) == 0:  # new contest
                        new_contest = Contest(
                            link=cur_contest["href"],
                            id=cur_contest["id"],
                            details=cur_contest["event"],
                            date=parsed_date,
                        )
                        new_contest.save()
                    else:
                        print(cheese_blog)

                return Response(data, status=status.HTTP_200_OK)
            else:
                attempt_num += 1
                # You can probably use a logger to log the error here
                time.sleep(5)  # Wait for 5 seconds before re-trying

        return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "asd"}, status=status.HTTP_200_OK)


"""
{
        "type_of": "article",
        "id": 909997,
        "title": "Advanced Interview Questions",
        "description": "Welcome to my post, I will list some of the interview questions that I encountered in the interview...",
        "readable_publish_date": "Nov 27",
        "slug": "advanced-interview-questions-m8l",
        "path": "/shoaib0023/advanced-interview-questions-m8l",
        "url": "https://dev.to/shoaib0023/advanced-interview-questions-m8l",
        "comments_count": 0,
        "public_reactions_count": 0,
        "collection_id": null,
        "published_timestamp": "2021-11-27T18:14:40Z",
        "positive_reactions_count": 0,
        "cover_image": "https://res.cloudinary.com/practicaldev/image/fetch/s--HVz7ibJa--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/96yw9cy3bxl17gfscape.jpg",
        "social_image": "https://res.cloudinary.com/practicaldev/image/fetch/s--ZGoryaDb--/c_imagga_scale,f_auto,fl_progressive,h_500,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/96yw9cy3bxl17gfscape.jpg",
        "canonical_url": "https://dev.to/shoaib0023/advanced-interview-questions-m8l",
        "created_at": "2021-11-26T15:57:22Z",
        "edited_at": "2021-11-27T18:17:53Z",
        "crossposted_at": null,
        "published_at": "2021-11-27T18:14:40Z",
        "last_comment_at": "2021-11-27T18:14:40Z",
        "reading_time_minutes": 4,
        "tag_list": [
            "programming",
            "startup",
            "challenge",
            "python"
        ],
        "tags": "programming, startup, challenge, python",
        "user": {
            "name": "Mo Shoaib",
            "username": "shoaib0023",
            "twitter_username": null,
            "github_username": "Shoaib0023",
            "website_url": null,
            "profile_image": "https://res.cloudinary.com/practicaldev/image/fetch/s--ISUCKnbz--/c_fill,f_auto,fl_progressive,h_640,q_auto,w_640/https://dev-to-uploads.s3.amazonaws.com/uploads/user/profile_image/624980/837f60a5-b7fb-4dab-9383-8d6d6e1ecba1.jpeg",
            "profile_image_90": "https://res.cloudinary.com/practicaldev/image/fetch/s--qLxO84b1--/c_fill,f_auto,fl_progressive,h_90,q_auto,w_90/https://dev-to-uploads.s3.amazonaws.com/uploads/user/profile_image/624980/837f60a5-b7fb-4dab-9383-8d6d6e1ecba1.jpeg"
        },
        "flare_tag": {
            "name": "challenge",
            "bg_color_hex": "#bf1942",
            "text_color_hex": "#ffffff"
        }
    }

"""
