from rest_framework import serializers
from .models import Folder,File
import shutil



class FilelistSerializer(serializers.Serializer):
    files=serializers.ListField(child=serializers.FileField(max_length=100000,allow_empty_file=False,use_url=False))
    folder=serializers.CharField(required=False)

    def zip_file(self,folder):
        shutil.make_archive( f'static/zip/{folder}', 'zip', f'static/{folder}')


    def create(self, validated_data):
        folder=Folder.objects.create()
        files=validated_data.pop('files')
        filelist=[]
        for file in files:
            file_obj=File.objects.create(folder=folder,file=file)
            filelist.append(file_obj)
        self.zip_file(folder.uid)
        return {'files':{}, 'folder':str(folder.uid)}
        