from rest_framework import routers
from .views import NoteView

router = routers.DefaultRouter()
router.register('notes', NoteView)
