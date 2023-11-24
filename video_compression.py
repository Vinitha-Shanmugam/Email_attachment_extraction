# import os
# import subprocess
#
# def compress_videos(folder_path):
#     for filename in os.listdir(folder_path):
#         if filename.endswith('.mov') or filename.endswith('.mp4'):
#             input_path = os.path.join(folder_path, filename)
#             output_path = os.path.join(folder_path, f'compressed_{filename}')
#
#             ffmpeg_cmd = f'ffmpeg -i "{input_path}" -c:v libx264 -c:a copy -crf 20 "{output_path}"'
#             subprocess.run(ffmpeg_cmd, shell=True)
#
# folder_path = r'C:\Users\Vrdella\Videos\Captures'
# compress_videos(folder_path)
# # # # from django.shortcuts import render
# # # #
# # # # # from rest_framework import viewsets
# # # # # from rest_framework.response import Response
# # # # # from Video_compression_app import serializers
# # # # # import subprocess
# # # # #
# # # # #
# # # # # class VideoCompressionViewSet(viewsets.ViewSet):
# # # # #     def create(self, request):
# # # # #         serializer = serializers.VideoSerializer(data=request.data)
# # # # #         if serializer.is_valid():
# # # # #             video_file = serializer.validated_data['video']
# # # # #             size_limit = serializer.validated_data['size_limit']
# # # # #
# # # # #             # Handle the video compression using ffmpeg as shown in your original example
# # # # #
# # # # #             # Provide a download link to the user
# # # # #             compressed_video_url = "/media/compressed_video.mp4"  # Update with the actual URL
# # # # #
# # # # #             return Response({'message': 'Video compressed successfully', 'compressed_video_url': compressed_video_url})
# # # # #         return Response(serializer.errors)
# # # # from rest_framework import viewsets
# # # # from rest_framework.response import Response
# # # # from .serializers import VideoSerializer
# # # # from rest_framework.decorators import action
# # # #
# # # #
# # # # class VideoCompressionViewSet(viewsets.ViewSet):
# # # #     serializer_class = VideoSerializer  # Specify the serializer class
# # # #
# # # #     @action(detail=False, methods=['post'])
# # # #     def create(self, request):
# # # #         serializer = self.serializer_class(data=request.data)
# # # #         if serializer.is_valid():
# # # #             video_file = serializer.validated_data['video']
# # # #             size_limit = serializer.validated_data['size_limit']
# # # #
# # # #             # Handle the video compression using ffmpeg as shown in your original example
# # # #
# # # #             # Provide a download link to the user
# # # #             compressed_video_url = "/media/compressed_video.mp4"  # Update with the actual URL
# # # #
# # # #             return Response({'message': 'Video compressed successfully', 'compressed_video_url': compressed_video_url})
# # # #         return Response(serializer.errors)
# # # #
# # # #     # Add other actions as needed (e.g., list, retrieve, update, destroy)
# # # from rest_framework.parsers import MultiPartParser
# # # from rest_framework.response import Response
# # # from rest_framework.views import APIView
# # # import subprocess
# # # from Video_compression_app import serializers
# # # from Video_compression_app.models import Video
# # # from django.http import FileResponse
# # #
# # #
# # # class VideoCompressionView(APIView):
# # #     parser_classes = (MultiPartParser,)
# # #
# # #     def post(self, request):
# # #         serializer = serializers.VideoSerializer(data=request.data)
# # #         if serializer.is_valid():
# # #             video_file = serializer.validated_data['video']
# # #             size_limit = serializer.validated_data['size_limit']
# # #
# # #             # Handle the video compression using ffmpeg as shown in your original example
# # #
# # #             # Provide a  download link to the user
# # #             compressed_video_url = "/media/compressed_video.mp4"  # Update with the actual URL
# # #             compressed_video = Video(video=video_file, size_limit=size_limit)
# # #             # compressed_video_url = compressed_video.video.url
# # #
# # #             compressed_video.save()
# # #             return Response({
# # #                 'message': 'Video compressed successfully',
# # #                 'compressed_video_url': compressed_video_url,
# # #             })
# # #
# # #             # return Response({'message': 'Video compressed successfully', 'compressed_video_url': compressed_video_url})
# # #         return Response(serializer.errors)
# # from django.conf import settings
# # # from rest_framework.parsers import MultiPartParser
# # # from rest_framework.response import Response
# # # from rest_framework.views import APIView
# # # from Video_compression_app import serializers
# # # from Video_compression_app.models import Video
# # # from django.http import FileResponse
# # # import subprocess
# # #
# # #
# # # class VideoCompressionView(APIView):
# # #     parser_classes = (MultiPartParser,)
# # #
# # #     def post(self, request):
# # #         serializer = serializers.VideoSerializer(data=request.data)
# # #         if serializer.is_valid():
# # #             video_file = serializer.validated_data['video']
# # #             size_limit = serializer.validated_data['size_limit']
# # #
# # #             # Handle the video compression using ffmpeg as shown in your original example
# # #             # Compress the video and save it
# # #             compressed_video_path = r"C:\Compressed_videos"
# # #             # Perform video compression using subprocess or your preferred method
# # #             compressed_video_path = os.path.join(settings.MEDIA_ROOT, 'compressed_video.mp4')
# # #             # Create a Video model to save the compressed video
# # #             compressed_video = Video(video=compressed_video_path, size_limit=size_limit)
# # #             compressed_video.save()
# # #
# # #             # Return the compressed video as an attachment
# # #             with open(compressed_video_path, 'rb') as video_file:
# # #                 response = FileResponse(video_file)
# # #                 response['Content-Disposition'] = 'attachment; filename="compressed_video.mp4"'
# # #                 return response
# # #         return Response(serializer.errors)
# # from rest_framework.parsers import MultiPartParser
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from Video_compression_app import serializers
# # from Video_compression_app.models import Video
# # from django.http import FileResponse
# # from django.conf import settings
# # import subprocess
# # import os
# #
# #
# # class VideoCompressionView(APIView):
# #     parser_classes = (MultiPartParser,)
# #
# #     def post(self, request):
# #         serializer = serializers.VideoSerializer(data=request.data)
# #         if serializer.is_valid():
# #             video = serializer.validated_data['video']
# #             size_limit = serializer.validated_data['size_limit']
# #
# #             # Create a unique filename for the compressed video
# #             compressed_video_filename = 'videos'
# #
# #             # Create the full path to save the compressed video within the MEDIA_ROOT
# #             compressed_video_path = os.path.join(settings.MEDIA_ROOT, compressed_video_filename)
# #             compressed_video_url = os.path.join(settings.MEDIA_URL, compressed_video_filename)
# #             # Compress the video using subprocess (replace this with your compression logic)
# #             # Example subprocess command (adjust as needed)
# #             compression_command = f'ffmpeg -i "{video.temporary_file_path()}" -c:v libx264 -c:a copy -crf 20 "{compressed_video_path}"'
# #             subprocess.run(compression_command, shell=True)
# #
# #             # Create a Video model to save the compressed video
# #             compressed_video = Video(video=compressed_video_filename, size_limit=size_limit)
# #             compressed_video.save()
# #
# #             # Return the compressed video as an attachment
# #             with open(compressed_video_path, 'rb') as video_file:
# #                 response = FileResponse(video_file)
# #                 response['Content-Disposition'] = f'attachment; filename="{compressed_video_filename}"'
# #                 return response
# #         return Response(serializer.errors)
# #
# # from rest_framework.parsers import MultiPartParser
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from Video_compression_app import serializers
# # from Video_compression_app.models import Video
# # from django.http import FileResponse
# # from django.conf import settings
# # import subprocess
# # import os
# #
# #
# # class VideoCompressionView(APIView):
# #     parser_classes = (MultiPartParser,)
# #
# #     def post(self, request):
# #         serializer = serializers.VideoSerializer(data=request.data)
# #         if serializer.is_valid():
# #             video_file = serializer.validated_data['video']
# #             size_limit = serializer.validated_data['size_limit']
# #
# #             # Define the path for the compressed video
# #             compressed_video_filename = 'compressed_video.mp4'
# #             compressed_video_path = os.path.join(settings.MEDIA_ROOT, compressed_video_filename)
# #
# #             # Define the FFmpeg command for video compression
# #             compression_command = f'ffmpeg -i "{video_file.temporary_file_path()}" -c:v libx264 -c:a aac -strict experimental -b:v 1500k -minrate 1500k -maxrate 1500k -bufsize 1500k -vf scale=1280:-2 -y "{compressed_video_path}"'
# #
# #             # Execute the FFmpeg command for video compression
# #             subprocess.run(compression_command, shell=True)
# #
# #             # Create a Video model to save the compressed video
# #             compressed_video = Video(video=compressed_video_filename, size_limit=size_limit)
# #             compressed_video.save()
# #
# #             # Return the compressed video as an attachment
# #             with open(compressed_video_path, 'rb') as video_file:
# #                 response = FileResponse(video_file)
# #                 response['Content-Disposition'] = f'attachment; filename="{compressed_video_filename}"'
# #                 return response
# #
# #         return Response(serializer.errors)
# # from rest_framework.parsers import MultiPartParser
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from Video_compression_app import serializers
# # from Video_compression_app.models import Video
# # from django.http import FileResponse
# # import subprocess
# # import os
# #
# #
# # class VideoCompressionView(APIView):
# #     parser_classes = (MultiPartParser,)
# #
# #     def post(self, request):
# #         serializer = serializers.VideoSerializer(data=request.data)
# #         if serializer.is_valid():
# #             video_file = serializer.validated_data['video']
# #             size_limit = serializer.validated_data['size_limit']
# #
# #             # Define the path for the compressed video in the current directory
# #             compressed_video_filename = 'compressed_video.mp4'
# #             compressed_video_path = os.path.join(os.getcwd(), compressed_video_filename)
# #
# #             # Define the FFmpeg command for video compression
# #             compression_command = f'ffmpeg -i "{video_file.temporary_file_path()}" -c:v libx264 -c:a aac -strict experimental -b:v 1500k -minrate 1500k -maxrate 1500k -bufsize 1500k -vf scale=1280:-2 -y "{compressed_video_path}"'
# #
# #             # Execute the FFmpeg command for video compression
# #             subprocess.run(compression_command, shell=True)
# #
# #             # Return the compressed video as an attachment
# #             with open(compressed_video_path, 'rb') as video_file:
# #                 response = FileResponse(video_file)
# #                 response['Content-Disposition'] = f'attachment; filename="{compressed_video_filename}"'
# #                 return response
# #
# #         return Response(serializer.errors)
#
# # from rest_framework.parsers import MultiPartParser
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from Video_compression_app import serializers
# # from Video_compression_app.models import Video
# # from django.http import FileResponse
# # import subprocess
# # import os
# #
# #
# # class VideoCompressionView(APIView):
# #     parser_classes = (MultiPartParser,)
# #
# #     def post(self, request):
# #         serializer = serializers.VideoSerializer(data=request.data)
# #         if serializer.is_valid():
# #             video_file = serializer.validated_data['video']
# #             size_limit = serializer.validated_data['size_limit']
# #
# #             # Define the path for the compressed video in the current directory
# #             compressed_video_filename = 'compressed_video.mp4'
# #             compressed_video_path = os.path.join(os.getcwd(), compressed_video_filename)
# #
# #             # Define the FFmpeg command for video compression with target size
# #             compression_command = f'ffmpeg -i "{video_file.temporary_file_path()}" -b:v {size_limit} "{compressed_video_path}"'
# #
# #             # Execute the FFmpeg command for video compression
# #             subprocess.run(compression_command, shell=True)
# #
# #             # Return the compressed video as an attachment
# #             with open(compressed_video_path, 'rb') as video_file:
# #                 response = FileResponse(video_file)
# #                 response['Content-Disposition'] = f'attachment; filename="{compressed_video_filename}"'
# #                 return response
# #
# #         return Response(serializer.errors)
#
# # from rest_framework.parsers import MultiPartParser
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from Video_compression_app import serializers
# # from Video_compression_app.models import Video
# # from django.http import FileResponse
# # import subprocess
# # import os
# #
# #
# # class VideoCompressionView(APIView):
# #     parser_classes = (MultiPartParser,)
# #
# #     def post(self, request):
# #         serializer = serializers.VideoSerializer(data=request.data)
# #         if serializer.is_valid():
# #             video_file = serializer.validated_data['video_file']
# #             size_limit = serializer.validated_data['size_limit']
# #             compressed_video_filename = 'compressed_video.mp4'
# #             compressed_video_path = os.path.join(os.getcwd(), compressed_video_filename)
# #             compression_command = f'ffmpeg -i "{video_file.temporary_file_path()}" -c:v libx264 -c:a aac -strict experimental -b:v 1500k -minrate 1500k -maxrate 1500k -bufsize 1500k -vf scale=1280:-2 -y "{compressed_video_path}"'
# #             subprocess.run(compression_command, shell=True)
# #
# #             with open(compressed_video_path, 'rb') as video_file:
# #                 response = FileResponse(video_file)
# #                 response['Content-Disposition'] = f'attachment; filename="{compressed_video_filename}"'
# #                 return response
# #
# #         return Response(serializer.errors)
#
#
# from rest_framework.parsers import MultiPartParser
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from Video_compression_app import serializers
# from Video_compression_app.models import Video
# from django.http import FileResponse
# import subprocess
# import os
#
#
# class VideoCompressionView(APIView):
#     parser_classes = (MultiPartParser,)
#
#     def post(self, request):
#         serializer = serializers.VideoSerializer(data=request.data)
#         if serializer.is_valid():
#             video_file = serializer.validated_data['video_file']
#             size_limit = serializer.validated_data['size_limit']
#
#             # Define the path for the compressed video in the current directory
#             compressed_video_filename = 'compressed_video.mp4'
#             compressed_video_path = os.path.join(os.getcwd(), compressed_video_filename)
#
#             # Define initial compression parameters
#             current_bitrate = 1500 # Initial bitrate in kbps
#             step = 100 # Step for bitrate adjustment
#
#             while True:
#                 # Construct the FFmpeg command with the current bitrate
#                 compression_command = f'ffmpeg -i "{video_file.temporary_file_path()}" -b:v {current_bitrate}k -strict experimental -vf scale=1280:-2 -y "{compressed_video_path}"'
#
#                 # Execute the FFmpeg command for video compression
#                 subprocess.run(compression_command, shell=True)
#
#                 # Get the size of the compressed video
#                 compressed_size = os.path.getsize(compressed_video_path)
#
#                 def parse_size_limit(self, size_limit):
#                     size_limit = size_limit.strip().lower()
#                     if size_limit.endswith('kb'):
#                         return int(size_limit[:-2]) * 1024
#                     elif size_limit.endswith('mb'):
#                         return int(size_limit[:-2]) * 1024 ** 2
#                     elif size_limit.endswith('gb'):
#                         return int(size_limit[:-2]) * 1024 ** 3
#                     return int(size_limit)
#
#                 # Check if the size is within the target limit
#                 if compressed_size <= parse_size_limit(self,size_limit):
#                     break  # The compressed video size is within the limit
#                 else:
#                     # Reduce the bitrate if the size is larger than the limit
#                     current_bitrate -= step
#                     if current_bitrate <= 0:
#                         break  # Ensure we don't go below 0 bitrate
#
#             # Return the compressed video as an attachment
#             with open(compressed_video_path, 'rb') as video_file:
#                 response = FileResponse(video_file)
#                 response['Content-Disposition'] = f'attachment; filename="{compressed_video_filename}"'
#                 return response
#
#         return Response(serializer.errors)
#
#
# # from rest_framework.parsers import MultiPartParser
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from Video_compression_app import serializers
# # from Video_compression_app.models import Video
# # from django.http import FileResponse
# # import subprocess
# # import os
# #
# #
# # class VideoCompressionView(APIView):
# #     parser_classes = (MultiPartParser,)
# #
# #     def post(self, request):
# #         serializer = serializers.VideoSerializer(data=request.data)
# #         if serializer.is_valid():
# #             video_file = serializer.validated_data['video_file']
# #             size_limit = self.parse_size_limit(serializer.validated_data['size_limit'])
# #
# #             # Define the path for the compressed video in the current directory
# #             compressed_video_filename = 'compressed_video.mp4'
# #             compressed_video_path = os.path.join(os.getcwd(), compressed_video_filename)
# #
# #             min_bitrate = 50  # Minimum bitrate (adjust as needed)
# #             max_bitrate = 5000  # Maximum bitrate (adjust as needed)
# #             current_bitrate = (min_bitrate + max_bitrate) // 2  # Initial bitrate
# #
# #             while max_bitrate - min_bitrate > 10:
# #                 compression_command = f'ffmpeg -i "{video_file.temporary_file_path()}" -b:v {current_bitrate} "{compressed_video_path}"'
# #
# #                 subprocess.run(compression_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# #
# #                 compressed_size = os.path.getsize(compressed_video_path)
# #
# #                 if compressed_size > size_limit:
# #                     max_bitrate = current_bitrate
# #                 else:
# #                     min_bitrate = current_bitrate
# #
# #                 current_bitrate = (min_bitrate + max_bitrate) // 2
# #
# #                 # If the size is within the target limit with a small tolerance
# #                 if abs(compressed_size - size_limit) < 10000:  # Tolerance of 10 KB
# #                     break
# #
# #             # Return the compressed video as an attachment
# #             with open(compressed_video_path, 'rb') as video_file:
# #                 response = FileResponse(video_file)
# #                 response['Content-Disposition'] = f'attachment; filename="{compressed_video_filename}"'
# #                 return response
# #
# #         return Response(serializer.errors)
# #
# #     def parse_size_limit(self, size_limit):
# #         size_limit = size_limit.strip().lower()
# #         if size_limit.endswith('kb'):
# #             return int(size_limit[:-2]) * 1024
# #         elif size_limit.endswith('mb'):
# #             return int(size_limit[:-2]) * 1024 ** 2
# #         elif size_limit.endswith('gb'):
# #             return int(size_limit[:-2]) * 1024 ** 3
# #         return int(size_limit)
#
# # views.py
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from django.http import HttpResponse
# # from .serializers import VideoUploadSerializer
# # from .utils import compress_video
# #
# #
# # class VideoUploadView(APIView):
# #     def post(self, request):
# #         serializer = VideoUploadSerializer(data=request.data)
# #
# #         if serializer.is_valid():
# #             video = serializer.validated_data['video']
# #             compression_size = serializer.validated_data['compression_size']
# #
# #             compressed_video_path = compress_video(video, compression_size)
# #
# #             # Provide the compressed video for download
# #             with open(compressed_video_path, 'rb') as video_file:
# #                 compressed_video_data = video_file.read()
# #
# #             response = HttpResponse(compressed_video_data, content_type='video/mp4')
# #             response['Content-Disposition'] = 'attachment; filename="compressed_video.mp4"'
# #
# #             return response
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # views.py
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from .serializers import VideoUploadSerializer
# # from .utils import compress_video
# #
# #
# # class VideoUploadView(APIView):
# #     def post(self, request):
# #         serializer = VideoUploadSerializer(data=request.data)
# #
# #         if serializer.is_valid():
# #             video = serializer.validated_data['video']
# #             compression_size = serializer.validated_data['compression_size']
# #
# #             compressed_video_data = compress_video(video, compression_size)
# #
# #             # Provide the compressed video as a byte array
# #             response = Response(compressed_video_data, content_type='video/mp4')
# #             response['Content-Disposition'] = 'attachment; filename="compressed_video.mp4"'
# #
# #             return response
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# # from rest_framework.parsers import MultiPartParser
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from Video_compression_app import serializers
# # from Video_compression_app.models import Video
# # from django.http import FileResponse
# # import subprocess
# # import os
# #
# #
# # class VideoCompressionView(APIView):
# #     parser_classes = (MultiPartParser,)
# #
# #     def post(self, request):
# #         serializer = serializers.VideoSerializer(data=request.data)
# #         if serializer.is_valid():
# #             video_file = serializer.validated_data['video_file']
# #             size_limit = serializer.validated_data['size_limit']
# #
# #             def parse_size_limit(size_limit):
# #                 size_limit = size_limit.strip().lower()
# #                 if size_limit.endswith('kb'):
# #                     return int(size_limit[:-2]) * 1024
# #                 elif size_limit.endswith('mb'):
# #                     return int(size_limit[:-2]) * 1024 ** 2
# #                 elif size_limit.endswith('gb'):
# #                     return int(size_limit[:-2]) * 1024 ** 3
# #                 return int(size_limit)
# #
# #             # Define the path for the compressed video in the current directory
# #             compressed_video_filename = 'compressed_video.mp4'
# #             compressed_video_path = os.path.join(os.getcwd(), compressed_video_filename)
# #
# #             # Define initial compression parameters
# #             current_bitrate = 1500  # Initial bitrate in kbps
# #             step = 100  # Step for bitrate adjustment
# #
# #             target_size = parse_size_limit(size_limit)  # Convert size_limit using parse_size_limit
# #
# #             while True:
# #                 # Construct the FFmpeg command with the current bitrate
# #                 compression_command = f'ffmpeg -i "{video_file.temporary_file_path()}" -b:v {current_bitrate}k -strict experimental -vf scale=1280:-2 -y "{compressed_video_path}"'
# #
# #                 # Execute the FFmpeg command for video compression
# #                 subprocess.run(compression_command, shell=True)
# #
# #                 # Get the size of the compressed video
# #                 compressed_size = os.path.getsize(compressed_video_path)
# #
# #                 # Check if the size is within the target limit
# #                 if compressed_size <= target_size:
# #                     break  # The compressed video size is within the limit
# #                 else:
# #                     # Calculate a new bitrate to get closer to the target size
# #                     bitrate_difference = (compressed_size - target_size) // 1024  # in KB
# #                     current_bitrate -= bitrate_difference
# #                     if current_bitrate <= 0:
# #                         break  # Ensure we don't go below 0 bitrate
# #
# #             # Return the compressed video as an attachment
# #             with open(compressed_video_path, 'rb') as video_file:
# #                 response = FileResponse(video_file)
# #                 response['Content-Disposition'] = f'attachment; filename="{compressed_video_filename}"'
# #                 return response
# #
# #         return Response(serializer.errors)


import os
import subprocess


def compress_videos(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.mov') or filename.endswith('.mp4'):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(folder_path, f'compressed_{filename}')

            ffmpeg_cmd = f'ffmpeg -i {input_path} -c:v libx264 -c:a copy -crf 20 {output_path}'
            subprocess.run(ffmpeg_cmd, shell=True)


folder_path = r'C:\Users\Vrdella\Videos\compressed'
compress_videos(folder_path)
