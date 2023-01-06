from rest_framework import generics as rest_generic_views, permissions, exceptions as rest_exceptions

from todo.todos_api.models import Todo, Category
from todo.todos_api.serializers import TodoForCreateSerializer, TodoForListSerializer, CategorySerializer, \
    TodoForDetailsSerializer


class ListCreateTodoApiView(rest_generic_views.ListCreateAPIView):
    queryset = Todo.objects.all()
    create_serializer_class = TodoForCreateSerializer
    list_serializer_class = TodoForListSerializer
    filter_names = ('category',)

    permission_classes = (
        permissions.IsAuthenticated,
    )

    # Because we have two diff serializers here depending on the request
    # we use one of them. That way we do not need to create another view.
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.list_serializer_class
        return self.create_serializer_class

    # Get only those created by our user.

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)

        return self.__apply_filters_to_queryset(queryset)

    # Get only those from a category
    def __apply_filters_to_queryset(self, queryset):
        queryset_params = {}
        for filter_name in self.filter_names:
            filter_id = self.request.query_params.get(filter_name, None)
            if filter_id:
                queryset_params[f'{filter_name}'] = filter_id
            return queryset.filter(**queryset_params)


class DetailsTodoApiView(rest_generic_views.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoForDetailsSerializer
    # Only auth users can update
    permission_classes = (
        permissions.IsAuthenticated,
    )

    # Only creator can update
    def get_object(self):
        todo = super().get_object()
        if todo.user != self.request.user:
            raise rest_exceptions.PermissionDenied
        return todo


class ListCategoriesApiView(rest_generic_views.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    # Get only different categories which have something in them.
    def get_queryset(self):
        return self.queryset.filter(todo__user_id=self.request.user.id).distinct()


