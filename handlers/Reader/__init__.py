from aiogram import Router

# from .Another import another_router
# from .Erros import erros_router
# from .no_money import money_router

from .Re_pass import re_pass_router
from .default_reader_handler import main_router

# from .tranlation_questions import tranlation_questions_router

Reader_router = Router()
Reader_router.include_router(main_router)
Reader_router.include_router(re_pass_router)
# Reader_router.include_router()
# Reader_router.include_router()
# Reader_router.include_router()
# Reader_router.include_router()
