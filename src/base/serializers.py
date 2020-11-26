from rest_framework import serializers


class FilterCommentListSerializer(serializers.ListSerializer):
    """только parent коменты"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """вывод потомков рекурсивно"""
    def to_representation(self, data):
        serializer = self.parent.parent.__class__(data, context=self.context)
        return serializer.data
