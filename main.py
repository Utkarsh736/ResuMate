from fasthtml.common import *
from gemini import Gemini
from dotenv import load_dotenv
import os
import tempfile
from file_processing import process_resume_file

load_dotenv()

app, rt = fast_app()
gemini = Gemini()
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED_TYPES = {"application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"}

@rt("/")
def upload_form():
    return Titled(
        "Resume Review Service",
        Div(
            Form(
                Div(
                    Input(type="file", name="file", 
                         accept=".pdf,.docx",
                         class_="form-control"),
                    Button("Upload Resume", type="submit", 
                          class_="btn btn-primary mt-3"),
                    class_="mb-3"
                ),
                method="post",
                enctype="multipart/form-data",
                hx_post="/process",
                hx_target="#feedback",
                hx_swap="innerHTML",
                hx_trigger="submit",
                hx_indicator="#spinner"
            ),
            Div(id="feedback", class_="mt-4"),
            Div(class_="htmx-indicator", id="spinner", 
               style="display: none;")(
                Div(class_="spinner-border", role="status")(
                    Span(class_="visually-hidden")("Loading...")
                )
            )
        ),
        style="max-width: 800px; margin: 0 auto; padding: 2rem;"
    )

@rt("/process", methods=["POST"])
def process_resume(request):
    try:
        if "file" not in request.files:
            return Div(P("No file uploaded"), class_="alert alert-danger")
            
        file = request.files["file"]
        if not file or file.filename == "":
            return Div(P("Invalid file"), class_="alert alert-danger")
        
        # Validate file size
        file.file.seek(0, os.SEEK_END)
        file_size = file.file.tell()
        file.file.seek(0)
        if file_size > MAX_FILE_SIZE:
            return Div(P("File too large (max 5MB)"), class_="alert alert-danger")
        
        # Validate file type
        file_type = file.content_type
        if file_type not in ALLOWED_TYPES:
            return Div(P("Invalid file type. Only PDF and DOCX allowed"), 
                      class_="alert alert-danger")
        
        # Process file
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            file.save(tmp_file.name)
            text_content = process_resume_file(tmp_file.name, file_type)
            os.unlink(tmp_file.name)
        
        # Get AI feedback
        feedback = gemini.review(text_content)
        return Div(
            H3("Analysis Results", class_="mb-3"),
            Div(
                H4("Professional Feedback", class_="text-primary"),
                Pre(feedback["review"], class_="p-3 bg-light rounded"),
                class_="mb-4"
            ),
            Div(
                H4("Improved Resume Text", class_="text-success"),
                Pre(feedback["revisedResume"], class_="p-3 bg-light rounded")
            )
        )
        
    except Exception as e:
        return Div(
            P("Error processing file:", class_="text-danger"),
            Pre(str(e)),
            class_="alert alert-danger"
        )

@rt("/favicon.ico")
def favicon():
    print("Favicon request received")  # Will not appear in logs if route isn't matched
    return FileResponse("static/favicon.ico")

@rt("/debug-file-check")
def file_check():
    return {
        "exists": os.path.exists("static/favicon.ico"),
        "path": os.path.abspath("static/favicon.ico")
    }


if __name__ == "__main__":
    serve()