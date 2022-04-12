from rest_framework import routers
from .api import SubjectViewSet, HomeworkViewSet, TeacherViewSet

router = routers.DefaultRouter()
router.register('subjects', SubjectViewSet, 'subjects')
router.register('homeworks', HomeworkViewSet, 'homeworks')
router.register('teachers', TeacherViewSet, 'teachers')

urlpatterns = router.urls