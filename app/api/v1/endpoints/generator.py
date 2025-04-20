"""Resume generator endpoints."""
import logging
import tempfile

from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse

from app.models.resume import ResumeData
from app.services.generator import ResumeGenerator
from app.services.style import Style
from app.services.utils import remove_file

_LOGGER = logging.getLogger(__name__)
router = APIRouter(prefix="/v1")


@router.post("/resume/generate", tags=["resume"])
async def generate_resume(data: ResumeData):
    """
    Generate a resume PDF from the provided resume data.

    This endpoint accepts resume data in JSON format, processes it,
    and generates a PDF file.

    Args:
        data: ResumeData object containing resume details.
        background_tasks: FastAPI BackgroundTasks object to manage background processing.

    Returns:
        FileResponse: A response containing the generated PDF file.

    Raises:
        HTTPException: If an error occurs during resume generation.
    """
    try:
        _LOGGER.info("Start generate resume endpoint")
        file_name = f"{data.name.lower().replace(" ", "_")}"
        file_name = file_name.replace(".", "_").replace(",", "_")
        generator = ResumeGenerator(style=Style())

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
            pdf_path = f.name

        generator.generate_pdf(data.model_dump(), output_path=pdf_path)

        _LOGGER.info("Generate resume service done")
        return FileResponse(
            path=pdf_path,
            media_type="application/pdf",
            filename=file_name,
            headers={
                "Content-Disposition": f"attachment; filename={file_name}"
            },
            background=BackgroundTasks([lambda: remove_file(pdf_path)])
        )
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating resume: {exc}"
        ) from exc
