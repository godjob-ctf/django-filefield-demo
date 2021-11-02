from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import render
from django.views import View

from demoapp.models import DemoModel


class DemoView(View):
    def get(self, request):
        return render(request, "demoapp/index.html", {"message": "Select a PNG file"})

    def post(self, request):
        input_file = request.FILES.get("input_file")

        if not input_file:
            return render(
                request, "demoapp/index.html", {"message": "You did not select a file"}
            )

        # create empty file to save the thumbnail later
        processed_file = SimpleUploadedFile(
            input_file.name, b"", content_type=input_file.content_type
        )

        image = Image.open(input_file)
        image.thumbnail((100, 100))
        image.save(processed_file)

        instance = DemoModel.objects.create(
            input_file=input_file, processed_file=processed_file
        )

        return render(
            request,
            "demoapp/index.html",
            {
                "message": "File processed",
                "uploaded": True,
                "input_file": instance.input_file,
                "processed_file": instance.processed_file,
            },
        )
