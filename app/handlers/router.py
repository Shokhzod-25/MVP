from fastapi import BackgroundTasks
import os

from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.schemas.schemas import UserData
from app.utils.document import create_doc_file

router = APIRouter(tags=["templates"])


@router.post("/file")
async def create_file(user_data: UserData, background_tasks: BackgroundTasks):
    await create_doc_file(user_data)

    file_path = f"{user_data.file_name}.docx"

    background_tasks.add_task(os.remove, file_path)

    return FileResponse(
        path=file_path,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename=f"{user_data.file_name}.docx",
    )
