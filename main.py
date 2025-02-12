from fasthtml.common import *
from gemini import Gemini
from dotenv import load_dotenv

load_dotenv()

app, rt = fast_app()
gemini = Gemini()

@rt("/")
def upload_form():
    return Titled(
        "Resume Review",
        Form(
            Input(type="file", name="file", accept=".pdf"),
            Button("Upload", type="submit"),
            method="post",
            enctype="multipart/form-data",
            hx_post=process_upload,
            hx_target="#feedback",
            hx_swap="innerHTML"
        ),
        Div(id="feedback")
    )

@rt("/process_upload", methods=["POST"])
def process_upload(request):
    file = request.files.get("file")
    if file:
        file_path = f"./pdfs/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        result = gemini.review(file_path)
        return Div(P("Feedback:"), P(result))
    else:
        return Div(P("No file uploaded."))

serve()
