# Views
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResponseSerializer
from .third_party_api_adapters import execute_searching_workflow


class SuggestionAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Check for required parameters
            required_params = ["personality_type", "type_of_activity", "indoor_or_outdoor", "number_of_people",
                               "social", "location", "time", "date", "over_21", "filters"]

            # Validate required params
            for param in required_params:
                if param not in request.GET:
                    return JsonResponse({"detail": f"Missing required parameter: {param}"}, status=400)

            user_inputs = {
                "personality_type": request.GET.get("personality_type"),
                "type_of_activity": request.GET.get("type_of_activity"),
                "indoor_or_outdoor": request.GET.get("indoor_or_outdoor"),
                "number_of_people": request.GET.get("number_of_people"),
                "social": request.GET.get("social"),
                "location": request.GET.get("location"),
                "time": request.GET.get("time"),
                "date": request.GET.get("date"),
                "over_21": request.GET.get("over_21"),
                "filters": request.GET.getlist("filters", ""),
            }

            print(user_inputs)

            # Call external API logic function and obtain the data
            suggestion_data, response_summary = execute_searching_workflow(user_inputs)

            # Create response data - convert DocumentContent Objects to a dictionary that's serializable
            response_data = {
                # "suggestions": [{'url': suggestion.url.encode('utf-8', 'replace').decode('utf-8'),
                #                  'title': suggestion.title.encode('utf-8', 'replace').decode('utf-8'),
                #                  'description': suggestion.extract.encode('utf-8', 'replace').decode('utf-8')}
                #                 for suggestion in suggestion_data],
                "suggestions": [{'url': suggestion.url,
                                 'title': suggestion.title,
                                 'description': suggestion.extract}
                                for suggestion in suggestion_data],
                "response_summary": response_summary,
            }

            print(response_data)

            serializer = ResponseSerializer(data=response_data)
            if serializer.is_valid():
                return Response(serializer.validated_data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            return JsonResponse({"detail": "Invalid value"}, status=400)
        except Exception as e:
            return JsonResponse({"detail": str(e)}, status=500)
